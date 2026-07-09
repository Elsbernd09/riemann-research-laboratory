# Phase 5I — Sign-Chamber Geometry Report

## Status

COMPLETE.

## Population

The experiment used the frozen 360-point Phase 5H signed-transfer dataset.

No quadrature was recomputed.

No zero windows were added or removed.

---

# Chamber classification

Frozen zero-sign tolerance:

\[
10^{-50}.
\]

Boundary point count:

\[
0.
\]

Observed chamber counts:

\[
\begin{array}{c|r}
(+,+,+) & 5\\
(+,+,-) & 8\\
(+,-,+) & 66\\
(+,-,-) & 83\\
(-,+,+) & 104\\
(-,+,-) & 85\\
(-,-,+) & 6\\
(-,-,-) & 3
\end{array}
\]

P-CHM-001:

PASS.

All 360 points occupied one of the eight non-boundary sign chambers.

---

# Same-sign validation

Same-sign point count:

\[
8.
\]

Maximum observed deviation from

\[
C_{\mathrm{scalar}}=1
\]

was

\[
0.
\]

P-CHM-002:

PASS.

This is an algebraic and implementation validation.

It is not an independent empirical discovery.

---

# Extreme cancellation and mixed signs

Extreme-cancellation point count:

\[
185.
\]

Mixed-sign share:

\[
1.0.
\]

P-CHM-003:

PASS.

Qualification:

This is largely definition-driven because same-sign nonzero real components satisfy

\[
C_{\mathrm{scalar}}=1.
\]

---

# Mixed-chamber cancellation propensity

Among eligible mixed chambers with at least ten points, the observed conditional extreme-cancellation rates were approximately

\[
0.5455,
\quad
0.5542,
\quad
0.5865,
\quad
0.4941.
\]

The maximum-minus-minimum range was approximately

\[
0.09242.
\]

The frozen P-CHM-004 threshold required a range greater than

\[
0.25.
\]

P-CHM-004:

FAIL.

Interpretation:

Coarse mixed-sign chamber identity does not strongly discriminate extreme-cancellation propensity in the tested finite population.

The sign pattern identifies whether scalar cancellation is possible, but it does not encode the relative component magnitudes required to quantify severity.

---

# Certificate-looseness chamber enrichment

The bottom quartile of

\[
T_{\sup}
\]

contained 90 points.

The maximum observed chamber enrichment was approximately

\[
1.3012.
\]

The frozen P-CHM-005 threshold required enrichment greater than

\[
1.5.
\]

P-CHM-005:

FAIL.

Interpretation:

No sign chamber was strongly concentrated among the loosest deterministic certificates under the frozen enrichment rule.

---

# Chamber transitions

Observed transitions per 19-step window:

\[
13,13,12,8,13,12,12,9,15,13,13,13,14,13,9,14,13,13.
\]

Mean transitions per window:

\[
12.3333.
\]

Median:

\[
13.
\]

P-CHM-006:

PASS strongly.

Interpretation:

The signed response triple changes sign chamber frequently along the frozen integer c-grid.

No claim of chaos, randomness, or stochastic independence follows.

---

# Transition-proximity test

Near-transition point count:

\[
357.
\]

Far-transition point count:

\[
0.
\]

P-CHM-007:

FAIL.

Qualification:

The frozen transition-distance operationalization became non-discriminating under the observed high transition density.

Because no point had transition distance at least three, the far comparison group was empty.

The failure must not be reinterpreted as evidence that cancellation does or does not intensify near a transition.

The frozen test was unable to discriminate the hypothesis on the integer c-grid.

No threshold is changed post hoc.

---

# Phase scorecard

\[
\begin{array}{ll}
\mathrm{P\mbox{-}CHM\mbox{-}001} & \mathrm{PASS},\\
\mathrm{P\mbox{-}CHM\mbox{-}002} & \mathrm{PASS},\\
\mathrm{P\mbox{-}CHM\mbox{-}003} & \mathrm{PASS\ WITH\ ALGEBRAIC\ QUALIFICATION},\\
\mathrm{P\mbox{-}CHM\mbox{-}004} & \mathrm{FAIL},\\
\mathrm{P\mbox{-}CHM\mbox{-}005} & \mathrm{FAIL},\\
\mathrm{P\mbox{-}CHM\mbox{-}006} & \mathrm{PASS\ STRONGLY},\\
\mathrm{P\mbox{-}CHM\mbox{-}007} & \mathrm{FAIL\ —\ NON\mbox{-}DISCRIMINATING\ TEST}.
\end{array}
\]

---

# Main conclusion

The coarse eight-chamber sign classification is insufficient to explain the severity of scalar cancellation.

Signs identify whether cancellation can occur.

Among the dominant mixed-sign chambers, however:

- extreme-cancellation propensity varies only modestly;
- no chamber is strongly enriched among the loosest deterministic certificates;
- chamber transitions are extremely frequent.

The next analysis must retain relative component magnitudes rather than sign labels alone.

A natural representation is the component-share simplex

\[
a
=
\frac{|R_{\mathrm{atom}}|}{S},
\qquad
e
=
\frac{|R_{\mathrm{end}}|}{S},
\qquad
i
=
\frac{|R_{\mathrm{int}}|}{S},
\]

where

\[
S
=
|R_{\mathrm{atom}}|
+
|R_{\mathrm{end}}|
+
|R_{\mathrm{int}}|
\]

and

\[
a+e+i=1.
\]

---

# Restrictions

All results are finite-data and in-sample.

Chamber labels are derived from the response components.

Same-sign and mixed-sign consequences are partly algebraic.

No predictive generalization is established.

No asymptotic theorem is established.

No RH consequence follows.

