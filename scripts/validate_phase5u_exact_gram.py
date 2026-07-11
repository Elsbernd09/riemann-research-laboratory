from __future__ import annotations

import math

import mpmath as mp


def coefficient(
    n: int,
    ell: int,
) -> mp.mpf:
    return mp.mpf(
        (-1) ** (ell - 1)
        * math.comb(n, ell)
        * ell
        * (ell + 1)
    )


def direct_susceptibility(
    n: int,
    gamma: mp.mpf,
) -> mp.mpf:
    z = mp.mpf("0.5") + 1j * gamma

    value = mp.mpf("0")

    for ell in range(1, n + 1):
        c = coefficient(
            n,
            ell,
        )

        value += c * (
            z ** (-ell - 2)
            +
            mp.conj(z) ** (-ell - 2)
        )

    return mp.re(value)


def gram_susceptibility(
    n: int,
    gamma: mp.mpf,
) -> mp.mpf:
    z = mp.mpf("0.5") + 1j * gamma

    c = mp.matrix(
        [
            coefficient(n, ell)
            for ell in range(1, n + 1)
        ]
    )

    v = mp.matrix(
        [mp.mpf("1")]
        +
        [
            z ** (-ell - 2)
            for ell in range(1, n + 1)
        ]
    )

    dimension = n + 1

    matrix = mp.matrix(
        dimension,
        dimension,
    )

    for row in range(dimension):
        for col in range(dimension):
            matrix[row, col] = mp.mpf("0")

    for index in range(n):
        matrix[0, index + 1] = c[index]
        matrix[index + 1, 0] = c[index]

    total = mp.mpc("0")

    for row in range(dimension):
        for col in range(dimension):
            total += (
                mp.conj(v[row])
                *
                matrix[row, col]
                *
                v[col]
            )

    return mp.re(total)


def two_channel_susceptibility(
    n: int,
    gamma: mp.mpf,
) -> mp.mpf:
    z = mp.mpf("0.5") + 1j * gamma

    coefficients = [
        coefficient(n, ell)
        for ell in range(1, n + 1)
    ]

    norm = mp.sqrt(
        mp.fsum(
            value**2
            for value in coefficients
        )
    )

    p = mp.fsum(
        coefficients[ell - 1]
        *
        z ** (-ell - 2)
        for ell in range(1, n + 1)
    ) / norm

    u_plus = (
        1 + p
    ) / mp.sqrt(2)

    u_minus = (
        1 - p
    ) / mp.sqrt(2)

    return norm * (
        abs(u_plus) ** 2
        -
        abs(u_minus) ** 2
    )


def main() -> None:
    mp.mp.dps = 80

    n_values = list(range(1, 31))

    gamma_values = [
        mp.mpf("0"),
        mp.mpf("0.25"),
        mp.mpf("1"),
        mp.mpf("3"),
        mp.mpf("10"),
        mp.mpf("25"),
        mp.mpf("100"),
    ]

    maximum_gram_error = mp.mpf("0")
    maximum_channel_error = mp.mpf("0")

    print(
        "PHASE 5U EXACT GRAM VALIDATOR"
    )
    print("=" * 88)

    for n in n_values:
        coefficients = [
            coefficient(n, ell)
            for ell in range(1, n + 1)
        ]

        norm = mp.sqrt(
            mp.fsum(
                value**2
                for value in coefficients
            )
        )

        if norm <= 0:
            raise ArithmeticError(
                f"Coefficient norm vanished at n={n}."
            )

        for gamma in gamma_values:
            direct = direct_susceptibility(
                n,
                gamma,
            )

            gram = gram_susceptibility(
                n,
                gamma,
            )

            channels = two_channel_susceptibility(
                n,
                gamma,
            )

            gram_error = abs(
                direct - gram
            )

            channel_error = abs(
                direct - channels
            )

            maximum_gram_error = max(
                maximum_gram_error,
                gram_error,
            )

            maximum_channel_error = max(
                maximum_channel_error,
                channel_error,
            )

        print(
            f"n={n:2d} "
            f"rank_prediction=2 "
            f"inertia_prediction=(1,1,{n - 1}) "
            f"coefficient_norm={mp.nstr(norm, 16)}"
        )

    threshold = mp.mpf("1e-60")

    if maximum_gram_error > threshold:
        raise ArithmeticError(
            "Exact Gram identity consistency check failed."
        )

    if maximum_channel_error > threshold:
        raise ArithmeticError(
            "Two-channel factorization consistency check failed."
        )

    print("=" * 88)

    print(
        "maximum_gram_identity_error: "
        f"{mp.nstr(maximum_gram_error, 30)}"
    )

    print(
        "maximum_two_channel_identity_error: "
        f"{mp.nstr(maximum_channel_error, 30)}"
    )

    print(
        "VALIDATION STATUS: PASS"
    )

    print(
        "INTERPRETATION: NUMERICAL CONSISTENCY ONLY. "
        "RANK AND INERTIA FOLLOW ALGEBRAICALLY FROM "
        "THE BLOCK MATRIX STRUCTURE."
    )


if __name__ == "__main__":
    main()
