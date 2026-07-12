# Phase 10AX Transfer Certificate Calculator Output

## Status

TRANSFER_CERTIFICATE_CALCULATOR

## Formula

\[
\mathcal E_N^{(m)}=\tau_N^{(m)}+\pi_N^{(m)}+\kappa_N^{(m)}+\chi_N^{(m)}
\]

\[
\text{transfer bound}=R^2m\mathcal E_N^{(m)}
\]

## Example: certified_margin_example

- total_entrywise_error_E_N_m: 0.0031
- transfer_bound_R2_m_E_N_m: 0.0372
- transfer_certificate: TRANSFER_BOUND_COMPUTED
- negative_direction_transfer: NEGATIVE_DIRECTION_TRANSFER_CERTIFIED
- certificate_sha256: db42ed491baf9fcb014665226f61e9b0c57ba32aa39096e0c20d6cb04c7b8a27

## Example: not_certified_margin_example

- total_entrywise_error_E_N_m: 0.035
- transfer_bound_R2_m_E_N_m: 3.500
- transfer_certificate: TRANSFER_BOUND_COMPUTED
- negative_direction_transfer: NEGATIVE_DIRECTION_TRANSFER_NOT_CERTIFIED
- certificate_sha256: 967aab967fbd8965d99b30dd1f4c2d3803cae889dfca3fc579c7feba0cdcd038

## Example: bound_only_example

- total_entrywise_error_E_N_m: 0.00155
- transfer_bound_R2_m_E_N_m: 0.0069750
- transfer_certificate: TRANSFER_BOUND_COMPUTED
- negative_direction_transfer: ETA_NOT_PROVIDED
- certificate_sha256: 91a7cf7530d2adbf83dcd019ff0ee9a690649dada55338c241d2e71aee07673f

## Boundary

This calculator does not prove RH.

This calculator does not falsify RH.

This calculator does not prove a new RH criterion.

This calculator does not prove unconditional classical convergence.

This calculator does not import the true Weil form.

This calculator does not claim novelty.

## Exact audit strings

TRANSFER_CERTIFICATE_CALCULATOR

TOTAL_ENTRYWISE_ERROR_COMPUTED

TRANSFER_BOUND_COMPUTED

NEGATIVE_DIRECTION_TRANSFER_CERTIFIED

NEGATIVE_DIRECTION_TRANSFER_NOT_CERTIFIED

CERTIFICATE_SHA256_RECORDED

UNCONDITIONAL_CLASSICAL_CONVERGENCE_NOT_PROVEN

NOT_RH_CONTRIBUTION_YET

