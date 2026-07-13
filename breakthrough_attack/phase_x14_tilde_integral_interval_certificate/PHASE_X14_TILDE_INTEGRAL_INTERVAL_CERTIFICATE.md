# Phase X14 — Tilde Integral Interval Certificate

## Purpose

Phase X13 created a partial interval certificate for:

\[
\int F(x)\,dx.
\]

Phase X14 creates the matching partial interval certificate for:

\[
\int \widetilde F(x)\,dx,
\qquad
\widetilde F(x)=x^{-1}F(1/x).
\]

This is still not a full certified arithmetic entry.

---

# 1. Tilde support

If:

\[
\operatorname{supp}(F)\subset[A,B],
\]

then:

\[
\operatorname{supp}(\widetilde F)\subset[B^{-1},A^{-1}].
\]

This follows because:

\[
\widetilde F(x)=x^{-1}F(1/x)
\]

is nonzero only when:

\[
1/x\in[A,B].
\]

---

# 2. Tilde integral certificate

Apply midpoint quadrature to:

\[
\widetilde F(x)
\]

on:

\[
[B^{-1},A^{-1}].
\]

Using a candidate derivative bound \(B_2^{\sim}\), the X6 theorem gives:

\[
\int_{B^{-1}}^{A^{-1}}\widetilde F(x)\,dx
\in
\left[
Q_N(\widetilde F)-E_{\sim},
Q_N(\widetilde F)+E_{\sim}
\right],
\]

where:

\[
E_{\sim}=\frac{(A^{-1}-B^{-1})^3B_2^{\sim}}{24N^2}.
\]

---

# 3. Honest certification status

This phase creates the tilde integral certificate pattern.

However, the derivative bound for \(\widetilde F\) is transferred conservatively from the existing \(F''\)-bound machinery and still inherits incomplete coefficient certification.

Therefore the status is:

\[
\boxed{
\texttt{TILDE\_INTEGRAL\_INTERVAL\_CERTIFICATE\_COEFFICIENTS\_NOT\_CERTIFIED}
}
\]

---

# Theorem X14.1 — tilde support theorem

If:

\[
\operatorname{supp}(F)\subset[A,B],
\]

then:

\[
\operatorname{supp}(\widetilde F)\subset[B^{-1},A^{-1}].
\]

## Proof

\[
\widetilde F(x)=x^{-1}F(1/x).
\]

The factor \(x^{-1}\) does not affect support for \(x>0\).

Thus \(\widetilde F(x)\neq0\) only when:

\[
F(1/x)\neq0.
\]

This requires:

\[
1/x\in[A,B].
\]

Equivalently:

\[
x\in[B^{-1},A^{-1}].
\]

\[
\square
\]

---

# Theorem X14.2 — tilde integral partial certificate

Assume:

\[
\operatorname{supp}(\widetilde F)\subset[a,b],
\]

and:

\[
\|(\widetilde F)''\|_\infty\le B_2^{\sim}.
\]

Then midpoint quadrature gives:

\[
\int_a^b\widetilde F(x)\,dx
\in
\left[
Q_N(\widetilde F)-\frac{(b-a)^3B_2^{\sim}}{24N^2},
Q_N(\widetilde F)+\frac{(b-a)^3B_2^{\sim}}{24N^2}
\right].
\]

## Proof

Apply the X6 midpoint quadrature theorem to \(h=\widetilde F\).

\[
\square
\]

---

# 4. What remains for full \(M_{00}\)

After X13 and X14, the central and tilde integral certificate patterns exist.

The full entry still needs:

1. finite prime-side certificate;
2. constant-term certificate;
3. archimedean continuous-extension certificate;
4. coefficient-solve certificate;
5. outward-rounded arithmetic review.

---

# Boundary

This phase does not prove RH.

This phase does not prove a breakthrough.

This phase does not establish novelty.

This phase does not compute a fully certified arithmetic entry.

It creates the tilde integral interval certificate pattern.

Exact audit strings:

PHASE_X14_TILDE_INTEGRAL_INTERVAL_CERTIFICATE_COMPLETE

TILDE_SUPPORT_THEOREM_PROVED

TILDE_INTEGRAL_INTERVAL_CERTIFICATE_CREATED

MIDPOINT_QUADRATURE_THEOREM_APPLIED_TO_TILDE_F

TILDE_DERIVATIVE_BOUND_USED

TILDE_INTEGRAL_CERTIFICATE_COEFFICIENTS_NOT_CERTIFIED

FULL_T_BL_ENTRY_NOT_CERTIFIED

CERTIFIED_ARITHMETIC_ENTRY_NOT_COMPUTED

READY_FOR_PHASE_X15_PRIME_SIDE_INTERVAL_CERTIFICATE

