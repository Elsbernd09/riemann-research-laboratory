from __future__ import annotations

import cmath
import math
from dataclasses import dataclass


@dataclass(frozen=True)
class DefectSample:
    beta: float
    gamma: float
    x: float
    u: float
    energy: float
    quadratic_approx: float
    relative_error: float


def radial_log_defect(beta: float, gamma: float) -> float:
    rho = complex(beta, gamma)
    w = 1.0 - 1.0 / rho
    return math.log(abs(w))


def exact_formula_u(beta: float, gamma: float) -> float:
    numerator = (beta - 1.0) ** 2 + gamma ** 2
    denominator = beta ** 2 + gamma ** 2
    return 0.5 * math.log(numerator / denominator)


def sample(beta: float, gamma: float) -> DefectSample:
    x = beta - 0.5
    u1 = radial_log_defect(beta, gamma)
    u2 = exact_formula_u(beta, gamma)

    if abs(u1 - u2) > 1e-12:
        raise AssertionError((u1, u2))

    energy = u1 * u1
    quadratic_approx = x * x / ((gamma * gamma + 0.25) ** 2)

    if quadratic_approx == 0.0:
        relative_error = 0.0
    else:
        relative_error = abs(energy - quadratic_approx) / quadratic_approx

    return DefectSample(
        beta=beta,
        gamma=gamma,
        x=x,
        u=u1,
        energy=energy,
        quadratic_approx=quadratic_approx,
        relative_error=relative_error,
    )


def main() -> None:
    print("=" * 80)
    print("PHASE 7C RADIAL DEFECT ENERGY VALIDATION")
    print("=" * 80)

    gammas = [1.0, 5.0, 14.134725141734693, 50.0, 100.0]
    xs = [-0.1, -0.01, -0.001, 0.0, 0.001, 0.01, 0.1]

    for gamma in gammas:
        print(f"gamma={gamma}")

        for x in xs:
            beta = 0.5 + x
            s = sample(beta, gamma)

            assert s.energy >= -1e-15

            if abs(x) < 1e-15:
                assert abs(s.energy) < 1e-15
            else:
                assert s.energy > 0.0

            print(
                "  "
                f"x={s.x:+.6g} "
                f"u={s.u:+.12e} "
                f"D={s.energy:.12e} "
                f"quad={s.quadratic_approx:.12e} "
                f"relerr={s.relative_error:.3e}"
            )

    print("Nonnegativity: PASS")
    print("Critical-line vanishing: PASS")
    print("Small-displacement quadratic approximation: OBSERVED")
    print("=" * 80)


if __name__ == "__main__":
    main()
