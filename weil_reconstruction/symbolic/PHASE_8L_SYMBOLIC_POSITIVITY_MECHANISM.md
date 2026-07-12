# Phase 8L — Symbolic Positivity Mechanism Note

## Purpose

Phase 8K source-locked the distinction between:

\[
f^*_{\mathrm{alg}}(x)=x^{-1}f(1/x)
\]

and the Hermitian positivity adjoint

\[
g^*_{\mathrm{pos}}(x)=x^{-1}\overline{g(1/x)}.
\]

Phase 8L records the symbolic positivity mechanism behind Bombieri Theorem 1.

This is not a proof of RH.

This is not a new Weil criterion.

This is a reconstruction note explaining why the zero-side quadratic expression is nonnegative if RH holds.

---

# 1. Hermitian positivity convention

For complex-valued \(g\), use the positivity adjoint

\[
g^*_{\mathrm{pos}}(x)
=
x^{-1}\overline{g(1/x)}.
\]

Its Mellin transform satisfies

\[
g^*_{\mathrm{pos}}(s)
=
\overline{g(1-\overline{s})}.
\]

Define

\[
F=g*g^*_{\mathrm{pos}}.
\]

Then

\[
F(s)
=
g(s)\overline{g(1-\overline{s})}.
\]

---

# 2. Evaluation at a zero

Let

\[
\rho=\beta+i\gamma
\]

be a nontrivial zero.

Then

\[
F(\rho)
=
g(\rho)\overline{g(1-\overline{\rho})}.
\]

This expression depends on the horizontal location of \(\rho\).

---

# 3. What RH does

If RH holds, then

\[
\beta=\frac12.
\]

Therefore

\[
\rho=\frac12+i\gamma
\]

and

\[
1-\overline{\rho}
=
1-\left(\frac12-i\gamma\right)
=
\frac12+i\gamma
=
\rho.
\]

Hence

\[
F(\rho)
=
g(\rho)\overline{g(\rho)}
=
|g(\rho)|^2.
\]

Therefore the zero-side expression becomes

\[
\sum_\rho |g(\rho)|^2.
\]

This is nonnegative.

---

# 4. Positivity mechanism

The symbolic mechanism is:

\[
\boxed{
\text{RH turns the reflected-conjugate evaluation point }1-\overline{\rho}\text{ into }\rho.
}
\]

That converts a paired product into a square norm.

This is the core positivity mechanism.

---

# 5. Why this matters for Phase 7

Phase 7 tried to detect horizontal displacement

\[
\beta-\frac12.
\]

The Bombieri-Weil mechanism sees the same issue differently.

If

\[
\beta\ne\frac12,
\]

then

\[
1-\overline{\rho}\ne\rho.
\]

Therefore

\[
g(\rho)\overline{g(1-\overline{\rho})}
\]

is not automatically a square norm.

That is where off-critical zeros can break positivity.

---

# 6. What this note proves

This note proves only the elementary symbolic implication:

If RH holds, then the Hermitian zero-side product becomes a sum of squared absolute values.

It does not prove the converse.

The converse is part of the classical Bombieri/Weil theorem.

The project records that theorem as known source material, not as a project-original proof.

---

# 7. Implementation status

Symbolic positivity reasoning using the Hermitian star is allowed.

Exact finite-rank Weil matrix implementation remains blocked until the finite truncation model and matrix entries are source-extracted.

---

# 8. Boundary

No RH proof.

No new Weil criterion.

No novelty claim.

No finite-rank Weil matrix yet.

