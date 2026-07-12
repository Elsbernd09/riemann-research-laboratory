# Algorithm 10W Lock

## Name

Combined-Radius Stability Certification

## Radii

\[
\mathcal R_F
=
L_t(U)
\left(
\sum_{j,k}m_jm_k(d_j+d_k)^2
\right)^{1/2}.
\]

\[
\mathcal R_{\mathrm{row}}
=
\max_j
\sum_k
\sqrt{m_jm_k}L_t(U)(d_j+d_k).
\]

\[
\mathcal R_{\min}
=
\min\{\mathcal R_F,\mathcal R_{\mathrm{row}}\}.
\]

## Verdict rule

If

\[
\mathcal R_{\min}<g_0(M),
\]

return:

CERTIFIED_STABLE

Otherwise return:

NOT_CERTIFIED

## Soundness source

The soundness source is Theorem 10V.3.

## Boundary

This algorithm does not prove RH.

This algorithm does not falsify RH.

This algorithm does not use zeta zeros.

This algorithm does not claim novelty.

Exact audit strings:

COMBINED_RADIUS_CERTIFIED_ALGORITHM

COMBINED_MINIMUM_RADIUS_CERTIFICATE

CERTIFIED_STABLE

NOT_CERTIFIED

