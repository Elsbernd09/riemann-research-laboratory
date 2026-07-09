# Phase 4G Equal-Weight Three-Orbit High-Precision Audit

## Objective

Determine whether the strongest equal-weight three-orbit near-cancellation candidates from Phase 4F are:

1. numerical precision artifacts;
2. exact equalities at higher precision;
3. anomalously close relative to the admissible parity-local moment spacing;
4. or ordinary extreme-value outcomes in a large search.

---

# 1. Search target

The rigid equal-weight three-orbit equation is

\[
A_r=A_p+A_q,
\]

where

\[
A_k
=
c_k^6\sqrt{c_k^2+4},
\]

subject to

\[
p\equiv q\pmod2,
\]

\[
r\not\equiv p\pmod2,
\]

and

\[
r>\max(p,q).
\]

The Phase 4F search examined candidate landings in the opposite-parity moment subsequence.

---

# 2. Strongest candidate

The strongest parity-local candidate in the searched range was

\[
\boxed{
(p,q,r)
=
(1995,2225,2350).
}
\]

The 500-decimal-digit audit independently recomputed the required blind scales and moments.

The candidate did not become an exact equality.

Its signed residual remained nonzero at 500 decimal digits.

The high-precision recomputation preserved both normalized defect statistics to extreme relative accuracy.

Thus the candidate is not a low-precision artifact.

---

# 3. Global normalized defect

For a candidate triple define

\[
D(p,q,r)
=
\frac{
|A_r-A_p-A_q|
}{
A_r+A_p+A_q
}.
\]

For the strongest candidate,

\[
\boxed{
D
\approx
4.4320976\times10^{-11}.
}
\]

Viewed alone, this is numerically very small.

However, the moment values and local spacings are enormous at high blind-scale indices.

Therefore D cannot by itself establish anomalous additive structure.

---

# 4. Parity-local defect

For the target

\[
T=A_p+A_q,
\]

let the consecutive admissible opposite-parity moments around the target define the local parity spacing.

The parity-local defect is

\[
E
=
\frac{
|A_r-T|
}{
\Delta_{\mathrm{par}}
}.
\]

For the strongest candidate,

\[
\boxed{
E_{\min,\mathrm{obs}}
=
0.00000014920384409657137373515322075499153717310195648445328993777144793723612
}
\]

approximately.

Equivalently,

\[
\boxed{
E_{\min,\mathrm{obs}}
\approx
1.4920384409657\times10^{-7}.
}
\]

---

# 5. Number of searched candidate records

The full Phase 4F checkpoint recorded

\[
\boxed{
M
=
3{,}357{,}233
}
\]

candidate records.

This large multiple-search count is essential when interpreting the smallest observed defect.

---

# 6. Crude extreme-value benchmark

A heuristic null model was declared:

\[
E
\sim
\operatorname{Uniform}(0,1/2).
\]

This model is not proved.

The candidate defects are dependent and need not be uniformly distributed.

It is used only as a simple extreme-value benchmark.

For M independent Uniform(0,1/2) samples, the expected minimum is

\[
\frac{1}{2(M+1)}.
\]

At

\[
M=3{,}357{,}233,
\]

the benchmark expected minimum is

\[
\boxed{
E_{\min,\mathrm{exp}}
\approx
1.4893212686\times10^{-7}.
}
\]

The observed-to-expected ratio is

\[
\boxed{
\frac{
E_{\min,\mathrm{obs}}
}{
E_{\min,\mathrm{exp}}
}
=
1.0018244366634174229\ldots
}
\]

Thus the observed minimum is extremely close to the crude null expected minimum.

---

# 7. Heuristic extreme-value probability

Under the same iid Uniform(0,1/2) benchmark,

\[
P(
\min E\le e
)
=
1-(1-2e)^M.
\]

At the observed minimum,

\[
\boxed{
P(
\min E\le E_{\min,\mathrm{obs}}
)
=
0.63279106499581505689\ldots
}
\]

approximately.

This is not a rigorous p-value.

The iid and uniform assumptions have not been established.

However, under the declared benchmark, the observed best candidate is not unusually close.

---

# 8. Main conclusion

The Phase 4F search produced very small global normalized defects.

The parity-local spacing normalization and extreme-value benchmark remove the appearance of anomalous additive structure.

The strongest observed parity-local defect is almost exactly at the crude expected minimum for the number of searched candidate records.

Therefore the current project conclusion is:

\[
\boxed{
\text{No anomalous equal-weight three-orbit additive resonance evidence was identified in the searched range.}
}
\]

---

# 9. Negative result

The search does not support introducing a project conjecture that the blind-scale moments satisfy an unusual three-term additive resonance law.

No exact relation

\[
A_r=A_p+A_q
\]

was certified.

No unusually small parity-local defect was observed relative to the declared crude extreme-value benchmark.

Accordingly, the project does not elevate the best triple to a mathematical conjecture.

---

# 10. Prediction scorecard

## P-TRI-001

Prediction:

The initial finite campaign will not certify an exact equality.

Result:

PASS.

## P-TRI-002

Prediction:

The minimum global normalized defect D will decrease strongly with search range.

Result:

PASS.

## P-TRI-003

Prediction:

The parity-local defect E will be more discriminating than D.

Result:

PASS.

The tiny global defect was not accompanied by anomalous parity-local spacing behavior.

## P-TRI-004

Prediction:

The strongest candidates will occur at relatively high indices.

Result:

PASS.

Qualitative prediction score:

\[
4/4.
\]

This score concerns project search predictions and is not evidence for RH.

---

# 11. Interpretation boundary

The crude iid Uniform(0,1/2) model is heuristic.

A rigorous distribution theorem for the parity-local defects has not been proved.

Therefore the project does not claim that the defects are random or uniformly distributed.

The supported statement is narrower:

The observed minimum was not anomalous under the declared simple benchmark.

---

# 12. RH implication

None.

The three-orbit search does not prove RH, exclude off-critical zeros, establish Li positivity, or control the full zeta zero sum.
