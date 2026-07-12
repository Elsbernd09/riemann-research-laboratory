# Code Artifact List

## Interval infrastructure

- `src/level4/interval_matrix.py`

Implements real interval arithmetic, interval matrices, Hermitian residual checks, Rayleigh quotient intervals, and negative-direction certificate logic.

## Arithmetic entry blueprint

- `src/level4/arithmetic_entry_blueprint.py`

Implements the interval component container for arithmetic matrix entries.

## Toy basis

- `src/level4/toy_basis.py`

Implements triangular log-coordinate toy basis functions, star evaluation, and prototype multiplicative convolution.

## Toy arithmetic entry

- `src/level4/toy_arithmetic_entry.py`

Computes floating-point prototype central, star-central, prime, constant, archimedean, and final arithmetic entry components.

## Toy arithmetic matrix

- `src/level4/toy_matrix_prototype.py`

Assembles a small toy arithmetic matrix, symmetrizes it, wraps it in crude intervals, and runs Rayleigh interval certificate logic.

## Important warning

The toy computation is not a certified arithmetic-only RH certificate. It is only a prototype pipeline.

