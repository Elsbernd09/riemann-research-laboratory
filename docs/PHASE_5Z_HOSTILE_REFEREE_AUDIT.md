# Phase 5Z — Hostile Referee Audit of the Manuscript

## Status

REFEREE-STYLE AUDIT COMPLETE.

MAIN THEOREM SURVIVES.

PAPER FRAMING REQUIRES TIGHTENING.

## Manuscript under audit

`paper/latex/main.tex`

Working title:

**Matched-Scale Li Susceptibility and Centered-Primitive Transfer of Zero-Counting Discrepancy**

---

# 1. Referee objection: The theorem may be a direct corollary of classical \(S_1\) theory plus a kernel derivative bound

## Objection

The proof of the main theorem has the following structure:

1. classical \(S_1(t)=O(\log t)\);
2. centered primitive \(F=O(\log H)\);
3. kernel estimate \(\int |\chi_n''|=O(H^{-3})\);
4. integration by parts.

This is mathematically clean, but the global response theorem may be viewed as a direct corollary once the matched-scale derivative estimates are established.

## Response

Accepted.

The paper should not oversell the theorem as a deep new RH mechanism.

The paper should frame the result as a precise matched-scale specialization:

- the classical input is \(S_1\)-control;
- the project input is the Li susceptibility derivative hierarchy;
- the contribution is the exact transfer theorem and the quantitative matched-scale specialization.

## Required paper framing

Use language such as:

> The theorem is a short consequence of classical first-primitive control once the matched-scale Li susceptibility derivative hierarchy is established.

Do not use language suggesting a new RH strategy.

---

# 2. Referee objection: The scalar counting discrepancy is horizontally blind

## Objection

The paper studies

\[
E(t)=N(t)-M(t).
\]

But \(N(t)\) records only ordinates and multiplicities. It does not record horizontal zero location. Therefore the theorem cannot distinguish RH from ordinate-identical off-critical configurations.

## Response

Accepted.

The manuscript already includes a horizontal-blindness section. This section must remain prominent.

## Required paper framing

The theorem is a response-asymptotic result, not an RH criterion.

---

# 3. Referee objection: Ordinary integration with a staircase function requires regularity care

## Objection

The function \(N(t)\) is a staircase. Therefore \(E(t)\) is not smooth. The integration-by-parts identity must be interpreted correctly.

## Response

Accepted.

The identity uses ordinary integrals, not Stieltjes integrals.

We define

\[
F(t)=\int_H^t(E(s)-\overline E)\,ds.
\]

Then \(F\) is absolutely continuous, with

\[
F'(t)=E(t)-\overline E
\]

almost everywhere.

Since \(\chi_n'\) is continuously differentiable on the positive interval, ordinary integration by parts for absolutely continuous \(F\) applies.

No Stieltjes atom term appears in the interior identity.

## Required manuscript language

Add a sentence near the transfer identity:

> Since \(F\) is absolutely continuous and \(\chi_n'\) is \(C^1\) on the window, the integration by parts is the ordinary absolutely-continuous integration-by-parts formula.

---

# 4. Referee objection: \(S_1\) normalization and point values at zeros

## Objection

The definition of \(S(t)\) at zero ordinates varies by convention. The manuscript must clarify that the ordinary integrals are unaffected.

## Response

Accepted.

Already addressed, but strengthen the wording.

## Required manuscript language

State:

> Any change of \(S(t)\) on the discrete zero set changes neither \(S_1\) nor the ordinary integrals used here.

---

# 5. Referee objection: Uniformity in \(n/H\in K\)

## Objection

The theorem claims uniformity in \(n/H\in K\). This depends on compactness away from \(0\). The paper must explicitly track the induced compact set on the full relative window.

## Response

Accepted.

Already included:

\[
K_\eta=
[c_-/(1+\eta),c_+].
\]

## Required manuscript language

Keep this compactness reduction in the proof.

Do not state uniformity down to \(n/H=0\).

---

# 6. Referee objection: Endpoint difference \(|\chi(B)-\chi(H)|=O(H^{-2})\) is crude

## Objection

The proof only uses the pointwise bound

\[
\chi=O(H^{-2}).
\]

It does not exploit cancellation in the difference. This is fine but should be stated honestly.

## Response

Accepted.

This is intentional.

## Required manuscript language

Keep:

> No subtraction asymptotic is needed; the uniform pointwise bound is sufficient.

---

# 7. Referee objection: Numerical experiments are irrelevant to proof

## Objection

The numerical PCA and zero-window experiments are not needed for the theorem.

## Response

Accepted.

The numerical section must be clearly labeled motivation only.

## Required manuscript language

Keep:

> These computations are not proof dependencies.

---

# 8. Referee objection: Prior-art novelty remains unresolved

## Objection

The uploaded-corpus audit is not a complete novelty audit. The phrase "No subsuming source identified" is insufficient for novelty.

## Response

Accepted.

The manuscript must not claim novelty.

## Required manuscript language

Keep:

> No subsuming source has been identified in the current uploaded-corpus audit. This sentence is not a novelty claim. Originality remains under active prior-art review.

---

# 9. Referee objection: The Li kernel's explicit-formula embedding is classical

## Objection

The paper must not imply that embedding \(f_n\) into explicit-formula machinery is new.

## Response

Accepted.

Bombieri--Lagarias already connect Li coefficients to the Guinand--Weil explicit formula.

## Required manuscript language

Keep classical Li/Weil section.

---

# 10. Referee objection: The main result's value may be expository/specialization rather than transformative

## Objection

The main theorem packages classical \(S_1\)-control with a project-specific kernel. Its value may be as a precise specialization and response estimate, not a major breakthrough.

## Response

Accepted.

The correct paper claim is:

> We identify and quantify a matched-scale response-transfer mechanism for the Li susceptibility kernel.

Not:

> We make progress toward RH.

---

# 11. Audit conclusion

The theorem survives.

The manuscript should be framed as:

1. a clean matched-scale specialization;
2. a response-transfer theorem;
3. an unconditional suppression estimate;
4. a rigorous explanation of finite numerical component-share behavior;
5. not an RH criterion.

The strongest theorem remains:

\[
R_{\mathrm{int}}
=
O_{K,\eta}
\left(
\frac{\log H}{H^3}
\right).
\]

No RH proof.

No novelty claim.

