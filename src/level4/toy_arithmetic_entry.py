from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Any
import json
import math

from src.level4.toy_basis import TriangularLogBump, convolution_eval_x, build_default_toy_basis


EULER_GAMMA_APPROX = 0.5772156649015329


def is_prime_power(n: int) -> tuple[bool, int]:
    if n < 2:
        return (False, 0)
    for p in range(2, int(math.sqrt(n)) + 1):
        if n % p == 0:
            k = 0
            temp = n
            while temp % p == 0:
                temp //= p
                k += 1
            if temp == 1:
                return (is_prime(p), p)
            return (False, 0)
    return (True, n)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r = int(math.sqrt(n))
    for q in range(3, r + 1, 2):
        if n % q == 0:
            return False
    return True


def von_mangoldt(n: int) -> float:
    ok, p = is_prime_power(n)
    return math.log(p) if ok else 0.0


@dataclass(frozen=True)
class ToyEntryComponents:
    central: float
    central_star: float
    prime: float
    constant: float
    archimedean: float

    @property
    def entry_value(self) -> float:
        return self.central + self.central_star - self.prime - self.constant - self.archimedean

    def to_dict(self) -> Dict[str, float]:
        return {
            "central": self.central,
            "central_star": self.central_star,
            "prime": self.prime,
            "constant": self.constant,
            "archimedean": self.archimedean,
            "entry_value": self.entry_value,
        }


def F_ij_x(phi_j: TriangularLogBump, phi_i: TriangularLogBump, x: float, conv_steps: int = 800) -> float:
    return convolution_eval_x(phi_j, phi_i, x, steps=conv_steps)


def F_star_x(phi_j: TriangularLogBump, phi_i: TriangularLogBump, x: float, conv_steps: int = 800) -> float:
    if x <= 0:
        return 0.0
    return (1.0 / x) * F_ij_x(phi_j, phi_i, 1.0 / x, conv_steps=conv_steps)


def integrate_x(func, lo: float, hi: float, steps: int) -> float:
    if hi <= lo:
        return 0.0
    h = (hi - lo) / steps
    total = 0.0
    for k in range(steps):
        x = lo + (k + 0.5) * h
        total += func(x)
    return total * h


def compute_toy_entry(
    phi_j: TriangularLogBump,
    phi_i: TriangularLogBump,
    B: float = 1.0,
    integral_steps: int = 600,
    conv_steps: int = 500,
) -> ToyEntryComponents:
    """
    Floating-point, non-certified prototype for M_ij = T[phi_j * phi_i^*].
    """
    M = math.exp(2.0 * B)
    lo = math.exp(-2.0 * B)
    hi = M

    def F(x: float) -> float:
        return F_ij_x(phi_j, phi_i, x, conv_steps=conv_steps)

    def Fs(x: float) -> float:
        return F_star_x(phi_j, phi_i, x, conv_steps=conv_steps)

    central = integrate_x(F, lo, hi, integral_steps)
    central_star = integrate_x(Fs, lo, hi, integral_steps)

    prime = 0.0
    for n in range(1, int(math.floor(M)) + 1):
        lam = von_mangoldt(n)
        if lam:
            prime += lam * (F(float(n)) + Fs(float(n)))

    F1 = F(1.0)
    constant = (math.log(4.0 * math.pi) + EULER_GAMMA_APPROX) * F1

    eps = 1e-5
    def arch_integrand(x: float) -> float:
        numerator = F(x) + Fs(x) - (2.0 * F1 / x)
        return numerator * x / (x * x - 1.0)

    arch_finite = integrate_x(arch_integrand, 1.0 + eps, M, integral_steps)
    arch_tail = -F1 * math.log((M + 1.0) / (M - 1.0))
    archimedean = arch_finite + arch_tail

    return ToyEntryComponents(
        central=central,
        central_star=central_star,
        prime=prime,
        constant=constant,
        archimedean=archimedean,
    )


def write_toy_entry_certificate(output_path: Path) -> None:
    basis = build_default_toy_basis()
    comps = compute_toy_entry(basis[0], basis[0])
    payload = {
        "phase": "12Y",
        "status": "TOY_ARITHMETIC_ENTRY_PROTOTYPE_COMPLETE",
        "important_boundary": "FLOATING_POINT_PROTOTYPE_ONLY",
        "entry": {"i": 0, "j": 0, "components": comps.to_dict()},
        "audit_strings": [
            "TOY_ARITHMETIC_ENTRY_PROTOTYPE_COMPLETE",
            "TOY_CENTRAL_INTEGRAL_COMPUTED",
            "TOY_STAR_CENTRAL_INTEGRAL_COMPUTED",
            "TOY_FINITE_PRIME_SUM_COMPUTED",
            "TOY_CONSTANT_TERM_COMPUTED",
            "TOY_ARCHIMEDEAN_TERM_COMPUTED",
            "TOY_ARITHMETIC_ENTRY_COMPUTED",
            "FLOATING_POINT_PROTOTYPE_ONLY",
            "CERTIFIED_INTERVAL_ENTRY_NOT_YET_PROVED",
            "LEVEL4_READY_FOR_TOY_MATRIX_PROTOTYPE",
        ],
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    out = Path("original_results/finite_bombieri_stability/level4_candidate/toy_entry_prototype/toy_entry_certificate.json")
    write_toy_entry_certificate(out)
    print(f"Wrote {out}")
