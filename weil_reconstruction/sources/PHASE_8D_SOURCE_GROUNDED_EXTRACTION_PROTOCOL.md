# Phase 8D — Source-Grounded Weil Extraction Protocol

## Purpose

Phase 8C selected Bombieri-style Weil quadratic form reconstruction as the next path.

Phase 8D establishes the rule for doing that reconstruction correctly:

\[
\boxed{
\text{Do not reconstruct exact Weil formulae from memory. Extract them from sources.}
}
\]

This phase does not prove RH.

This phase does not claim a new Weil criterion.

This phase creates the source-grounded protocol needed before any exact formula, code, or theorem is added.

---

# 1. Why this protocol is necessary

The Weil criterion has multiple equivalent formulations.

Small differences in convention can change:

1. the test-function class;
2. the transform normalization;
3. the zero-side expression;
4. the prime-side expression;
5. signs in the quadratic form;
6. which positivity statement is exactly RH-equivalent.

Therefore, the project must not proceed by informal memory.

Every exact formula must be source-extracted and convention-locked.

---

# 2. Required extraction fields

For every source used in Phase 8, record:

## Bibliographic identity

- author;
- title;
- year;
- section/page/theorem number;
- file path or citation pointer.

## Test-function class

Record exactly:

- domain;
- smoothness;
- decay;
- compact support conditions;
- symmetry conditions;
- transform assumptions.

## Transform convention

Record exactly:

- Fourier/Mellin/Laplace convention;
- sign in the exponential;
- normalization constants;
- variable names;
- inversion convention if used.

## Zero-side expression

Record exactly:

- sum over zeros;
- multiplicity convention;
- pairing convention;
- whether zeros are shifted or transformed;
- convergence interpretation.

## Prime-side expression

Record exactly:

- prime sum terms;
- archimedean terms;
- pole/trivial-zero terms;
- constants.

## Quadratic form

Record exactly:

- functional being tested;
- positivity condition;
- admissible functions;
- statement equivalent to RH;
- how off-critical zeros generate negative directions.

## Finite truncation connection

Record exactly:

- whether finite truncations appear in the source;
- what matrix or finite form is used;
- what convergence claim is made;
- whether negative eigenvalues are discussed.

---

# 3. Forbidden actions

Until extraction is complete, do not:

1. write a claimed exact Weil quadratic formula;
2. implement a claimed Weil matrix;
3. call a toy matrix a Weil form;
4. claim finite-rank detection is classical;
5. claim new RH progress;
6. publish breakthrough language.

---

# 4. Allowed actions

Allowed before extraction is complete:

1. create reading templates;
2. create convention tables;
3. create source comparison files;
4. identify unknowns;
5. record possible reconstruction paths;
6. write toy code only if clearly labeled diagnostic.

---

# 5. Phase 8D conclusion

The next mathematical step is not coding.

The next mathematical step is exact source extraction.

