# Phase B13 — Smooth Basis Certification Plan

## Purpose

Phase B12 showed that the triangular toy basis blocks true Weil-test certification because it is not \(C_c^\infty\).

Phase B13 replaces the toy basis direction with a smooth compactly supported basis plan.

This phase is still a plan and prototype.

It does not compute a certified arithmetic entry.

---

# 1. Smooth bump

Define:

\[
\psi(u)=
\begin{cases}
\exp\left(-\frac1{1-u^2}\right), & |u|<1,\\
0, & |u|\ge1.
\end{cases}
\]

This is the standard smooth compactly supported bump.

It satisfies:

\[
\psi\in C_c^\infty(\mathbb R).
\]

Its support is:

\[
[-1,1].
\]

---

# 2. Log-coordinate basis function

Define:

\[
\phi_{c,w}(x)=\psi\left(\frac{\log x-c}{w}\right),
\qquad w>0.
\]

Then:

\[
\operatorname{supp}(\phi_{c,w})
=
[e^{c-w},e^{c+w}].
\]

Thus:

\[
\phi_{c,w}\in C_c^\infty(0,\infty).
\]

---

# 3. Star/involution support

Using the project star convention:

\[
\phi^*(x)=x^{-1}\phi(1/x).
\]

If

\[
\operatorname{supp}(\phi)\subset[e^{c-w},e^{c+w}],
\]

then

\[
\operatorname{supp}(\phi^*)\subset[e^{-c-w},e^{-c+w}].
\]

The extra factor \(x^{-1}\) changes values but not support.

---

# 4. Convolution support

For multiplicative convolution:

\[
F=\phi*\phi^*,
\]

support multiplies:

\[
\operatorname{supp}(F)
\subset
[e^{c-w}e^{-c-w},e^{c+w}e^{-c+w}]
=
[e^{-2w},e^{2w}].
\]

This is crucial because it gives a finite prime cutoff:

\[
n\le e^{2w}.
\]

---

# Theorem B13.1 — smooth log-bump belongs to \(C_c^\infty(0,\infty)\)

Let

\[
\psi(u)=
\begin{cases}
\exp(-1/(1-u^2)), & |u|<1,\\
0, & |u|\ge1.
\end{cases}
\]

and

\[
\phi_{c,w}(x)=\psi((\log x-c)/w)
\]

with \(w>0\).

Then:

\[
\phi_{c,w}\in C_c^\infty(0,\infty).
\]

## Proof

The function \(\psi\) is the standard smooth bump on \(\mathbb R\), with compact support \([-1,1]\).

The map

\[
x\mapsto (\log x-c)/w
\]

is smooth on \((0,\infty)\).

The composition of smooth functions is smooth.

The support condition

\[
|(\log x-c)/w|\le1
\]

is equivalent to:

\[
c-w\le \log x\le c+w,
\]

or:

\[
e^{c-w}\le x\le e^{c+w}.
\]

Thus the support is compact in \((0,\infty)\).

Therefore:

\[
\phi_{c,w}\in C_c^\infty(0,\infty).
\]

\[
\square
\]

---

# Theorem B13.2 — convolution support bound

If

\[
\operatorname{supp}(\phi_{c,w})\subset[e^{c-w},e^{c+w}],
\]

then

\[
\operatorname{supp}(\phi_{c,w}*\phi_{c,w}^*)
\subset[e^{-2w},e^{2w}].
\]

## Proof

The star support is:

\[
\operatorname{supp}(\phi^*)\subset[e^{-c-w},e^{-c+w}].
\]

Multiplicative convolution support lies in the product of supports.

Therefore:

\[
\operatorname{supp}(\phi*\phi^*)
\subset
[e^{c-w}e^{-c-w},e^{c+w}e^{-c+w}]
=
[e^{-2w},e^{2w}].
\]

\[
\square
\]

---

# 5. Certification plan

To turn this into a certified arithmetic entry, future phases need:

1. interval evaluation of \(\psi\);
2. interval evaluation of \(\phi_{c,w}\);
3. interval evaluation of \(\phi^*\);
4. interval enclosure of convolution \(F\);
5. singularity-subtracted archimedean integral;
6. interval quadrature;
7. pole-constraint validation;
8. source-normalization validation.

---

# 6. Breakthrough relevance

This phase fixes a real blocker.

It moves the project from a toy non-smooth basis toward a legitimate \(C_c^\infty\) test-function family.

However, it still does not certify an entry.

Therefore:

\[
\boxed{\text{BREAKTHROUGH\_NOT\_ACHIEVED}}
\]

---

# 7. Next phase

Phase B14 should implement the smooth basis object and run basic support/audit tests.

The target is not certified integration yet.

The target is:

\[
\boxed{
\text{smooth basis object + support certificate}
}
\]

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a breakthrough.

This phase does not prove novelty.

This phase does not compute a certified arithmetic entry.

Exact audit strings:

PHASE_B13_SMOOTH_BASIS_CERTIFICATION_PLAN_COMPLETE

SMOOTH_BUMP_DEFINED

LOG_SMOOTH_BASIS_DEFINED

SMOOTH_BASIS_IN_CC_INFINITY_PROVED

STAR_SUPPORT_BOUND_PROVED

CONVOLUTION_SUPPORT_BOUND_PROVED

FINITE_PRIME_CUTOFF_FROM_SUPPORT_IDENTIFIED

TRIANGULAR_TOY_BASIS_REPLACEMENT_PLAN_CREATED

BREAKTHROUGH_NOT_ACHIEVED

READY_FOR_PHASE_B14_SMOOTH_BASIS_IMPLEMENTATION

