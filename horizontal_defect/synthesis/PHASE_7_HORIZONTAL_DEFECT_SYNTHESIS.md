# Phase 7 Horizontal Defect Program Synthesis

## Purpose

This document synthesizes Phase 7A through Phase 7K.

The goal is to state honestly what the horizontal-defect program achieved, what it ruled out, what remains open, and what the next serious research direction should be.

This is not a proof of the Riemann Hypothesis.

This is not a claim of RH progress.

This is an organized research synthesis.

---

# 1. Motivation

The previous zero-counting response project showed that scalar zero-counting data is horizontally blind.

The Riemann Hypothesis is a statement about horizontal zero location:

\[
\Re(\rho)=\frac12.
\]

Therefore any RH-relevant program must interact with the horizontal displacement

\[
\beta-\frac12.
\]

The Phase 7 program redirected the project toward horizontal-defect detection.

---

# 2. Phase 7A — Horizontal information audit

Phase 7A classified objects by whether they are:

1. horizontally blind;
2. horizontally sensitive;
3. positivity-compatible;
4. explicit-formula compatible;
5. computationally testable;
6. potentially RH-relevant.

Main conclusion:

\[
\boxed{
\text{A method that cannot see }\beta-\frac12\text{ cannot prove RH.}
}
\]

Scalar zero-counting objects such as

\[
N(T)
\]

and

\[
E(T)=N(T)-M(T)
\]

are insufficient for RH because they forget horizontal zero location.

---

# 3. Phase 7B — Linear Li-filter obstruction

Phase 7B studied finite linear Li horizontal-defect filters

\[
L(u,\theta)
=
\sum_{n=1}^N
a_n\cos(n\theta)(\cosh(nu)-1).
\]

For small \(u\),

\[
L(u,\theta)
=
\frac{u^2}{2}
\sum_{n=1}^N
a_nn^2\cos(n\theta)
+
O(u^4).
\]

The leading phase factor is a zero-mean cosine polynomial.

Main result:

A nontrivial finite linear Li horizontal-defect filter cannot be a universal positive detector of horizontal displacement at leading order.

Meaning:

Naive finite linear Li-filter positivity attacks are obstructed.

---

# 4. Phase 7C — Quadratic radial Li-coordinate defect

Phase 7C constructed the radial Li-coordinate defect

\[
D_{\mathrm{rad}}(\rho)
=
\left(\log |1-1/\rho|\right)^2.
\]

This satisfies

\[
D_{\mathrm{rad}}(\rho)\ge0
\]

and

\[
D_{\mathrm{rad}}(\rho)=0
\]

if and only if

\[
\Re(\rho)=\frac12.
\]

For

\[
\rho=\frac12+x+i\gamma,
\]

the expansion is

\[
D_{\mathrm{rad}}(\rho)
=
\frac{x^2}{(\gamma^2+\frac14)^2}
+
O(x^4).
\]

Main result:

The radial Li-coordinate defect is a faithful positive single-zero horizontal-displacement detector.

Boundary:

No arithmetic-side or explicit-formula representation was established.

---

# 5. Phase 7D — Aggregation barrier

Phase 7D showed that finite positive aggregation of radial defects is straightforward:

\[
\sum_j
w_j
\left(\log |1-1/\rho_j|\right)^2
\ge0
\]

for positive weights.

The aggregate vanishes if and only if every included zero lies on the critical line.

Main result:

Positive aggregation is easy.

Boundary:

This is mostly tautological unless an arithmetic-side formula forces the aggregate to vanish.

The real problem is not defining a positive defect.

The real problem is connecting it to Weil-positive or explicit-formula-compatible machinery.

---

# 6. Phase 7E — No-go comparison with finite linear filters

Phase 7E proved that the radial defect cannot be uniformly dominated by finite linear Li filters near the critical line.

There is no finite linear filter

\[
L(u,\theta)
=
\sum_{n=1}^{N}
a_n\cos(n\theta)(\cosh(nu)-1)
\]

and constant

\[
c>0
\]

such that

\[
L(u,\theta)\ge cu^2
\]

for all small \(u\ne0\) and all \(\theta\).

Main result:

The bridge from positive radial defect to arithmetic-side control cannot pass through ordinary finite linear Li filters alone.

---

# 7. Phase 7F — Quadratic Li-filter positivity lift

Phase 7F showed that quadratic lifting defeats the phase-sign obstruction.

Define

\[
\Delta_n(u,\theta)
=
\cos(n\theta)(\cosh(nu)-1).
\]

Then

\[
Q_{1,2}(u,\theta)
=
\Delta_1(u,\theta)^2+\Delta_2(u,\theta)^2
\]

is strictly positive for every

\[
u\ne0
\]

and every phase

\[
\theta.
\]

Its small-displacement profile is

\[
Q_{1,2}(u,\theta)
=
\frac{u^4}{4}
\left(
\cos^2\theta+
16\cos^2(2\theta)
\right)
+
O(u^6).
\]

Main result:

Quadratic information can create phase-uniform horizontal detection.

Boundary:

The object is nonlinear and not automatically compatible with classical linear explicit formulae.

---

# 8. Phase 7G — Weil-positive interface audit

Phase 7G audited the possible bridge to classical Weil positivity.

Main conclusion:

The current quadratic detectors are positive and horizontally sensitive, but no Weil-compatible representation has been established.

Three possible bridges were identified:

1. exact Weil representation;
2. comparison with a Weil-positive quadratic form;
3. finite-rank negative-direction detection.

The most accessible path is finite-rank testbed work.

---

# 9. Phase 7H — Centered finite-rank quartet testbed

Phase 7H repaired the toy finite-rank testbed by centering an off-critical quartet against its critical-line collapse.

The centered matrix is

\[
C_m(x,\gamma)
=
\sum_{\epsilon=\pm1}
\sum_{\eta=\pm1}
v_m(\rho_{\epsilon,\eta}(x))v_m(\rho_{\epsilon,\eta}(x))^*
-
2\sum_{\eta=\pm1}
v_m(\rho_{0,\eta})v_m(\rho_{0,\eta})^*.
\]

Main result:

\[
C_m(0,\gamma)=0.
\]

Thus the testbed signal genuinely measures displacement away from the critical-line collapse.

Boundary:

The model is diagnostic and not a classical Weil quadratic form.

---

# 10. Phase 7I — Centered signal scaling law

Phase 7I proved the scaling law

\[
C_m(x,\gamma)
=
x^2B_m(\gamma)+O_{m,\gamma}(x^4).
\]

Thus the centered finite-rank signal is second order in horizontal displacement.

Main result:

The toy finite-rank horizontal signal scales like

\[
x^2.
\]

Boundary:

This is a finite-rank diagnostic theorem, not a Weil theorem.

---

# 11. Phase 7J — Second-order indefiniteness audit

Phase 7J studied the second-order coefficient

\[
B_m(\gamma)
=
\lim_{x\to0}
\frac{C_m(x,\gamma)}{x^2}.
\]

Pure-Python Rayleigh quotient scans showed both positive and negative directions for tested degrees and heights.

Main diagnostic result:

The second-order signal can appear indefinite in finite feature models.

Boundary:

This is diagnostic evidence only.

It is not a theorem of Weil positivity.

---

# 12. Phase 7K — Stability audit

Phase 7K stress-tested the second-order sign behavior across heights, degrees, and feature bases.

Outcome:

Mixed.

Some bases showed both positive and negative directions.

Other bases showed mostly one-sign behavior.

Main conclusion:

\[
\boxed{
\text{The toy finite-rank sign behavior is basis-dependent.}
}
\]

This is an important obstruction.

A genuine RH-relevant construction cannot rely on arbitrary basis-dependent toy behavior.

---

# 13. What Phase 7 achieved

Phase 7 achieved the following:

1. It redirected the project from horizontally blind scalar counting to horizontal zero displacement.
2. It proved finite linear Li-filter positivity obstruction.
3. It constructed a faithful radial Li-coordinate defect.
4. It proved positive aggregation is tautological without arithmetic-side control.
5. It proved finite linear filters cannot dominate the radial defect.
6. It constructed a positive quadratic Li-filter detector.
7. It identified Weil-positive compatibility as the central barrier.
8. It built a centered finite-rank diagnostic testbed.
9. It proved the centered signal scales like \(x^2\).
10. It found basis-dependence in finite-rank sign behavior.

---

# 14. What Phase 7 did not achieve

Phase 7 did not prove RH.

Phase 7 did not prove a new RH criterion.

Phase 7 did not prove a new Weil criterion.

Phase 7 did not connect the radial defect to an arithmetic-side formula.

Phase 7 did not prove basis-independent finite-rank negative-direction detection.

Phase 7 did not establish a canonical Weil-compatible test family.

---

# 15. Honest research status

The strongest honest conclusion is:

\[
\boxed{
\text{Horizontal-defect detection is possible locally, but the arithmetic-side bridge remains open.}
}
\]

The most important obstruction is:

\[
\boxed{
\text{Toy finite-rank behavior is basis-dependent unless a canonical Weil-compatible structure is imposed.}
}
\]

---

# 16. Next serious research direction

The next serious direction is not to add more arbitrary toy bases.

The next serious direction is:

\[
\boxed{
\text{Replace toy feature bases with a classical Weil-compatible test family.}
}
\]

Possible next phase:

**Phase 8A — Classical Weil Criterion Reconstruction**

Goal:

Reconstruct the classical Weil quadratic criterion carefully inside the repo, then identify exactly where off-critical zeros create negative directions.

This should be done as a literature-grounded reconstruction, not as a novelty claim.

