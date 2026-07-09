# Phase 5I — Sign-Chamber Geometry of the Three Response Channels

## Objective

Study the joint sign geometry of

\[
R_{\mathrm{atom}},
\qquad
R_{\mathrm{end}},
\qquad
R_{\mathrm{int}},
\]

using the frozen Phase 5H signed-transfer dataset.

The exact counting response is

\[
R_{\mathrm{count}}
=
R_{\mathrm{atom}}
+
R_{\mathrm{end}}
+
R_{\mathrm{int}}.
\]

Phase 5H found weak normalized interior alignment but frequent scalar cancellation.

Phase 5I therefore studies whether cancellation and deterministic-certificate looseness are concentrated in particular sign chambers or near chamber transitions in the frozen c-grid.

No RH consequence is claimed.

No novelty claim is made.

---

# Sign chambers

For a nonzero triple

\[
(R_{\mathrm{atom}},R_{\mathrm{end}},R_{\mathrm{int}}),
\]

define its sign chamber as one of

\[
(+,+,+),
(+,+,-),
(+,-,+),
(+,-,-),
(-,+,+),
(-,+,-),
(-,-,+),
(-,-,-).
\]

Frozen zero-sign tolerance:

\[
10^{-50}.
\]

If any component has magnitude at or below the tolerance, classify the point as

\[
\mathrm{BOUNDARY}.
\]

---

# Existing Phase 5H quantities

Scalar cancellation coefficient:

\[
C_{\mathrm{scalar}}
=
\frac{
|R_{\mathrm{count}}|
}{
|R_{\mathrm{atom}}|
+
|R_{\mathrm{end}}|
+
|R_{\mathrm{int}}|
}.
\]

Sup-certificate tightness:

\[
T_{\sup}
=
\frac{
|R_{\mathrm{count}}|
}{
|R_{\mathrm{atom}}|
+
\Lambda_n(H,\eta)\|E_D\|_\infty
}.
\]

---

# Frozen predictions

## P-CHM-001 — sign chamber exhaustiveness

PASS rule:

All 360 Phase 5H points are assigned to exactly one of the eight non-boundary sign chambers.

No BOUNDARY points may occur under the frozen \(10^{-50}\) tolerance.

---

## P-CHM-002 — same-sign chamber validation

For chambers

\[
(+,+,+)
\]

and

\[
(-,-,-),
\]

the scalar cancellation coefficient must equal one up to numerical error.

PASS rule:

Every same-sign point satisfies

\[
|C_{\mathrm{scalar}}-1|<10^{-45}.
\]

This is primarily an algebraic and implementation validation.

---

## P-CHM-003 — extreme cancellation is mixed-sign

Define extreme cancellation by

\[
C_{\mathrm{scalar}}<0.25.
\]

PASS rule:

At least 95 percent of extreme-cancellation points lie in mixed-sign chambers.

This result is expected to be largely algebraic because same-sign chambers cannot cancel.

---

## P-CHM-004 — mixed chambers differ in cancellation propensity

For each mixed-sign chamber containing at least 10 points, compute

\[
\Pr(
C_{\mathrm{scalar}}<0.25
\mid
\mathrm{chamber}
).
\]

PASS rule:

Among eligible mixed chambers,

\[
\max p_j-\min p_j>0.25.
\]

This is a descriptive finite-data comparison.

---

## P-CHM-005 — extreme certificate looseness is chamber-concentrated

Define extreme certificate looseness as membership in the bottom quartile of

\[
T_{\sup}.
\]

For each chamber \(j\), let

\[
p_j
\]

be its global frequency and

\[
q_j
\]

its frequency among bottom-quartile points.

Define enrichment

\[
E_j=q_j/p_j
\]

whenever \(p_j>0\).

PASS rule:

At least one chamber satisfies

\[
E_j>1.5.
\]

---

## P-CHM-006 — chamber transitions are common in c

Within each fixed window, order points by frozen requested coordinates

\[
c=1,2,\ldots,20.
\]

Count chamber changes between consecutive coordinates.

PASS rule:

Mean chamber transitions per window exceed 5.

---

## P-CHM-007 — cancellation intensifies near chamber transitions

For each point, define transition distance as the minimum frozen c-grid distance to a chamber transition in the same window.

Near-transition points:

transition distance at most 1.

Far-transition points:

transition distance at least 3.

PASS rule:

\[
\operatorname{median}
C_{\mathrm{near}}
<
\operatorname{median}
C_{\mathrm{far}}.
\]

---

# Required outputs

The experiment must report:

- total point count;
- boundary point count;
- count and frequency of every chamber;
- same-sign validation point count;
- maximum same-sign deviation from one;
- extreme-cancellation point count;
- mixed-sign share of extreme-cancellation points;
- per-mixed-chamber extreme-cancellation rate;
- maximum-minus-minimum eligible mixed-chamber rate;
- bottom-quartile Tsup threshold;
- per-chamber bottom-quartile enrichment;
- maximum chamber enrichment;
- transitions per window;
- mean and median transitions per window;
- near-transition point count;
- far-transition point count;
- median near-transition C_scalar;
- median far-transition C_scalar;
- frozen P-CHM-001 through P-CHM-007 scorecard.

All point-level classifications must be written to CSV.

A chamber summary CSV must be written separately.

A JSON summary must be written separately.

---

# Failure-prevention rules

1. Same-sign chamber cancellation equal to one is algebraic and is not empirical discovery.

2. Extreme cancellation appearing in mixed-sign chambers is partly definition-driven.

3. Chamber labels use the response components themselves.

4. All Phase 5I statistics are in-sample descriptive quantities.

5. Chamber enrichment is not a probability model.

6. Transition proximity does not imply causation.

7. No asymptotic theorem follows.

8. No RH consequence follows.

