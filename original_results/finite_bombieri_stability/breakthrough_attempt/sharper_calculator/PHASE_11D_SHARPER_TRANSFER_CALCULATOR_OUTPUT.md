# Phase 11D Sharper Transfer Certificate Calculator Output

## Status

SHARPER_TRANSFER_CERTIFICATE_CALCULATOR

## Assumption

KAPPA_ZERO_UNDER_EXTRACTED_KERNEL_ALIGNMENT

## Formula

\[
\mathcal E_{sharp,N}^{(m)}=\tau_N^{(m)}+\pi_N^{(m)}+\chi_N^{(m)}
\]

\[
\text{sharper transfer bound}=R^2m\mathcal E_{sharp,N}^{(m)}
\]

## Example: sharper_certified_margin_example

- sharper_total_error_tau_pi_chi: 0.0021
- sharper_transfer_bound_R2_m_tau_pi_chi: 0.0252
- transfer_certificate: SHARPER_TRANSFER_BOUND_COMPUTED
- negative_direction_transfer: SHARPER_NEGATIVE_DIRECTION_TRANSFER_CERTIFIED
- certificate_sha256: aed5a5ea5af12212fd2d747dee46a6669c3c87397f121548629cca199ba4aaac

## Example: sharper_not_certified_margin_example

- sharper_total_error_tau_pi_chi: 0.025
- sharper_transfer_bound_R2_m_tau_pi_chi: 2.500
- transfer_certificate: SHARPER_TRANSFER_BOUND_COMPUTED
- negative_direction_transfer: SHARPER_NEGATIVE_DIRECTION_TRANSFER_NOT_CERTIFIED
- certificate_sha256: 4a193953f4bfed4478b9b3e614b9d6548ecce722162066f1eb1e8dacc50f5cdc

## Example: sharper_bound_only_example

- sharper_total_error_tau_pi_chi: 0.00105
- sharper_transfer_bound_R2_m_tau_pi_chi: 0.0047250
- transfer_certificate: SHARPER_TRANSFER_BOUND_COMPUTED
- negative_direction_transfer: ETA_NOT_PROVIDED
- certificate_sha256: 9c714bd248a1e6e3b2a96cfca8c8649b4400f004526cc8de4a60dcc860b87d91

## Boundary

This calculator does not prove RH.

This calculator does not falsify RH.

This calculator does not prove a new RH criterion.

This calculator does not prove full classical validation.

This calculator does not prove unconditional classical convergence.

This calculator does not claim novelty.

## Exact audit strings

SHARPER_TRANSFER_CERTIFICATE_CALCULATOR

KAPPA_ZERO_UNDER_EXTRACTED_KERNEL_ALIGNMENT

SHARPER_TOTAL_ERROR_COMPUTED

SHARPER_TRANSFER_BOUND_COMPUTED

SHARPER_NEGATIVE_DIRECTION_TRANSFER_CERTIFIED

SHARPER_NEGATIVE_DIRECTION_TRANSFER_NOT_CERTIFIED

CERTIFICATE_SHA256_RECORDED

FULL_CLASSICAL_VALIDATION_NOT_PROVEN

NOT_RH_CONTRIBUTION_YET

