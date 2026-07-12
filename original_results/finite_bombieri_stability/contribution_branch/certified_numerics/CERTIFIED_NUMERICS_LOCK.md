# Certified Numerics Lock

## Computational error

\[
C_{ij}^{(N)}
=
\widetilde G^{(N)}_{ij}-G^{(N),exact}_{ij}.
\]

## Interval certificate

If

\[
G^{(N),exact}_{ij}\in[\ell_{ij}^{(N)},u_{ij}^{(N)}],
\]

then

\[
|\widetilde G^{(N)}_{ij}-G^{(N),exact}_{ij}|
\leq
r_{ij}^{(N)}.
\]

## Global numerical certificate

\[
\chi_N^{(m)}
=
\max_{i,j}r_{ij}^{(N)}.
\]

Then

\[
|C_{ij}^{(N)}|\leq \chi_N^{(m)}.
\]

## Matrix-level bound

\[
\|\widetilde G^{(N)}-G^{(N),exact}\|_2
\leq
m\chi_N^{(m)}.
\]

## Exact audit strings

CERTIFIED_NUMERICAL_ERROR_MODEL

INTERVAL_CERTIFIED_COMPUTATIONAL_ERROR_BOUND

MATRIX_LEVEL_NUMERICAL_ERROR_BOUND

CHI_N_M_NUMERICAL_ERROR_CERTIFICATE

COMPUTATIONAL_ERROR_CONTROLLED_CONDITIONALLY

CERTIFIED_NUMERICS_WORKFLOW

NOT_RH_CONTRIBUTION_YET

