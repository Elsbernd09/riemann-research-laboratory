# External Results Register

## Purpose

This register records statements the project may want to refer to that come from outside the project and are **not** published, refereed theorems. It exists so that such statements are never silently relabelled as KNOWN THEOREM, and so that it is always visible whether any project result depends on them.

It does not change any existing claim, any ledger entry, or any result of the project. It adds no phase.

## Status

The Claim Ledger allowed eight statuses. None fits a claim that has appeared only as an unrefereed preprint: it is not a KNOWN THEOREM (not published or standard), not a KNOWN CONJECTURE (its authors claim a proof), and not a PROVED IN PROJECT statement.

**UNREFEREED EXTERNAL CLAIM was adopted on 30 October 2026 at the project owner's instruction** and is now defined in `research_ledger/CLAIM_LEDGER.md` and listed in `README.md`. Rules:

1. It must be recorded here with its source, exact statement and the date it was read.
2. It may be used only as an explicitly labelled hypothesis. It must never be an input to a statement marked PROVED IN PROJECT unless the statement says so in its hypotheses.
3. It is promoted to KNOWN THEOREM only after publication or independent verification, with the source recorded. It is moved to FAILED CLAIM if a flaw is found.
4. No novelty or originality language for the project is permitted on the strength of it.

Ledger entries: ER-0001 is CL-E001, ER-0002 is CL-E002, ER-0003 is CL-E003.

## Register

### ER-0001. Zero-free half-plane for ζ at 7/8

**Source.** OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane ℜs > 7/8*, 30 September 2026, Theorem 1.1 (p. 4). Listed as entry 003 in the OpenAI math repository, as mirrored in the fork `brentharts/openai_math_yang_mills` (see the pointer below).

**Exact statement (paraphrase of the abstract and Theorem 1.1).** Every Dirichlet L-function, including ζ(s), has no zero in ℜs > 7/8, with the principal pole at s = 1 allowed. The same holds for every finite-order Hecke L-function over ℚ(√−3). The boundary ℜs = 7/8 is not excluded.

**Immediate consequence.** With the functional equation, every nontrivial zero ρ of ζ satisfies 1/8 ≤ ℜρ ≤ 7/8, that is |ℜρ − 1/2| ≤ 3/8.

**Status.** UNREFEREED EXTERNAL CLAIM. The paper states that it does not prove the Riemann Hypothesis. I have not checked its proof.

**Does any project result depend on it?** No. The main theorem in `paper/01_SCOPE_AND_MAIN_RESULT.md` is stated through E(t) = N(t) − M(t) and S₁(t) and does not use a zero-free region.

**Where it could matter.**
- *Interpretation of the zero surgery parameter.* In `docs/ZERO_SURGERY_SPECIFICATION.md` the displacement parameter satisfies 0 < δ < 1/2. If ER-0001 holds, a hypothetical **actual** zero of ζ off the line would have δ ≤ 3/8. The specification already says that Level I surgery does not define a modified zeta function, so synthetic experiments with δ > 3/8 are not contradicted. They simply could not be read as describing actual zeros of ζ. A numerical check of the quadratic response up to δ = 3/8 is in `docs/QUADRATIC_RESPONSE_DELTA_RANGE.md` (ledger entry CL-E004).
- *RH-conditional refinement.* The refinement that gains a factor (log log H)² assumes RH. A version assuming only that all zeros satisfy ℜρ ≤ θ for some θ < 1 would be a PROJECT CONJECTURE candidate **only after** the prior-art investigation required by the Discovery threshold. No claim is made here about whether such a version is known or true.

### ER-0002. Zero-free half-plane for ζ at 11/12

**Source.** OpenAI, *The Quasi-Riemann Hypothesis* (companion), 5 October 2026, Theorem 1.1. Part I of the 30 September paper contains the same 11/12 stage (its §11).

**Statement.** Every Dirichlet L-function, including ζ, and every finite-order Hecke L-function over ℚ(√−3), has no zero in ℜs > 11/12.

**Status.** UNREFEREED EXTERNAL CLAIM. The companion paper describes this as an intermediate step toward ER-0001, so it is weaker and adds no independent evidence for it. **Dependence:** none.

### ER-0003. Uniform exclusion of Landau–Siegel zeros

**Source.** OpenAI, *Uniform exclusion of Landau–Siegel zeros*, 1 October 2026, Theorem 1.

**Statement.** There is an absolute constant c > 0 such that every real zero β ∈ (0, 1) of every primitive nonprincipal real Dirichlet L-function of conductor q ≥ 3 satisfies (1 − β) log q ≥ c.

**Status.** UNREFEREED EXTERNAL CLAIM. It concerns real characters, not ζ itself. **Dependence:** none. Recorded because it appears in the same group of claims.

## How to cite these in project documents

- Write "claimed in an unrefereed preprint [ER-000x]", never "it is known that" or "it has been shown that".
- Never describe the project's results as relying on, extending or supporting them.
- If a document uses one as a hypothesis, state it in the hypotheses of that statement.

## Pointer

A reading guide to the three source papers, with figures and a small zero-counting check using the same smooth term M(t) as this project, is in the OpenAI-math fork note `ZETA_ZEROS.md` (fork: `brentharts/openai_math_yang_mills`). It is a reading guide, not a verification: the proofs have not been checked.

## Questions for review

1. Is a θ-restricted version of the RH-conditional refinement worth a prior-art audit, or does it fall outside the project's scope?
2. The one-quartet check in `docs/QUADRATIC_RESPONSE_DELTA_RANGE.md` leaves open the aggregate response over many zeros for δ up to 3/8.
