# Phase 5R — Hardy/Parseval Route and Classical Keiper–Li Radius Obstruction

## Status

PRIOR-ART AND STRUCTURAL AUDIT COMPLETE.

## Objective

Determine whether Parseval or Hardy-space energy of the Keiper–Li generating function provides a distinct route for separating positive horizontal zero-defect energy.

The naive route does not.

It either fails analytically under RH or collapses to the classical Keiper–Li analytic-radius mechanism.

---

# 1. Classical Keiper generating function

Define

\[
\Phi(z)
=
\log 2\xi\left(\frac1{1-z}\right).
\]

The Keiper coefficients satisfy

\[
\Phi(z)
=
\sum_{n\ge1}
\lambda_n^K z^n.
\]

The conformal map

\[
x=\frac1{1-z}
\]

maps the half-plane

\[
\Re x>\frac12
\]

to the unit disk

\[
|z|<1.
\]

The critical line maps to the unit circle.

Classical Keiper–Li theory therefore gives

\[
\boxed{
\mathrm{RH}
\iff
\Phi
\text{ is regular throughout }
|z|<1.
}
\]

This analytic-radius mechanism is classical prior art.

---

# 2. Transformed zero singularities

For a nontrivial zero

\[
\rho,
\]

define

\[
z_\rho
=
1-\frac1\rho.
\]

The logarithmic derivative of the Keiper generating function is meromorphic and has a simple pole at each transformed zero coordinate

\[
z_\rho.
\]

If RH holds, transformed zeros lie on

\[
|z|=1.
\]

If RH fails, functional-equation symmetry produces at least one transformed zero inside

\[
|z|<1.
\]

Thus an RH-violating zero produces an interior singularity of the generating-function architecture.

This is classical Keiper–Li sensitivity.

---

# 3. Classical asymptotic separation

The classical asymptotic alternative is qualitatively:

RH false:

\[
\lambda_n^L
\]

receives exponentially growing contributions of the form

\[
z_\rho^{-n}
\]

from transformed zeros satisfying

\[
|z_\rho|<1.
\]

RH true:

\[
\lambda_n^L
=
n\left(
\frac12\log n+c
\right)
+
o(n)
\]

at the classical asymptotic scale.

Since

\[
\lambda_n^L
=
n\lambda_n^K,
\]

RH true gives

\[
\lambda_n^K
=
\frac12\log n+c+o(1).
\]

Therefore qualitative detection of interior singularities through exponential coefficient growth is already classical.

---

# 4. Ordinary Hardy H2 obstruction

The ordinary Hardy \(H^2\) coefficient condition would require

\[
\sum_{n\ge1}
|\lambda_n^K|^2
<
\infty.
\]

Under RH,

\[
\lambda_n^K
=
\frac12\log n+c+o(1).
\]

Hence

\[
|\lambda_n^K|^2
\asymp
(\log n)^2
\]

at leading scale.

Therefore

\[
\sum_{n\ge1}
|\lambda_n^K|^2
=
\infty.
\]

Thus

\[
\boxed{
\mathrm{RH}
\not\Rightarrow
\Phi\in H^2.
}
\]

The ordinary unweighted Hardy \(H^2\) route is analytically unsuitable.

---

# 5. Radial Parseval identity

For every radius inside the convergence disk,

\[
0<r<1,
\]

Parseval gives

\[
\frac1{2\pi}
\int_0^{2\pi}
|\Phi(re^{i\theta})|^2d\theta
=
\sum_{n\ge1}
|\lambda_n^K|^2r^{2n}.
\]

Under RH, the radial energy still diverges as

\[
r\uparrow1
\]

because the coefficient sequence has logarithmic growth.

If RH fails, an interior transformed zero limits the analytic radius and creates exponential coefficient growth.

Thus the broad radial-energy distinction is another expression of the classical analytic-radius and coefficient-growth mechanism.

No distinct positive zero-orbit energy decomposition is obtained.

---

# 6. Failure to recover single-orbit energy

Phase 5Q showed that for a single symmetric zero orbit,

\[
\mathcal E_b(u,\theta)
=
\sum_n
b_n\Delta_n(u,\theta)^2
\]

can be positive and faithful to horizontal displacement.

The ordinary Keiper–Li generating function contains instead the aggregated coefficients

\[
\lambda_n
=
\sum_j
L_{n,j}.
\]

Parseval applied after aggregation produces quadratic cross terms between distinct zero orbits.

Therefore ordinary coefficient-space energy does not equal the sum of single-orbit horizontal-defect energies.

The Phase 5Q global aggregation obstruction remains.

---

# 7. Prior-art disposition

## Analyticity in the unit disk

PA-4.

Classical Keiper–Li architecture.

## Interior transformed-zero singularities

PA-4.

Classical.

## Exponential asymptotic sensitivity to off-critical zeros

PA-4.

Classical Keiper–Li and Voros asymptotic machinery.

## Ordinary Hardy H2 norm

Rejected as an RH-true state space because the Keiper coefficient sequence is not square summable under the classical RH asymptotic.

## Radially weighted Parseval energy

PA-3 unless a genuinely distinct orbit-separation theorem is proved.

Simple radial weighting measures coefficient growth and analytic radius but does not separate zero-orbit energies before aggregation.

---

# 8. Research redirection

The project abandons the naive one-variable Hardy/Parseval energy route.

The remaining target is a transform that separates or orthogonalizes zero-orbit contributions before quadratic aggregation.

A useful transform must satisfy:

1. analytic accessibility from \(\xi\), \(\xi'/\xi\), or an explicit formula;

2. orbit separation or a positive lower bound for horizontal defect energy;

3. faithfulness to horizontal zero displacement;

4. no presupposed knowledge of individual zero coordinates.

Before constructing such a transform, the project must audit Weil positivity, the Guinand–Weil explicit formula, Bombieri–Lagarias quadratic criteria, de Branges-type Hilbert-space criteria, and Nyman–Beurling/Báez-Duarte \(L^2\) formulations.

---

# 9. Restrictions

No RH proof is obtained.

No new analytic-radius criterion is claimed.

No Hardy-space originality claim is made.

No positive global horizontal-defect energy has been extracted from the ordinary Keiper–Li sequence.

The phrase

"No subsuming source identified in the current audit"

does not apply to the analytic-radius mechanism, which is directly subsumed by classical Keiper–Li prior art.

