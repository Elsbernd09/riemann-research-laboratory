# Phase 5L — Disjoint Higher-Zero Principal-Axis Replication

## Objective

Test the frozen first-500-zero component-share principal axis on disjoint higher-zero response windows.

The primary centroid and principal axis are frozen in

`results/phase5l_frozen_primary_axis.json`

before generation or inspection of any Phase 5L higher-zero component-share point.

No RH consequence is claimed.

No novelty claim is made.

---

# Primary frozen model

Let

\[
\mu_{500}
\]

be the frozen Phase 5J component-share centroid and

\[
v_{500}
\]

the frozen canonical leading principal axis.

The model is the affine line

\[
\mu_{500}
+
\operatorname{span}(v_{500}).
\]

The Phase 5L higher-zero data must not contribute to refitting this line before primary replication metrics are scored.

---

# Higher-zero range

Generate critical-line zero ordinates with authoritative indices

\[
501\le j\le1500.
\]

Number of new ordinates:

\[
1000.
\]

Working precision:

\[
80
\]

decimal digits.

Every generated ordinate must satisfy

\[
\left|
\zeta\left(
\frac12+i\gamma_j
\right)
\right|
<
10^{-40}.
\]

The higher-zero CSV must store the authoritative global zero index.

---

# Counting-function convention

For a higher-zero ordinate range, define the empirical absolute count by

\[
N_D(t)
=
500
+
\#\{
\gamma_j:
501\le j\le1500,
\gamma_j\le t
\}.
\]

The additive offset 500 records the known number of ordinates preceding the generated block.

The response windows themselves use only zero ordinates with indices at least 501.

This is disjoint higher-zero window replication.

It is not a claim that zeta zeros are statistically independent samples.

---

# Frozen anchor grid

Authoritative anchor indices:

\[
550,
700,
850,
1000,
1150,
1300,
1400.
\]

Frozen relative widths:

\[
\eta
\in
\{
0.05,
0.10,
0.20,
0.50
\}.
\]

A frozen anchor-width pair enters the external replication population iff:

1. the upper window endpoint is contained in the generated index-501-through-1500 ordinate range;
2. the closed window contains at least 25 generated higher-zero ordinates;
3. H is reconstructed from the authoritative anchor zero index.

No window is selected based on its component-share geometry or frozen-axis residual.

---

# Frozen c-grid

For every eligible higher-zero window use

\[
c_{\mathrm{requested}}
=
1,2,\ldots,20.
\]

Set

\[
n
=
\max(
1,
\operatorname{nint}(c_{\mathrm{requested}}H)
).
\]

---

# External frozen-axis score

For higher-zero component-share vector

\[
x=(a,e,i),
\]

define projection onto the frozen first-500 affine principal line by

\[
\Pi_{500}x
=
\mu_{500}
+
\langle
x-\mu_{500},
v_{500}
\rangle
v_{500}.
\]

Define

\[
F_{\mathrm{external}}
=
1-
\frac{
\sum
\|x-\Pi_{500}x\|^2
}{
\sum
\|x-\mu_{500}\|^2
}.
\]

Define normalized residual

\[
\rho(x)
=
\frac{
\|x-\Pi_{500}x\|
}{
\|x-\mu_{500}\|
}
\]

when the denominator is nonzero.

---

# Frozen predictions

## P-EXT-001 — higher-zero numerical validation

PASS rule:

All 1000 generated ordinates, with indices exactly 501 through 1500, satisfy

\[
|\zeta(1/2+i\gamma_j)|<10^{-40}.
\]

---

## P-EXT-002 — frozen-axis external explained fraction

PASS rule:

\[
F_{\mathrm{external}}>0.95.
\]

This is the central external replication prediction.

---

## P-EXT-003 — small external point residual

PASS rule:

\[
\operatorname{median}\rho<0.20.
\]

---

## P-EXT-004 — widespread window-level replication

Compute frozen-axis explained fraction separately for every eligible higher-zero window.

PASS rule:

At least 80 percent of eligible windows satisfy

\[
F_{\mathrm{window}}>0.90.
\]

---

## P-EXT-005 — no severe higher-window collapse

PASS rule:

\[
\min F_{\mathrm{window}}>0.75.
\]

---

## P-EXT-006 — higher-zero refitted direction agrees with frozen axis

Only after P-EXT-002 through P-EXT-005 are scored, fit a principal axis to the higher-zero simplex cloud.

PASS rule:

\[
|
\langle
v_{\mathrm{high}},
v_{500}
\rangle
|
>
0.995.
\]

A secondary refit cannot rescue failed frozen-axis replication.

---

## P-EXT-007 — higher-zero cloud remains in-plane concentrated

For the two positive higher-zero simplex covariance eigenvalues

\[
\lambda_1\ge\lambda_2,
\]

PASS rule:

\[
\frac{\lambda_1}{\lambda_1+\lambda_2}>0.95.
\]

This is a secondary diagnostic.

---

# Failure-prevention rules

1. The first-500 centroid and principal axis are frozen before higher-zero share generation.

2. Phase 5L test points must not contribute to the primary affine line.

3. A higher-zero PCA refit is secondary and occurs only after primary metrics are scored.

4. Frozen anchor and eta grids are not changed after results.

5. Window inclusion depends only on endpoint containment and occupancy.

6. Disjoint higher-zero windows are not described as statistically independent zeta samples.

7. External replication of the component-share geometry is not an RH theorem.

8. No off-critical-zero constraint follows.

9. No RH consequence follows.

