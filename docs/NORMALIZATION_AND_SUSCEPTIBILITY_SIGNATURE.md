# Normalization and the Susceptibility Signature

## Phase 0D

This document records the analysis of normalization dependence in cross-diagnostic zero-surgery response.

---

# 1. Problem

For a diagnostic kernel \(f\), define

\[
\mathcal R_f(\delta,\gamma)
=
\sum_{\epsilon=\pm1}
\sum_{\eta=\pm1}
f\left(
\frac12+\epsilon\delta+i\eta\gamma
\right)
-
2
\sum_{\eta=\pm1}
f\left(
\frac12+i\eta\gamma
\right).
\]

When \(f\) is analytic near the baseline pair,

\[
\mathcal R_f(\delta,\gamma)
=
\delta^2\chi_f(\gamma)
+
O(\delta^4),
\]

where

\[
\chi_f(\gamma)
=
f''\left(\frac12+i\gamma\right)
+
f''\left(\frac12-i\gamma\right).
\]

For conjugation-compatible \(f\),

\[
\chi_f(\gamma)
=
2\Re
f''\left(\frac12+i\gamma\right).
\]

Raw values of \(\chi_f\) cannot automatically be compared across unrelated diagnostic families because the native scale and normalization of the kernels may differ.

---

# 2. Rejected universal normalization: baseline-value normalization

Define

\[
B_f(\gamma)
=
f\left(\frac12+i\gamma\right)
+
f\left(\frac12-i\gamma\right).
\]

The candidate normalization

\[
\frac{\chi_f}{|B_f|}
\]

is rejected as a universal metric.

Reason:

\[
B_f
\]

may vanish or become arbitrarily small because of cancellation.

A near-zero denominator can create a spurious sensitivity singularity.

The ratio may still be recorded as a diagnostic-specific secondary observable.

---

# 3. Rejected intrinsic normalization: absolute pair magnitude

Define

\[
A_f(\gamma)
=
\left|
f\left(\frac12+i\gamma\right)
\right|
+
\left|
f\left(\frac12-i\gamma\right)
\right|.
\]

The candidate normalization

\[
\frac{|\chi_f|}{A_f}
\]

avoids pair cancellation.

However, under an additive kernel shift

\[
f\mapsto f+C,
\]

the susceptibility is unchanged because

\[
(f+C)''
=
f'',
\]

while \(A_f\) changes.

Therefore this ratio is not intrinsic to the perturbative response unless an additive normalization of \(f\) has been canonically fixed.

It is rejected as a universal metric.

---

# 4. Orientation coefficient

For

\[
\rho=\frac12+i\gamma
\]

and \(f''(\rho)\ne0\), define

\[
\Omega_f(\gamma)
=
\frac{
|\Re f''(\rho)|
}{
|f''(\rho)|
}.
\]

Then

\[
0\le\Omega_f(\gamma)\le1.
\]

Interpretation:

- values near 1 indicate that the complex second derivative projects strongly onto the symmetric horizontal response channel;
- values near 0 indicate that most second-derivative curvature is invisible to that response channel.

If \(f''(\rho)=0\), the orientation coefficient is undefined and must not be silently assigned a numerical value.

The orientation coefficient measures directional alignment, not response magnitude.

---

# 5. Local shape invariant

For \(f'(\rho)\ne0\), define

\[
\mathcal K_f(\rho)
=
\frac{
f(\rho)f''(\rho)
}{
(f'(\rho))^2
}.
\]

Under constant nonzero multiplicative rescaling

\[
f\mapsto cf,
\]

one has

\[
\mathcal K_{cf}
=
\mathcal K_f.
\]

Thus \(\mathcal K_f\) removes arbitrary constant multiplicative scale.

It is not invariant under additive shifts

\[
f\mapsto f+C.
\]

The kernel convention must therefore be derived from the standard mathematical definition of each diagnostic family.

---

# 6. Logarithmic curvature

For \(f(\rho)\ne0\), define

\[
\mathcal C_f(\rho)
=
\frac{f''(\rho)}{f(\rho)}
-
\left(
\frac{f'(\rho)}{f(\rho)}
\right)^2.
\]

Where a local logarithm is defined,

\[
\mathcal C_f(\rho)
=
(\log f)''(\rho).
\]

The quotient expression is the preferred computational definition because it avoids unnecessary global branch choices.

Under constant nonzero multiplicative rescaling,

\[
f\mapsto cf,
\]

one has

\[
\mathcal C_{cf}
=
\mathcal C_f.
\]

This quantity measures logarithmic curvature rather than the original raw signed-response susceptibility.

The two must not be conflated.

---

# 7. Susceptibility signature

The project will not currently force all diagnostic sensitivity into one universal scalar.

For each admissible kernel \(f\), define the susceptibility signature

\[
\Sigma_f(\gamma)
=
\left(
\chi_f(\gamma),
\Omega_f(\gamma),
\mathcal K_f(\rho),
\mathcal C_f(\rho)
\right),
\]

where

\[
\rho=\frac12+i\gamma.
\]

The signature separates four notions:

## Native quadratic response

\[
\chi_f.
\]

## Horizontal response orientation

\[
\Omega_f.
\]

## Local derivative-shape geometry

\[
\mathcal K_f.
\]

## Multiplicative-scale-invariant logarithmic curvature

\[
\mathcal C_f.
\]

The full finite-displacement response

\[
\mathcal R_f(\delta,\gamma)
\]

must also be retained.

---

# 8. Detection threshold suspended

The provisional detection scale

\[
n_*(\delta,\gamma;\tau)
=
\inf
\left\{
n:
|\mathcal R_{f_n}(\delta,\gamma)|
\ge\tau
\right\}
\]

is suspended as a cross-diagnostic metric.

Reason:

an absolute threshold \(\tau\) is generally dependent on diagnostic normalization.

A detection threshold may be reintroduced only after a family-specific normalization or statistically and mathematically justified comparison scale is derived.

---

# 9. Current research question

The initial question

"Which RH diagnostic detects a hypothetical off-line zero first?"

is underspecified.

The revised question is:

> How do explicitly defined RH-related zero kernels differ in native quadratic response, horizontal response orientation, local derivative-shape geometry, and multiplicative-scale-invariant logarithmic curvature under signed symmetry-breaking perturbation?

A secondary question is:

> Do different notions of sensitivity induce substantially different orderings of diagnostic families?

---

# 10. Current claim status

No originality claim is made.

The derivative identities and scaling calculations are elementary.

The susceptibility-signature formalism is project methodology until prior-art investigation and diagnostic-specific analysis establish whether it captures a useful mathematical phenomenon.
