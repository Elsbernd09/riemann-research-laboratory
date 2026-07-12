# Phase 9D — Representation Decision and Repair Plan

## Purpose

Phase 9C audited the Phase 9B synthetic eigenvalue validation output.

Phase 9D reads the Phase 9C representation status and chooses the correct next track.

This phase does not compute new eigenvalues.

This phase does not use zeta zeros.

This phase does not prove RH.

This phase does not claim novelty.

---

# 1. Possible statuses

## PRELIMINARY_SYNTHETIC_LOCK_POSSIBLE

This means all current synthetic cases passed the Hermitian gate and matched the Theorem 8 target.

If this status appears, the next track is:

\[
\texttt{FINAL\_SYNTHETIC\_VALIDATION\_SUITE}.
\]

This still does not say anything about zeta zeros.

---

## REPRESENTATION_NOT_LOCKED

This means at least one case was blocked or mismatched.

If this status appears, the next track is:

\[
\texttt{REPRESENTATION\_REPAIR\_REQUIRED}.
\]

This is not a mathematical contradiction.

It means the implementation/convention layer needs repair.

---

## UNKNOWN

This means the Phase 9C status could not be parsed.

If this status appears, manual inspection is required.

---

# 2. Repair targets if needed

If the representation is not locked, repair must focus on:

1. Hermitian conversion;
2. raw vs weighted matrix convention;
3. similarity transform convention;
4. multiplicity handling;
5. repeated-\(\gamma\) zero eigenvalue interpretation;
6. exact \(H\)-kernel normalization;
7. numerical tolerance.

---

# 3. Boundary

No new eigenvalues are computed in this phase.

No zeta zeros are used.

No RH proof.

No novelty claim.

No zeta-case Bombieri-Weil verification claim.

