# Quadratic Response and the Size of the Displacement

## Question

Does the quadratic approximation

\[
R_f(\delta,\gamma) \approx \delta^2 \chi_f(\gamma),
\qquad
\chi_n^{\mathrm{Li}}(\gamma) = 2\,\mathrm{Re}\, f_n''\!\left(\tfrac12+i\gamma\right),
\]

stay meaningful for displacements up to \(\delta = 3/8\)? That value is the largest displacement not excluded by the zero-free half-plane \(\mathrm{Re}\,s > 7/8\) claimed in an unrefereed preprint (see `docs/EXTERNAL_RESULTS_REGISTER.md`, ER-0001). This project does not use that claim. The question is asked because \(\delta\) in the surgery specification ranges over \(0<\delta<1/2\).

## What the paper says and does not say

Source: `paper/latex/main.tex`, Introduction.

- The symmetric horizontal orbit response of an analytic \(f\) is
  \(R_f(\delta,\gamma)=\sum_{\epsilon,\sigma=\pm1} f(\tfrac12+\epsilon\delta+i\sigma\gamma)-2\sum_{\sigma=\pm1} f(\tfrac12+i\sigma\gamma)\).
- The paper states that Taylor expansion gives \(R_f(\delta,\gamma)=\delta^2\chi_f(\gamma)+O(\delta^4)\).
  The remainder is stated as a Taylor remainder in \(\delta\). The paper does not state a range of \(\delta\) or a uniformity in \(\gamma\) and \(n\) for it.
- The main theorem is about
  \(R_{\mathrm{int}}(n;H,\eta)=-\int_H^{(1+\eta)H}E(t)\,\chi_n'(t)\,dt\).
  **It contains no \(\delta\).** It is a statement about the kernel \(\chi_n\) and the counting discrepancy \(E\), and holds whatever the range of \(\delta\) in which \(\chi_n\) approximates a displaced-zero response.
- The abstract states that the result "is compatible with failure of the Riemann Hypothesis".

So the \(\delta\)-range affects only how \(\chi_n\) is *interpreted* (as the response of a displaced quartet), not the theorem.

## Computational observation

Script: `experiments/li_quadratic_response_delta_range.py`. Results: `results/li_quadratic_response_delta_range/`. Test: `tests/test_li_quadratic_response_delta_range.py`. Run from the repository root with `python3 -m experiments.li_quadratic_response_delta_range`. 60-digit mpmath arithmetic; the exact response is computed directly from the Li kernel by `src.li_susceptibility.signed_orbit_response`, and \(\chi_n\) by `li_susceptibility_exact`.

**Metric.** The error is \(|R-\delta^2\chi_n|/(\delta^2 A_n)\), where
\(A_n(\gamma)=2n\sqrt{n^2+4\gamma^2}/(\gamma^2+1/4)^2\) is the amplitude envelope of the exact formula for \(\chi_n\). The ratio to \(|\chi_n|\) itself is not used as the headline metric because \(\chi_n\) vanishes at blind scales, where any relative error is unbounded.

**Worst error over 100 values of \(n/\gamma\in[0.1,10]\).**

| \(\gamma\) | \(\delta=0.05\) | \(\delta=0.125\) | \(\delta=0.25\) | \(\delta=0.375\) |
|---|---|---|---|---|
| 14.1347 (first zero) | 1.2e-4 | 7.3e-4 | 2.9e-3 | **6.6e-3** |
| 21.0220 (second zero) | 5.4e-5 | 3.4e-4 | 1.3e-3 | 3.0e-3 |
| 100 | 2.4e-6 | 1.5e-5 | 6.0e-5 | 1.4e-4 |
| 1000 | 2.4e-8 | 1.5e-7 | 6.0e-7 | 1.4e-6 |

The worst case is at the top of the grid, \(n/\gamma\approx10\), in every row.

**Observations.**

1. In the matched-scale window and at the heights tested, the quadratic approximation is within about 0.7% of the envelope at \(\delta=3/8\) and at the first zero ordinate, and the error falls with height.
2. At fixed \(\delta\) the error scales like \(1/\gamma^2\) over the tested heights: the \(\delta=0.375\) column changes by factors of 49 (14.13 to 100) and 100 (100 to 1000), against \((100/14.13)^2\approx50\) and \(10^2=100\).
3. At fixed \(\gamma\) the error scales like \(\delta^2\) (each doubling of \(\delta\) multiplies it by about 4) at the smaller displacements, as expected for an \(O(\delta^2)\) relative remainder; at \(\delta=0.375\) the ratio to \(\delta=0.25\) is 2.25, as expected from \((0.375/0.25)^2\).

**Outside the matched-scale window** (first zero ordinate, \(\delta=3/8\), \(n=k\gamma^2\)). Here the relative error with respect to \(\chi_n\) is:

| \(k\) | \(n\) | relative error |
|---|---|---|
| 0.01 | 1 | −0.12% |
| 0.1 | 19 | −0.03% |
| 1 | 199 | +5.1% |
| 3 | 599 | +39% |

The approximation degrades when \(n\delta/\gamma^2\) is of order one.

## Why this is the natural scale (HEURISTIC, with one exact step)

For \(z=\tfrac12+\delta+i\gamma\) one has exactly \(|1-1/z|^2=1-2\delta/|z|^2\), since \(|z-1|^2-|z|^2=-2\delta\). Hence
\(|1-1/z|^n\approx e^{-n\delta/|z|^2}\), and the partner at \(\tfrac12-\delta+i\gamma\) carries \(e^{+n\delta/|z|^2}\). The expansion in \(\delta\) therefore has \(n\delta/\gamma^2\) as its natural small parameter, which is \(c\,\delta/\gamma\) at \(n=c\gamma\). The kernel is also singular at \(z=0\), at distance about \(\gamma\) from the critical-line point, so a Taylor series in \(\delta\) cannot have radius larger than about \(\gamma\). This accounts for the table above qualitatively; I did not derive the constants.

## Limits of this observation

- It concerns **one conjugate quartet** and the Li kernel. It does not test the aggregate response summed over many zeros, nor any aggregate with cancellations.
- It tests selected heights (the first two zero ordinates, 100 and 1000) and a grid of 100 values of \(n/\gamma\). It is a finite computation, not a uniform bound, and not a proof of the paper's \(O(\delta^4)\) remainder with explicit constants.
- The envelope-normalized error can hide a large relative error near blind scales.
- The test says nothing about whether a displaced zero of \(\zeta\) can exist. Whether \(\delta\) up to 3/8 is available to an actual zero depends on an unrefereed external claim (ER-0001).

## Ledger

Recorded as CL-E004 (COMPUTATIONAL OBSERVATION) in `research_ledger/CLAIM_LEDGER.md`.
