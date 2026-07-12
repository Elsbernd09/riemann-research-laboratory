# Theorem 8 Extraction Template

## Source

Bombieri, Section 8.

## Exact theorem statement

The number of negative eigenvalues of the matrix

\[
H(\Gamma;t)
\]

equals the number of distinct complex conjugate pairs

\[
(\gamma,\overline{\gamma})
\]

in \(\Gamma\).

Status: LOCKED at statement level.

## Hypotheses

Source context:

1. \(\Gamma\) is obtained from a finite multiset \(Z\) with zeta-zero-like symmetries.
2. Elements are counted with multiplicity.
3. \(\rho=1/2+i\gamma\).
4. \(\Gamma\) is invariant under complex conjugation and multiplication by \(-1\).
5. The finite approximation matrix is \(H(\Gamma;t)\).

Status: PARTIAL.

## Objects used

- \(Z\): finite multiset of source points.
- \(\Gamma\): finite multiset of \(\gamma\)-values.
- \(t\): interval half-width.
- \(V\): finite-dimensional span from Section 8.
- \(V^\circ\): boundary subspace satisfying \(F(-t)=F(t)=0\).
- \(L\): source-extracted linear object.
- \(H(\gamma,\gamma';t)\): Section 8 matrix kernel.

## Matrix/eigenvalue statement

Negative eigenvalue count:

\[
\#\{\lambda<0:\lambda\in\operatorname{Spec}(H(\Gamma;t))\}
=
\#\{\text{distinct complex conjugate pairs }(\gamma,\overline{\gamma})\subset\Gamma\}.
\]

Status: LOCKED at statement level.

## Zero eigenvalue statement

Repeated elements of \(\Gamma\) create zero eigenvalue multiplicity

\[
\sum_{\gamma}'(m(\gamma)-1).
\]

Status: LOCKED at statement level.

## Odd/even distinction

Not the main object of Theorem 8 extraction here.

Further odd/even refinements belong to later Section 8/9 extraction.

Status: PARTIAL.

## Relationship to off-critical zeros

If \(\gamma\) is non-real, then

\[
\rho=\frac12+i\gamma
\]

has real part different from \(1/2\).

Thus non-real \(\gamma\)-pairs correspond to off-critical geometry.

Status: LOCKED conceptually.

## Boundary

Known source theorem.

No novelty claim.

No RH proof.

No implementation yet.

