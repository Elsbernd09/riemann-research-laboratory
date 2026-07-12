# Phase 12E — Provisional Import of \(F_g=g*g^*\) and \(Q_W(g)=T[g*g^*]\)

## Purpose

Phase 12C blocked the Level 4 candidate branch because the exact classical construction \(F_g\) was missing.

The user then supplied a source-summary text stating the Weil/Bombieri positivity construction:

\[
F_g=g*g^*,
\]

where

\[
g^*(x)=\frac{1}{x}\overline{g(1/x)}
\]

and \(*\) is multiplicative convolution with Haar measure \(dy/y\).

Phase 12E provisionally imports this object.

---

# 1. Provisional source status

This import is not yet a final primary-source import.

The supplied text appears to be a summary of Weil/Bombieri positivity rather than a primary source such as Weil, Bombieri, or a peer-reviewed theorem statement.

Therefore this phase marks the import as:

\[
\boxed{\text{PROVISIONAL SOURCE IMPORT}}
\]

not:

\[
\boxed{\text{FINAL PRIMARY-SOURCE IMPORT}}.
\]

---

# 2. Imported involution

For a complex-valued test function \(g\), define

\[
g^*(x)=\frac{1}{x}\overline{g(1/x)}.
\]

This involution encodes the \(s\mapsto1-s\) symmetry of the zeta functional equation under the Mellin transform.

---

# 3. Imported multiplicative convolution

For suitable functions \(a,b\) on \((0,\infty)\), define multiplicative convolution by

\[
(a*b)(x)=\int_0^\infty a(y)b(x/y)\frac{dy}{y}.
\]

Therefore,

\[
F_g(x)=(g*g^*)(x)
=
\int_0^\infty g(y)g^*(x/y)\frac{dy}{y}.
\]

Substituting the definition of \(g^*\), this becomes

\[
F_g(x)
=
\int_0^\infty
g(y)
\frac{y}{x}
\overline{g(y/x)}
\frac{dy}{y}.
\]

Equivalently,

\[
F_g(x)
=
\frac{1}{x}
\int_0^\infty
g(y)\overline{g(y/x)}\,dy.
\]

Some source summaries write closely related normalizations. The exact normalization must still be checked against the primary source.

---

# 4. Provisional Weil quadratic form

Using the Bombieri explicit formula functional \(T\), define provisionally:

\[
Q_W(g)=T[F_g]=T[g*g^*].
\]

This is the provisional quadratic Weil positivity form.

---

# 5. Provisional positivity criterion

The supplied source-summary text states the Weil/Bombieri positivity criterion in the form:

\[
\mathrm{RH}
\Longleftrightarrow
T[g*g^*]\ge0
\]

for all admissible nonzero \(g\).

This phase records the criterion as provisional:

\[
\boxed{
\mathrm{RH}
\Longleftrightarrow
Q_W(g)\ge0
\quad
\forall g\in\mathcal D_W
}
\]

where

\[
Q_W(g)=T[g*g^*].
\]

---

# 6. Mellin transform check

Let

\[
\widehat g(s)=\int_0^\infty g(x)x^{s-1}\,dx.
\]

The supplied source-summary text states the involution identity:

\[
\widehat{g^*}(s)
=
\overline{\widehat g(1-\bar s)}.
\]

Therefore, by the Mellin convolution theorem,

\[
\widehat{F_g}(s)
=
\widehat{g*g^*}(s)
=
\widehat g(s)\overline{\widehat g(1-\bar s)}.
\]

If \(\rho\) lies on the critical line, then

\[
1-\bar\rho=\rho,
\]

so

\[
\widehat{F_g}(\rho)
=
|\widehat g(\rho)|^2.
\]

This explains why positivity is tied to RH.

---

# 7. Remaining unresolved points

The import is mathematically useful but not final.

The following must still be primary-source confirmed:

1. exact normalization of \(g^*\);
2. exact multiplicative Haar measure convention;
3. exact sign convention for \(Q_W\);
4. exact admissible domain \(\mathcal D_W\);
5. exact theorem statement;
6. whether \(T[g*g^*]\) or \(-T[g*g^*]\) is the positivity form under the project’s \(T\)-normalization;
7. compatibility with the previously extracted Bombieri \(T[f]\).

---

# 8. What this unlocks

The project can now provisionally proceed to define:

\[
Q_W(g)=T[g*g^*].
\]

This allows the next phase to attempt an internal consistency check between:

1. the project’s extracted \(T[f]\);
2. the provisional \(F_g=g*g^*\);
3. the Mellin identity;
4. the spectral positivity expression.

---

# 9. Next target

Phase 12F should prove the formal Mellin identities:

\[
\widehat{g^*}(s)=\overline{\widehat g(1-\bar s)}
\]

and

\[
\widehat{g*g^*}(s)
=
\widehat g(s)\overline{\widehat g(1-\bar s)}.
\]

This would be a real theorem from the imported objects.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not prove Level 4 contribution.

This phase does not use a primary mathematical source.

This phase does not fully resolve the sign convention.

This phase does not establish novelty.

Exact audit strings:

PROVISIONAL_F_G_IMPORT

F_G_EQUALS_G_CONVOLVE_G_STAR

G_STAR_INVOLUTION_IMPORTED

MULTIPLICATIVE_CONVOLUTION_IMPORTED

PROVISIONAL_Q_W_DEFINED

Q_W_EQUALS_T_OF_G_CONVOLVE_G_STAR

MELLIN_PRODUCT_TARGET_IDENTIFIED

PRIMARY_SOURCE_CONFIRMATION_STILL_REQUIRED

SIGN_CONVENTION_STILL_UNCONFIRMED

LEVEL4_BREAKTHROUGH_CANDIDATE_NOT_YET_ACHIEVED

