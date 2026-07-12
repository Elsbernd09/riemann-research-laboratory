# Phase B11 — Interval Candidate Arithmetic Entry

## Purpose

Phase B10 created a prototype floating-point arithmetic entry:

\[
M_{00}^{arith}.
\]

Phase B11 upgrades it to:

\[
\texttt{INTERVAL\_CANDIDATE}.
\]

This is not yet certified.

It is a conservative interval wrapper around the prototype value, with explicit unresolved error gates.

---

# 1. Entry target

\[
M_{00}^{arith}
=
T[\phi_0 \vee \overline{\phi_0}]
\]

under Bombieri–Lagarias normalization.

The entry uses the source-normalized constant term:

\[
-(\log\pi+\gamma)f(1).
\]

---

# 2. Interval candidate status

The new status is:

\[
\texttt{INTERVAL\_CANDIDATE}.
\]

This means:

1. an interval value exists;
2. the interval is conservative by design;
3. the error terms are not rigorously derived;
4. the entry is not certified;
5. the entry cannot be used in a certified arithmetic matrix.

---

# 3. Conservative interval

Given a prototype value:

\[
v_{\mathrm{proto}},
\]

Phase B11 creates a wide interval:

\[
[v_{\mathrm{proto}}-R,\ v_{\mathrm{proto}}+R].
\]

The radius \(R\) is chosen conservatively from component magnitudes and a minimum safety floor.

This is a candidate interval, not a proof-bound interval.

---

# 4. Missing certification gates

The interval is not certified because the following are not rigorously bounded:

1. quadrature error;
2. convolution approximation error;
3. archimedean singularity handling;
4. floating-point rounding error;
5. basis smoothness error;
6. pole-constraint error;
7. source-normalization transformation risk.

---

# Theorem B11.1 — interval candidate is not certified

An entry with status

\[
\texttt{INTERVAL\_CANDIDATE}
\]

cannot be used as a certified interval entry.

## Proof

By Phase B8, a certified entry must have status:

\[
\texttt{CERTIFIED\_INTERVAL\_ENTRY}.
\]

The status:

\[
\texttt{INTERVAL\_CANDIDATE}
\]

is distinct.

Therefore an interval candidate is not certified.

\[
\square
\]

---

# Theorem B11.2 — certified matrix cannot use interval candidates

A matrix containing an interval-candidate entry cannot be labeled certified.

## Proof

By Phase B8, a certified matrix requires every entry to be a certified interval entry.

An interval candidate is not a certified interval entry by Theorem B11.1.

Therefore any matrix containing such an entry is not certified.

\[
\square
\]

---

# 5. What this phase achieves

This phase creates the first interval-valued arithmetic entry candidate.

It is a major engineering step because the entry now has:

1. source metadata;
2. corrected normalization;
3. prototype value;
4. candidate interval;
5. unresolved certification gates;
6. explicit non-certification status.

---

# 6. Next target

Phase B12 should audit the error gates one by one and decide which can become rigorous.

The goal is not to pretend the interval is certified.

The goal is to identify the shortest path from:

\[
\texttt{INTERVAL\_CANDIDATE}
\]

to:

\[
\texttt{CERTIFIED\_INTERVAL\_ENTRY}.
\]

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a breakthrough.

This phase does not prove novelty.

This phase does not compute a certified arithmetic entry.

Exact audit strings:

PHASE_B11_INTERVAL_CANDIDATE_ENTRY_COMPLETE

M_00_ARITH_INTERVAL_CANDIDATE_CREATED

INTERVAL_CANDIDATE_STATUS_USED

CONSERVATIVE_INTERVAL_WRAPPER_CREATED

ERROR_GATES_RECORDED

INTERVAL_CANDIDATE_ENTRY_NOT_CERTIFIED

CERTIFIED_MATRIX_CANNOT_USE_INTERVAL_CANDIDATE

BREAKTHROUGH_NOT_ACHIEVED

READY_FOR_PHASE_B12_CERTIFIED_ERROR_BOUND_AUDIT

