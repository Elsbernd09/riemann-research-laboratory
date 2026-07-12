# Phase 10AX — Transfer Certificate Calculator

## Purpose

Phase 10AX implements the integrated transfer-certificate calculator promised in Phase 10AW.

The calculator takes:

\[
R,\quad m,\quad \tau,\quad \pi,\quad \kappa,\quad \chi,\quad \eta
\]

and computes:

\[
\mathcal E_N^{(m)}
=
\tau_N^{(m)}
+
\pi_N^{(m)}
+
\kappa_N^{(m)}
+
\chi_N^{(m)}.
\]

It then computes:

\[
R^2m\mathcal E_N^{(m)}.
\]

If a negativity margin \(\eta\) is supplied, it checks whether

\[
R^2m\mathcal E_N^{(m)}<\eta/2.
\]

If yes, the calculator returns:

`NEGATIVE_DIRECTION_TRANSFER_CERTIFIED`

Otherwise it returns:

`NEGATIVE_DIRECTION_TRANSFER_NOT_CERTIFIED`.

## Theorem-backed meaning

This calculator is backed by Phase 10AW.

If the input error bounds are valid, then the output transfer bound is valid.

If the input error bounds are valid and the negativity margin passes, then finite negative-direction transfer is certified under the conditional theorem.

## Important limitation

This calculator does not prove that the input bounds are true.

It only combines supplied bounds in a theorem-backed way.

The classical truncation, projection, and kernel/model terms remain unresolved unless separately proven.

## Current status

TRANSFER_CERTIFICATE_CALCULATOR

TOTAL_ENTRYWISE_ERROR_COMPUTED

TRANSFER_BOUND_COMPUTED

NEGATIVE_DIRECTION_TRANSFER_CERTIFIED

NEGATIVE_DIRECTION_TRANSFER_NOT_CERTIFIED

CERTIFICATE_SHA256_RECORDED

UNCONDITIONAL_CLASSICAL_CONVERGENCE_NOT_PROVEN

NOT_RH_CONTRIBUTION_YET

## Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not prove unconditional classical convergence.

This phase does not import the true Weil form.

This phase does not claim novelty.

