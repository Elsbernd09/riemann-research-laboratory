# Phase 8V — Bombieri Theorem 8 Extraction

## Purpose

Phase 8U source-extracted the formula-level \(H(\gamma,\gamma';t)\) kernel.

Phase 8V source-extracts Bombieri Theorem 8 at statement level and records the nearby zero-eigenvalue multiplicity convention from Lemma 10.

This phase does not implement the matrix.

This phase does not compute eigenvalues.

This phase does not prove RH.

This phase does not claim novelty.

---

# 1. Source

Enrico Bombieri, **Remarks on Weil's quadratic functional in the theory of prime numbers, I**, Section 8.

Relevant source region:

Section 8, around Lemma 10 and Theorem 8.

---

# 2. Lemma 10 source extraction

Bombieri records that the spectrum of

\[
H(\Gamma;t)
\]

contains zero eigenvalues arising from repeated elements of \(\Gamma\).

If \(m(\gamma)\) is the multiplicity of a distinct element \(\gamma\), the zero-eigenvalue contribution is

\[
\sum_{\gamma}'(m(\gamma)-1),
\]

where the prime indicates summation over distinct \(\gamma\)-values.

The remaining nonzero spectrum is represented by the distinct-\(\gamma\) matrix with multiplicity weights on the columns:

\[
H(\gamma_j,\gamma_k;t)m(\gamma_k).
\]

This is the source-level multiplicity warning.

---

# 3. Theorem 8 source extraction

Bombieri states:

\[
\boxed{
\text{The number of negative eigenvalues of }H(\Gamma;t)
\text{ equals the number of distinct complex conjugate pairs }
(\gamma,\overline{\gamma})\text{ in }\Gamma.
}
\]

This is the central finite-dimensional negative-eigenvalue count theorem for the first eigenvalue problem.

---

# 4. Interpretation

Theorem 8 says that the finite matrix detects non-real \(\gamma\)-pairs.

Since

\[
\rho=\frac12+i\gamma,
\]

a non-real \(\gamma\) corresponds to

\[
\gamma=a+ib,\qquad b\ne0,
\]

and therefore

\[
\rho=\frac12+i(a+ib)=\frac12-b+ia,
\]

which is horizontally displaced from the critical line.

Thus Bombieri's finite theorem connects:

\[
\text{off-critical zero geometry}
\]

to

\[
\text{negative eigenvalues of the finite approximation matrix}.
\]

This is the classical version of the horizontal-defect theme.

---

# 5. Important distinction

Theorem 8 is finite-dimensional and source-classical.

It does not by itself prove RH.

It does not by itself settle the infinite zeta case.

Bombieri's later Sections 10 and 11 handle the limiting transition to the zeta-function case, including the possibility that negative eigenvalues tend to zero and produce linear dependence relations.

Therefore, even after Theorem 8 is extracted, the project must not claim an RH proof.

---

# 6. Current lock status

## LOCKED

1. Section 8 finite skeleton;
2. \(H\)-kernel formula at source-note level;
3. coefficient equation skeleton;
4. zero-eigenvalue multiplicity warning from Lemma 10;
5. Theorem 8 negative-eigenvalue count statement.

## PARTIAL

1. exact implementation normalization;
2. numerical stability convention;
3. handling repeated \(\gamma\)-values in code;
4. precise real-matrix conversion;
5. Section 10 limiting transition to zeta.

## STILL BLOCKED

1. production matrix implementation;
2. eigenvalue experiments presented as Bombieri-Weil computations;
3. zeta-limit conclusions;
4. RH claims.

---

# 7. Boundary

Known source theorem reconstructed.

No project novelty.

No matrix implementation.

No eigenvalue computation.

No RH proof.

No novelty claim.

