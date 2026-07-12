from __future__ import annotations

import math
import cmath
from pathlib import Path
import importlib.util

module_path = Path("weil_reconstruction/finite_truncations/h_kernel_symbolic.py")
spec = importlib.util.spec_from_file_location("h_kernel_symbolic", module_path)
if spec is None or spec.loader is None:
    raise RuntimeError("Could not load h_kernel_symbolic module")

hks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hks)

TOL = 1e-9


def assert_near(a: complex, b: complex, label: str, tol: float = TOL) -> None:
    if abs(complex(a) - complex(b)) > tol:
        raise AssertionError(f"{label} failed: {a!r} vs {b!r}")


def assert_finite(z: complex, label: str) -> None:
    zc = complex(z)
    if not (math.isfinite(zc.real) and math.isfinite(zc.imag)):
        raise AssertionError(f"{label} is not finite: {z!r}")


def main() -> None:
    samples = hks.sanity_samples()
    t_values = [0.75, 1.0, 2.0]

    # K(0)=1 limiting branch.
    assert_near(hks.K(0), 1.0, "K(0)=1")

    # K is even.
    for z in samples:
        assert_near(hks.K(-z), hks.K(z), f"K evenness at {z!r}")

    # K_t is even.
    for t in t_values:
        for z in samples:
            assert_near(hks.K_t(-z, t), hks.K_t(z, t), f"K_t evenness at z={z!r}, t={t!r}")

    # Scalar values are finite for synthetic samples.
    for t in t_values:
        for x in samples:
            for y in samples:
                # Avoid the poles y=+/- i/2 caused by the denominator 1/4+y^2.
                if abs(0.25 + complex(y) * complex(y)) < 1e-8:
                    continue
                ks = hks.K_star(x, y, t)
                hv = hks.H_kernel(x, y, t)
                assert_finite(ks, f"K_star({x!r},{y!r},{t!r})")
                assert_finite(hv, f"H_kernel({x!r},{y!r},{t!r})")

    # Conjugation inspection only, not a theorem claim.
    inspection_rows = []
    for t in t_values:
        x = 0.4 + 0.2j
        y = -0.8 + 0.1j
        lhs = hks.H_kernel(x, y, t)
        rhs = hks.H_kernel(y, x, t)
        inspection_rows.append((t, lhs, rhs, lhs - rhs.conjugate()))

    out = Path("weil_reconstruction/finite_truncations/PHASE_8X_SANITY_OUTPUT.txt")
    out.write_text(
        "\n".join(
            [
                "PHASE 8X H-KERNEL SANITY OUTPUT",
                "K(0)=1: PASS",
                "K evenness: PASS",
                "K_t evenness: PASS",
                "K_star finite synthetic samples: PASS",
                "H_kernel finite synthetic samples: PASS",
                "No matrices assembled.",
                "No eigenvalues computed.",
                "No zeta zeros used.",
                "No RH claim.",
                "No novelty claim.",
                "",
                "Conjugation inspection rows only; not theorem claims:",
            ]
            + [
                f"t={t}: H(x,y;t)={lhs!r}, H(y,x;t)={rhs!r}, H(x,y)-conj(H(y,x))={diff!r}"
                for t, lhs, rhs, diff in inspection_rows
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    print("=" * 80)
    print("PHASE 8X H-KERNEL SANITY: PASS")
    print("SCALAR KERNEL FUNCTIONS: IMPLEMENTED")
    print("K(0) LIMITING BRANCH: PASS")
    print("K EVENNESS: PASS")
    print("K_t EVENNESS: PASS")
    print("FINITE SAMPLE EVALUATIONS: PASS")
    print("MATRICES ASSEMBLED: NONE")
    print("EIGENVALUES COMPUTED: NONE")
    print("ZETA ZEROS USED: NONE")
    print("RH CLAIM: NONE")
    print("NOVELTY CLAIM: NONE")
    print("=" * 80)


if __name__ == "__main__":
    main()
