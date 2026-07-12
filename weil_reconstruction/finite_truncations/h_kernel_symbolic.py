"""
Symbolic source-derived H-kernel functions for Bombieri Section 8.

This module implements only scalar kernel functions:

    K(z) = sin(z)/z
    K_t(z) = K(t z)
    K_star(x, y, t)
    H_kernel(x, y, t)

No matrices are assembled here.
No eigenvalues are computed here.
No zeta zeros are used here.
No RH claim is made here.
"""

from __future__ import annotations

import cmath
from typing import Union

Number = Union[int, float, complex]


def K(z: Number, tol: float = 1e-12) -> complex:
    """
    Stable evaluation of K(z) = sin(z)/z with K(0)=1.

    The limiting value at z=0 is used for small |z|.
    """
    zc = complex(z)
    if abs(zc) < tol:
        return complex(1.0, 0.0)
    return cmath.sin(zc) / zc


def K_t(z: Number, t: Number, tol: float = 1e-12) -> complex:
    """
    Scaled kernel K_t(z)=K(tz).
    """
    return K(complex(t) * complex(z), tol=tol)


def K_star(x: Number, y: Number, t: Number, tol: float = 1e-12) -> complex:
    """
    Source-extracted corrected kernel K^*(x,y;t).

    Formula recorded in Phase 8U:

    K^*(x,y;t)
    =
    K_t(x-y)
    -
    t/sinh(t) * (1/2+iy) K_t(i/2-y) K_t(i/2+x)
    -
    t/sinh(t) * (1/2-iy) K_t(i/2+y) K_t(i/2-x)

    This function only evaluates the formula.
    It does not assemble a matrix.
    """
    xc = complex(x)
    yc = complex(y)
    tc = complex(t)

    if abs(cmath.sinh(tc)) < tol:
        raise ZeroDivisionError("sinh(t) is too close to zero for stable K_star evaluation")

    factor = tc / cmath.sinh(tc)
    i = 1j

    term0 = K_t(xc - yc, tc, tol=tol)

    term1 = (
        factor
        * (0.5 + i * yc)
        * K_t(0.5j - yc, tc, tol=tol)
        * K_t(0.5j + xc, tc, tol=tol)
    )

    term2 = (
        factor
        * (0.5 - i * yc)
        * K_t(0.5j + yc, tc, tol=tol)
        * K_t(0.5j - xc, tc, tol=tol)
    )

    return term0 - term1 - term2


def H_kernel(x: Number, y: Number, t: Number, tol: float = 1e-12) -> complex:
    """
    Source-extracted H-kernel formula:

        H(x,y;t)=2t K^*(x,y;t)/(1/4+y^2)

    This function only evaluates scalar entries.
    It does not assemble a matrix.
    It does not compute eigenvalues.
    """
    yc = complex(y)
    denom = 0.25 + yc * yc

    if abs(denom) < tol:
        raise ZeroDivisionError("1/4 + y^2 is too close to zero for stable H evaluation")

    return (2.0 * complex(t) * K_star(x, y, t, tol=tol)) / denom


def near(a: Number, b: Number, tol: float = 1e-9) -> bool:
    """
    Numeric closeness helper for sanity checks only.
    """
    return abs(complex(a) - complex(b)) <= tol


def sanity_samples() -> list[complex]:
    """
    Deterministic sample points for scalar sanity checks.

    These are synthetic complex inputs.
    They are not zeta zeros.
    """
    return [
        0,
        0.25,
        -0.25,
        1.0,
        -1.0,
        2.0 + 0.3j,
        -2.0 - 0.3j,
        0.7 - 0.9j,
        -0.7 + 0.9j,
    ]


if __name__ == "__main__":
    print("This module defines scalar H-kernel functions only.")
    print("No matrices, eigenvalues, zeta zeros, or RH claims.")
