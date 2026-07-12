from __future__ import annotations

from pathlib import Path
from dataclasses import dataclass, asdict
import math
from typing import Dict, Any, List

OUT = Path("original_results/finite_bombieri_stability/h_kernel_lipschitz/calculator/PHASE_10AC_LH_CALCULATOR_OUTPUT.txt")


@dataclass
class CompactDomain:
    R: float
    S: float
    Ry: float
    Sy: float
    delta_y: float
    buffer_r: float
    t: float

    def validate(self) -> None:
        if self.R < 0 or self.S < 0 or self.Ry < 0 or self.Sy < 0:
            raise ValueError("box radii must be nonnegative")
        if self.delta_y <= 0:
            raise ValueError("delta_y must be positive")
        if self.buffer_r <= 0:
            raise ValueError("buffer_r must be positive")
        if self.t == 0:
            raise ValueError("t must be nonzero for this finite kernel branch")


def safe_ct(t: float) -> float:
    return abs(t / math.sinh(t))


def compute_majorants(domain: CompactDomain) -> Dict[str, float]:
    domain.validate()

    t_abs = abs(domain.t)
    rho_y = math.sqrt(domain.Ry ** 2 + domain.Sy ** 2)

    A0 = math.exp(t_abs * domain.S)
    A1 = math.exp(t_abs * (domain.S + domain.buffer_r)) / domain.buffer_r

    B0 = 1.0 / domain.delta_y
    B1 = 2.0 * rho_y / (domain.delta_y ** 2)

    C0 = 0.5 + rho_y
    c_abs = safe_ct(domain.t)

    M0 = A0 + 2.0 * c_abs * C0 * (A0 ** 2)
    Mx = A1 + 2.0 * c_abs * C0 * A0 * A1
    My = A1 + 2.0 * c_abs * ((A0 ** 2) + C0 * A0 * A1)

    Lx = 2.0 * t_abs * B0 * Mx
    Ly = 2.0 * t_abs * (B1 * M0 + B0 * My)
    LH = Lx + Ly

    return {
        "rho_y": rho_y,
        "A0": A0,
        "A1": A1,
        "B0": B0,
        "B1": B1,
        "C0": C0,
        "abs_c_t": c_abs,
        "M0": M0,
        "Mx": Mx,
        "My": My,
        "Lx": Lx,
        "Ly": Ly,
        "LH": LH,
    }


def examples() -> List[CompactDomain]:
    return [
        CompactDomain(R=1.0, S=0.5, Ry=1.0, Sy=0.25, delta_y=0.10, buffer_r=0.25, t=1.0),
        CompactDomain(R=2.0, S=0.75, Ry=1.5, Sy=0.20, delta_y=0.20, buffer_r=0.50, t=1.25),
        CompactDomain(R=0.5, S=0.10, Ry=0.5, Sy=0.10, delta_y=0.30, buffer_r=0.25, t=0.75),
    ]


def main() -> None:
    lines = [
        "PHASE 10AC L_H CONSTANT CALCULATOR OUTPUT",
        "",
        "Exact audit phrase: LH_CONSTANT_CALCULATOR",
        "Exact audit phrase: COMPUTABLE_H_KERNEL_LIPSCHITZ_CONSTANT",
        "Exact audit phrase: CONCRETE_COMPACT_DOMAIN_MAJORANTS",
        "",
        "Formula package:",
        "  A0 = exp(|t| S)",
        "  A1 = exp(|t|(S+r))/r",
        "  B0 = 1/Delta_Y",
        "  B1 = 2 rho_y / Delta_Y^2",
        "  C0 = 1/2 + rho_y",
        "  M0 = A0 + 2|c_t|C0 A0^2",
        "  Mx = A1 + 2|c_t|C0 A0 A1",
        "  My = A1 + 2|c_t|(A0^2 + C0 A0 A1)",
        "  Lx = 2|t|B0 Mx",
        "  Ly = 2|t|(B1 M0 + B0 My)",
        "  LH = Lx + Ly",
        "",
    ]

    for i, domain in enumerate(examples(), start=1):
        result = compute_majorants(domain)
        lines.append(f"EXAMPLE {i}")
        lines.append(f"  domain={asdict(domain)}")
        for key, value in result.items():
            lines.append(f"  {key}={value}")
        lines.append("")

    lines.extend([
        "Interpretation:",
        "  LH is a computable H-kernel Lipschitz constant candidate from the compact-domain majorant package.",
        "  This calculator does not by itself complete the final Lipschitz theorem.",
        "  The next phase must prove integration into the combined-radius stability certificate.",
        "",
        "Boundary:",
        "  This calculator uses no zeta zeros.",
        "  No RH claim.",
        "  No novelty claim.",
        "  This phase does not prove RH.",
        "  This phase does not falsify RH.",
        "  This phase does not use zeta zeros.",
        "  This phase does not claim novelty.",
    ])

    OUT.write_text("\n".join(lines), encoding="utf-8")

    print("=" * 80)
    print("PHASE 10AC L_H CONSTANT CALCULATOR: COMPLETE")
    print("COMPUTABLE H-KERNEL LIPSCHITZ CONSTANT: IMPLEMENTED")
    print("CONCRETE COMPACT-DOMAIN MAJORANTS: COMPUTED")
    print("FULL LIPSCHITZ THEOREM: NOT YET")
    print("RH CLAIM: NONE")
    print("NOVELTY CLAIM: NONE")
    print("=" * 80)


if __name__ == "__main__":
    main()
