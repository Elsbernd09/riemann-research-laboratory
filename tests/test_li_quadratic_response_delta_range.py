import mpmath as mp

from src.li_susceptibility import li_susceptibility_exact, signed_orbit_response


def _envelope(n, g):
    return 2 * n * mp.sqrt(n * n + 4 * g * g) / (g * g + mp.mpf(1) / 4) ** 2


def _error(d, g, n):
    r = signed_orbit_response(d, g, n)
    chi = li_susceptibility_exact(n, g)
    return abs(r - d * d * chi) / (d * d * _envelope(n, g))


def test_quadratic_response_accurate_to_three_eighths_at_matched_scale():
    with mp.workdps(50):
        d = mp.mpf("0.375")
        for g in (mp.mpf("14.134725"), mp.mpf(100)):
            for c in (0.25, 0.5, 1, 2, 5, 10):
                n = max(1, int(round(c * float(g))))
                assert _error(d, g, n) < mp.mpf("0.01")


def test_error_shrinks_with_height():
    with mp.workdps(50):
        d = mp.mpf("0.375")
        e_low = _error(d, mp.mpf(20), 20)
        e_high = _error(d, mp.mpf(200), 200)
        assert e_high < e_low / 10
