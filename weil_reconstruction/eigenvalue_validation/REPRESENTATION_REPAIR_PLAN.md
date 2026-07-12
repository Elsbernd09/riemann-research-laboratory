# Representation Repair Plan

## Trigger

Use this repair plan only if Phase 9D reports:

\[
\texttt{NEXT\_TRACK=REPRESENTATION\_REPAIR\_REQUIRED}.
\]

---

# 1. Inspect Hermitian residuals

For each synthetic case, compare residuals for:

1. full raw matrix;
2. distinct weighted matrix;
3. similarity-symmetrized candidate.

The selected representation must pass the Hermitian gate before eigenvalues are trusted.

---

# 2. Re-check source normalization

Re-check:

\[
K(x)=\frac{\sin x}{x},
\]

\[
K_t(x)=K(tx),
\]

\[
K^*(x,y;t),
\]

\[
H(x,y;t)=\frac{2tK^*(x,y;t)}{1/4+y^2}.
\]

Any ambiguity in the source formula must be recorded as a source-extraction issue.

---

# 3. Re-check multiplicity handling

Repeated \(\gamma\)-values create zero eigenvalues.

The distinct weighted matrix uses column weights:

\[
H(\gamma_j,\gamma_k;t)m(\gamma_k).
\]

The similarity candidate uses:

\[
\sqrt{m(\gamma_j)}H(\gamma_j,\gamma_k;t)\sqrt{m(\gamma_k)}.
\]

This must be audited before final validation.

---

# 4. No zeta zeros

Do not use zeta zeros during repair.

Synthetic finite multisets only.

