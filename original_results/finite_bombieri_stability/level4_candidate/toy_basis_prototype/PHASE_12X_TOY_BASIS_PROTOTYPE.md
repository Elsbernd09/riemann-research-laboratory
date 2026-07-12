# Phase 12X — Toy Basis Prototype

## Purpose

Phase 12W defined the true arithmetic-entry blueprint.

Phase 12X chooses an explicit toy basis for prototype computation.

This toy basis is compactly supported and easy to evaluate. It is not the final \(C_c^\infty\) theorem-level basis.

---

# 1. Log-coordinate toy basis

Let

\[
u=\log x.
\]

Define a triangular bump centered at \(c\) with width \(w>0\):

\[
\tau_{c,w}(u)=\max\left(0,1-\frac{|u-c|}{w}\right).
\]

Then define the multiplicative basis function:

\[
\phi_{c,w}(x)=\tau_{c,w}(\log x).
\]

Its support is

\[
\operatorname{supp}(\phi_{c,w})\subset[e^{c-w},e^{c+w}].
\]

For a common support window \([-B,B]\) in log-coordinate, choose centers \(c_j\in[-B+w,B-w]\).

---

# 2. Why this basis is useful

The triangular basis is:

1. compactly supported;
2. easy to evaluate;
3. easy to integrate numerically;
4. suitable for testing convolution and interval-matrix infrastructure.

It is only piecewise smooth, not \(C_c^\infty\).

Therefore it is a prototype basis, not the final theoretical basis.

---

# 3. Star operation

For a basis function

\[
\phi(x),
\]

the star is

\[
\phi^*(x)=x^{-1}\overline{\phi(1/x)}.
\]

For real-valued toy basis functions,

\[
\phi^*(x)=x^{-1}\phi(1/x).
\]

---

# 4. Multiplicative convolution

For two toy basis functions,

\[
F_{ij}(x)=\phi_j*\phi_i^*(x)
=
\int_0^\infty \phi_j(y)\phi_i^*(x/y)\frac{dy}{y}.
\]

In log coordinates \(y=e^v\), this becomes

\[
F_{ij}(e^u)
=
\int_{-\infty}^{\infty}
\phi_j(e^v)
\phi_i^*(e^{u-v})
\,dv.
\]

This is numerically tractable because both factors have compact support.

---

# 5. Prototype theorem

The toy basis satisfies the compact-support requirements of Phases 12Q and 12W.

Thus the finite prime-sum cutoff and reduced archimedean blueprint apply.

---

# Theorem 12X.1 — Toy basis compact support

Let

\[
\phi_{c,w}(x)=\max\left(0,1-\frac{|\log x-c|}{w}\right).
\]

Then

\[
\operatorname{supp}(\phi_{c,w})
\subset[e^{c-w},e^{c+w}].
\]

## Proof

The triangular bump is nonzero only when

\[
|\log x-c|<w.
\]

This is equivalent to

\[
c-w<\log x<c+w.
\]

Exponentiating gives

\[
e^{c-w}<x<e^{c+w}.
\]

Thus the support lies in

\[
[e^{c-w},e^{c+w}].
\]

\[
\square
\]

---

# 6. Implementation goal

The implementation provides:

1. triangular bump evaluator;
2. multiplicative basis evaluator;
3. star evaluator;
4. numerical convolution evaluator;
5. finite grid diagnostic;
6. toy-basis metadata certificate.

The output is not a certified arithmetic entry yet.

It is the concrete basis foundation for Phase 12Y.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not prove the full Weil positivity theorem.

This phase does not prove a complete arithmetic-only finite certificate.

This phase does not establish novelty.

Exact audit strings:

TOY_BASIS_PROTOTYPE_COMPLETE

TRIANGULAR_LOG_BUMP_DEFINED

MULTIPLICATIVE_TOY_BASIS_DEFINED

TOY_BASIS_COMPACT_SUPPORT_PROVED

STAR_EVALUATOR_IMPLEMENTED

CONVOLUTION_EVALUATOR_IMPLEMENTED

TOY_BASIS_ONLY_NOT_FINAL_C_C_INFINITY_BASIS

TRUE_CERTIFIED_ARITHMETIC_ENTRY_NOT_YET_COMPUTED

LEVEL4_READY_FOR_TOY_ENTRY_PROTOTYPE

