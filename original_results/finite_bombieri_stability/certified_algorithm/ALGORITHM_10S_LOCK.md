# Algorithm 10S Lock

## Algorithm name

Weighted Support Stability Certification

## Verdicts

The algorithm returns exactly one of:

\[
\texttt{CERTIFIED\_STABLE}
\]

or

\[
\texttt{NOT\_CERTIFIED}.
\]

---

# Computed quantity

\[
\mathcal R
=
L_t(U)
\left(
\sum_{j,k}m_jm_k(d_j+d_k)^2
\right)^{1/2}.
\]

---

# Certification rule

If

\[
\mathcal R<g_0(M),
\]

return:

\[
\texttt{CERTIFIED\_STABLE}.
\]

Otherwise return:

\[
\texttt{NOT\_CERTIFIED}.
\]

---

# Meaning

CERTIFIED_STABLE means Theorem 10Q proves negative-count stability.

NOT_CERTIFIED means the theorem does not certify stability.

NOT_CERTIFIED does not mean instability.

---

# Boundary

This algorithm does not prove RH.

This algorithm does not falsify RH.

This algorithm does not use zeta zeros.

This algorithm does not claim novelty.

