# Paper Theorem Dependency Map

## Central result

### Theorem A

\[
R_{\mathrm{int}}(n;H,\eta)
=
O_{K,\eta}
\left(
\frac{\log H}{H^3}
\right).
\]

Status:

PROVED IN PROJECT.

RH assumption:

NONE.

---

# Dependency graph

## Classical dependency C1

Riemann-von Mangoldt:

\[
E(t)
=
S(t)+O(1/t).
\]

Status:

CLASSICAL.

Used for:

window mean and centered primitive.

---

## Classical dependency C2

Unconditional first primitive:

\[
S_1(t)=O(\log t).
\]

Status:

CLASSICAL.

Used for:

\[
\overline E
=
O(\log H/H)
\]

and

\[
\|F\|_\infty
=
O(\log H).
\]

---

## Project dependency P1

Matched-scale susceptibility:

\[
t^2\chi_n(t)
=
\Psi_{Li}(n/t)
+
O(t^{-2}).
\]

Status:

PROVED IN PROJECT.

Used for:

endpoint scale

\[
\chi_n=O(H^{-2}).
\]

---

## Project dependency P2

Corrected second derivative:

\[
t^4\chi_n''(t)
=
K_{Li}^{(2)}(n/t)
+
O(t^{-2}).
\]

Status:

PROVED IN PROJECT.

Used for:

\[
\int_H^B
|\chi_n''(t)|dt
=
O(H^{-3}).
\]

Historical warning:

The first displayed explicit profile was algebraically false.

The failed profile remains recorded as a failed claim.

The corrected profile is

\[
K_{Li}^{(2)}(q)
=
2q^4\cos q
+
24q^3\sin q
-
72q^2\cos q
-
48q\sin q.
\]

---

## Project dependency P3

Centered primitive:

\[
F(t)
=
\int_H^t
(E(s)-\overline E)ds.
\]

Exact secant identity:

\[
F(t)
=
A(t)-A(H)
-
\frac{t-H}{B-H}
\left(
A(B)-A(H)
\right).
\]

Status:

PROVED IN PROJECT as an elementary specialization.

Classical ancestry:

antiderivative and integration-by-parts mechanism.

---

## Project dependency P4

Exact response transfer:

\[
R_{\mathrm{int}}
=
-\overline E
\left(
\chi_n(B)-\chi_n(H)
\right)
+
\int_H^B
F(t)\chi_n''(t)dt.
\]

Status:

PROVED IN PROJECT.

---

# Proof assembly

C1 + C2 imply

\[
\overline E
=
O(\log H/H)
\]

and

\[
\|F\|_\infty
=
O(\log H).
\]

P1 implies

\[
|\chi_n(B)-\chi_n(H)|
=
O(H^{-2}).
\]

P2 implies

\[
\int_H^B|\chi_n''|
=
O(H^{-3}).
\]

P4 then gives

\[
R_{\mathrm{int}}
=
O(\log H/H^3).
\]

---

# RH refinement

Replace C2 by the classical conditional input

\[
S_1(t)
=
O
\left(
\frac{\log t}
{(\log\log t)^2}
\right).
\]

All project kernel dependencies remain unchanged.

Result:

\[
R_{\mathrm{int}}
=
O
\left(
\frac{\log H}
{H^3(\log\log H)^2}
\right).
\]

---

# Claims not required for Theorem A

Theorem A does not depend on:

- Phase 4 blind-scale resonance;
- finite-zero PCA;
- Phase 5L external numerical replication;
- Weil positivity;
- Hardy spaces;
- Li generating-function radius;
- signed Gram inertia;
- horizontal-defect measures;
- RH.

This separation must remain explicit in the paper.

