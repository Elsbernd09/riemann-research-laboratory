# Phase 5K — Window-Level Principal-Axis Holdout Stability Report

## Status

COMPLETE.

## Objective

Test whether the Phase 5J near-one-dimensional component-share geometry survives when entire zero-height windows are excluded from principal-axis fitting.

The six primary folds held out three complete windows at a time.

A secondary leave-one-window-out audit held out each of the 18 dense windows individually.

All data remain inside the frozen first-500-critical-line-zero dataset.

This is not external replication.

No RH consequence is claimed.

---

# Primary training concentration

All six 15-window training populations retained leading in-plane explained fractions above

\[
0.99.
\]

Observed training fractions were approximately between

\[
0.99717
\]

and

\[
0.99781.
\]

P-HLD-001:

PASS.

Interpretation:

Deleting three whole windows did not destroy the near-one-dimensional training geometry.

---

# Three-window held-out explained fraction

Observed held-out explained fractions were approximately

\[
0.998751,
\]

\[
0.999198,
\]

\[
0.995958,
\]

\[
0.999287,
\]

\[
0.999285,
\]

and

\[
0.986027.
\]

Minimum:

\[
0.986027.
\]

Median:

\[
0.998031.
\]

Mean:

\[
0.996088.
\]

P-HLD-002:

PASS strongly.

P-HLD-003:

PASS strongly.

Interpretation:

A principal axis fitted without the held-out windows retained very high orthogonal explained fraction on unseen window blocks.

This is window-level internal holdout evidence.

It is not external dataset replication.

---

# Principal-axis direction stability

Minimum sign-invariant alignment between a training-fold principal axis and the full-sample axis:

\[
0.9999986487.
\]

P-HLD-004:

PASS strongly.

Interpretation:

The dominant component-share direction was highly stable under deletion of three complete windows.

The result does not establish an exact or asymptotic invariant direction.

---

# Point-level held-out residual

Global median normalized held-out residual:

\[
0.0402282.
\]

P-HLD-005:

PASS strongly.

Interpretation:

Typical held-out orthogonal line error was small relative to distance from the training centroid.

---

# Leave-one-window-out audit

Count of held-out windows with explained fraction above

\[
0.90:
\]

\[
18/18.
\]

Minimum leave-one-window-out explained fraction:

\[
0.971200.
\]

Median leave-one-window-out explained fraction:

\[
0.998868.
\]

P-HLD-006:

PASS strongly.

Interpretation:

No individual dense window was necessary to preserve high held-out principal-axis reconstruction within the first-500-zero dataset.

---

# Vertex-dominance guard

Primary held-out vertex-dominant fractions were approximately

\[
0.0833,
0.05,
0.2167,
0.0333,
0.5167,
0.
\]

Maximum:

\[
0.5167.
\]

The frozen P-HLD-007 rule required every primary fold to remain below

\[
0.40.
\]

P-HLD-007:

FAIL.

Interpretation:

The held-out populations are not uniformly protected against substantial vertex concentration.

One three-window test block was majority vertex-dominant.

The near-one-dimensional holdout result therefore must not be described as occurring exclusively in diffuse simplex-interior populations.

---

# Frozen scorecard

\[
\begin{array}{ll}
\mathrm{P\mbox{-}HLD\mbox{-}001} & \mathrm{PASS},\\
\mathrm{P\mbox{-}HLD\mbox{-}002} & \mathrm{PASS\ STRONGLY},\\
\mathrm{P\mbox{-}HLD\mbox{-}003} & \mathrm{PASS\ STRONGLY},\\
\mathrm{P\mbox{-}HLD\mbox{-}004} & \mathrm{PASS\ STRONGLY},\\
\mathrm{P\mbox{-}HLD\mbox{-}005} & \mathrm{PASS\ STRONGLY},\\
\mathrm{P\mbox{-}HLD\mbox{-}006} & \mathrm{PASS\ STRONGLY},\\
\mathrm{P\mbox{-}HLD\mbox{-}007} & \mathrm{FAIL}.
\end{array}
\]

---

# Main finite-data conclusion

The Phase 5J near-one-dimensional component-share geometry survives deterministic whole-window internal holdout testing strongly.

A principal axis learned without three complete test windows achieved median held-out explained fraction approximately

\[
99.8031\%.
\]

The worst primary fold still retained approximately

\[
98.6027\%
\]

held-out explained fraction.

All 18 leave-one-window-out test windows exceeded

\[
90\%
\]

explained fraction.

The dominant principal-axis direction was extremely stable across training subsets.

---

# Adversarial qualification

One primary held-out block had vertex-dominant fraction approximately

\[
51.67\%.
\]

Therefore the window-level result is not uniformly separated from vertex-concentrated simplex geometry.

The holdout success remains strong, but the vertex-dominance guard failed.

---

# Research decision

Further in-sample refinement of the first-500-zero dataset has diminishing value.

The next required pressure test is external dataset replication on a disjoint higher-zero dataset that was not used to derive, inspect, or fit the Phase 5J principal geometry.

The full first-500-zero principal axis must be frozen before the new dataset is analyzed.

---

# Restrictions

Window-level holdout is not external replication.

The 18 windows are drawn from one finite zero dataset.

No asymptotic persistence is proved.

No exact principal-line law is proved.

No off-critical-zero constraint is obtained.

No RH consequence follows.

