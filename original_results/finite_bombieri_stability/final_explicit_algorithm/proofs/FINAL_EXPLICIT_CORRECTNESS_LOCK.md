# Final Explicit Correctness Lock

## Correctness theorem

If Algorithm 10AF.1 outputs:

CERTIFIED_STABLE

then, under the compact-domain and Hermitian hypotheses,

\[
n_-(M(\widetilde\Gamma,t))=
n_-(M(\Gamma,t)).
\]

## Soundness source

The proof depends on:

1. the explicit \(H\)-kernel Lipschitz theorem;
2. the explicit \(H\)-kernel support-stability certificate;
3. the spectral-gap stability principle.

## Non-certification

If Algorithm 10AF.1 outputs:

NOT_CERTIFIED

then no instability claim is made.

NOT_CERTIFIED means only that the certificate did not prove stability.

## Exact audit strings

FINAL_EXPLICIT_ALGORITHM_CORRECTNESS_PROOF

FINAL_EXPLICIT_H_KERNEL_CERTIFIED_ALGORITHM

EXPLICIT_H_KERNEL_SUPPORT_STABILITY_CERTIFICATE

CERTIFIED_STABLE

NOT_CERTIFIED

## Boundary

This proof does not prove RH.

This proof does not falsify RH.

This proof does not use zeta zeros.

This proof does not claim novelty.

