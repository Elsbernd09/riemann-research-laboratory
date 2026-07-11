# Phase 8G — Full T[f] Functional Extraction Worksheet

## Purpose

Phase 8F extracted Bombieri Theorem 1 and Theorem 2 at statement level.

The next task is to extract the exact full formula for Bombieri's linear functional

\[
T[f].
\]

This phase does not fill the formula from memory.

This phase creates the worksheet and locking criteria needed to extract the formula correctly from the source.

This is not a proof of RH.

This is not a new Weil criterion.

This is not a novelty claim.

---

# 1. Why this phase is necessary

Bombieri Theorem 2 states that

\[
T[f]=T[f^*]=\sum_\rho f(\rho),
\]

and that RH is equivalent to positivity of

\[
T[f*f^*]\ge0.
\]

But before any exact computation or finite-rank reconstruction, the project must know the full formula for

\[
T[f].
\]

That formula contains more than the zero-side term.

It may include:

1. zero-side terms;
2. pole terms;
3. prime-side terms;
4. archimedean terms;
5. normalization constants;
6. transform conventions;
7. convergence conventions.

---

# 2. Extraction target

The target is to extract Bombieri's exact formula for

\[
T[f].
\]

The extraction must include:

## Zero-side term

Record the exact expression involving

\[
\sum_\rho f(\rho).
\]

## Prime-side term

Record the exact prime or prime-power sum.

## Pole term

Record any contribution from the pole of zeta.

## Trivial-zero term

Record whether trivial zeros are included, canceled, or represented through another term.

## Archimedean term

Record the gamma-factor or infinite-place contribution.

## Normalization

Record every constant and sign.

## Transform convention

Record whether the formula uses Mellin, Fourier, or another transform convention.

## Admissible class

Record exactly which function class is being used.

---

# 3. Current status

The following are already extracted at statement level:

\[
T[f]=T[f^*]=\sum_\rho f(\rho).
\]

\[
T[f*f^*]\ge0
\]

is RH-equivalent on the Bombieri test class.

The following remain unlocked:

1. exact full formula for \(T[f]\);
2. exact prime-side term;
3. exact archimedean term;
4. exact transform convention;
5. exact convergence interpretation;
6. exact finite truncation connection.

---

# 4. Extraction worksheet

## Source location

Source:

Bombieri, Remarks on Weil's quadratic functional in the theory of prime numbers, I.

Section:

TBD.

Page:

TBD.

Equation number:

TBD.

Theorem/definition number:

TBD.

---

## Exact original formula

Paste the original formula here before simplifying.

Status:

UNFILLED.

---

## Project notation translation

Translate the source formula into project notation only after the original is recorded.

Status:

BLOCKED.

---

## Term-by-term decomposition

### Zero-side term

Status:

PARTIAL.

Known statement-level identity:

\[
T[f]=\sum_\rho f(\rho).
\]

Exact convention:

UNLOCKED.

### Prime-side term

Status:

UNLOCKED.

### Pole term

Status:

UNLOCKED.

### Trivial-zero term

Status:

UNLOCKED.

### Archimedean term

Status:

UNLOCKED.

### Constants and signs

Status:

UNLOCKED.

### Transform convention

Status:

UNLOCKED.

---

# 5. Locking criteria

The full formula for

\[
T[f]
\]

may be marked LOCKED only after the repository contains:

1. the exact source formula;
2. the source location;
3. the project notation translation;
4. a term-by-term decomposition;
5. an audit confirming no term was dropped;
6. an explicit statement that no finite-rank code depends on unlocked conventions.

---

# 6. Forbidden next steps

Do not implement a Weil matrix yet.

Do not write finite truncation code yet.

Do not claim an exact arithmetic-side functional yet.

Do not compare Phase 7 toy matrices to \(T[f*f^*]\) yet.

Do not claim RH progress.

---

# 7. Phase conclusion

Phase 8G prepares the extraction of the full Bombieri functional.

The next phase should fill this worksheet from the source text.

