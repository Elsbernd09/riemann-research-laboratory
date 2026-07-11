# Referee Response Draft

This document anticipates likely objections to the manuscript.

---

## Objection 1

The result appears to be a direct consequence of classical \(S_1\)-bounds once the kernel derivative estimate is known.

### Response

We agree.

The paper does not claim the classical \(S_1\)-input is new. The contribution is the matched-scale specialization to the Li zero-coordinate susceptibility, the derivative hierarchy of the susceptibility kernel, and the exact centered-primitive response-transfer formulation.

We have revised the manuscript to state that the proof is short once the matched-scale Li susceptibility derivative hierarchy has been established.

---

## Objection 2

The theorem cannot imply RH because the scalar zero-counting function \(N(T)\) is horizontally blind.

### Response

We agree.

The manuscript explicitly states that \(N(T)\) records ordinates and multiplicities but discards horizontal zero coordinates. Therefore the theorem is not an RH criterion and is compatible with RH failure.

---

## Objection 3

The integration-by-parts step is suspicious because \(N(T)\) is a staircase function.

### Response

The proof uses ordinary integrals, not Stieltjes integrals.

We define

\[
F(t)
=
\int_H^t(E(s)-\overline E)ds.
\]

Then \(F\) is absolutely continuous and

\[
F'(t)=E(t)-\overline E
\]

almost everywhere. Since \(\chi_n'\) is \(C^1\) on the positive window, ordinary absolutely continuous integration by parts applies.

No Stieltjes atom term appears in the interior identity.

---

## Objection 4

The value of \(S(t)\) at zero ordinates is convention-dependent.

### Response

The main theorem uses ordinary integrals. Changing \(S(t)\) on the discrete set of zero ordinates does not affect those integrals.

Endpoint atom terms are treated separately and require explicit jump factors.

---

## Objection 5

The atom-share consequence was overstated.

### Response

This was corrected.

The manuscript now requires an explicit atom jump hypothesis

\[
\Delta N(H)=m_H\ge m_0>0.
\]

Kernel nondegeneracy alone does not imply atom existence.

---

## Objection 6

The numerical PCA does not prove anything.

### Response

We agree.

The numerical section is labeled finite-height motivation and validation only. The proof of the main theorem does not depend on numerical experiments.

---

## Objection 7

The Li kernel and its explicit-formula embedding are classical.

### Response

We agree.

The manuscript explicitly cites Bombieri-Lagarias and states that the Li kernel and Guinand-Weil embedding are classical.

---

## Objection 8

Weil positivity and Bombieri's quadratic functional already provide RH-equivalent positivity machinery.

### Response

We agree.

The manuscript does not claim a new Weil positivity framework.

---

## Objection 9

The manuscript claims novelty too strongly.

### Response

The manuscript does not claim novelty.

It states:

"No subsuming source has been identified in the current uploaded-corpus audit. This sentence is not a novelty claim. Originality remains under active prior-art review."

---

## Objection 10

The theorem is compatible with RH failure, so why is it interesting?

### Response

The theorem quantifies an unconditional asymptotic suppression mechanism for the interior zero-counting discrepancy response under the matched-scale Li susceptibility kernel.

It explains why the centered-primitive/interior response channel is lower order than the natural \(H^{-2}\) susceptibility scale. This gives a rigorous analytic mechanism behind the finite-height response geometry observed in the project.

Its value is response asymptotics, not RH implication.

