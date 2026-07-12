# Phase 11D — Sharper Transfer Certificate Calculator

## Purpose

Phase 11D implements the sharper transfer certificate calculator under the extracted-kernel alignment assumption:

\[
\kappa_N^{(m)}=0.
\]

The calculator uses the three-error bound:

\[
R^2m
\left(
\tau_N^{(m)}
+
\pi_N^{(m)}
+
\chi_N^{(m)}
\right).
\]

## Inputs

\[
R,\quad m,\quad \tau,\quad \pi,\quad \chi,\quad \eta.
\]

## Computed quantity

\[
\mathcal E_{\mathrm{sharp},N}^{(m)}
=
\tau_N^{(m)}
+
\pi_N^{(m)}
+
\chi_N^{(m)}.
\]

## Sharper transfer bound

\[
R^2m\mathcal E_{\mathrm{sharp},N}^{(m)}.
\]

## Negative-direction certificate

If

\[
R^2m\mathcal E_{\mathrm{sharp},N}^{(m)}<\eta/2,
\]

then the sharper negative-direction transfer margin is certified under the conditional theorem.

## Important limitation

This calculator assumes extracted-kernel alignment.

It does not prove full classical validation.

It does not prove the truncation bound.

It does not prove the projection bound.

It only computes the theorem-backed certificate once the bounds are supplied.

## Current status

SHARPER_TRANSFER_CERTIFICATE_CALCULATOR

KAPPA_ZERO_UNDER_EXTRACTED_KERNEL_ALIGNMENT

SHARPER_TOTAL_ERROR_COMPUTED

SHARPER_TRANSFER_BOUND_COMPUTED

SHARPER_NEGATIVE_DIRECTION_TRANSFER_CERTIFIED

SHARPER_NEGATIVE_DIRECTION_TRANSFER_NOT_CERTIFIED

CERTIFICATE_SHA256_RECORDED

FULL_CLASSICAL_VALIDATION_NOT_PROVEN

NOT_RH_CONTRIBUTION_YET

## Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not prove full classical validation.

This phase does not prove unconditional classical convergence.

This phase does not establish novelty.

