# Phase 7C — Quadratic Li-Coordinate Defect Energy

## Purpose

Phase 7B proved that finite linear Li horizontal-defect filters cannot be universal positive detectors at leading order.

The next natural move is quadratic.

This phase studies a positive single-quartet horizontal-defect energy based on the Li coordinate

\[
w(\rho)=1-\frac1\rho.
\]

This does not prove RH.

It constructs and validates a positive local detector of horizontal displacement.

---

# 1. Li-coordinate radial defect

Let

\[
\rho=\beta+i\gamma.
\]

Define

\[
w(\rho)=1-\frac1\rho.
\]

Write

\[
w=e^{u+i\theta}.
\]

Then

\[
u=\log |w|.
\]

Compute

\[
|w|^2
=
\left|1-\frac1\rho\right|^2
=
\frac{(\beta-1)^2+\gamma^2}{\beta^2+\gamma^2}.
\]

Therefore

\[
|w|=1
\]

if and only if

\[
(\beta-1)^2+\gamma^2
=
\beta^2+\gamma^2.
\]

This simplifies to

\[
\beta=\frac12.
\]

Thus

\[
u=0
\]

if and only if the zero lies on the critical line.

---

# 2. Defect energy

Define the Li-coordinate radial defect energy

\[
D_{\mathrm{rad}}(\rho)
=
\left(\log |1-1/\rho|\right)^2.
\]

Then

\[
D_{\mathrm{rad}}(\rho)\ge0.
\]

Also,

\[
D_{\mathrm{rad}}(\rho)=0
\]

if and only if

\[
\Re(\rho)=\frac12.
\]

Therefore \(D_{\mathrm{rad}}\) is a faithful single-zero horizontal-displacement detector.

---

# 3. Relation to horizontal displacement

Let

\[
x=\beta-\frac12.
\]

Then

\[
\beta=\frac12+x.
\]

We have

\[
|w|^2
=
\frac{(\beta-1)^2+\gamma^2}{\beta^2+\gamma^2}
=
\frac{(x-\frac12)^2+\gamma^2}{(x+\frac12)^2+\gamma^2}.
\]

Therefore

\[
u
=
\frac12
\log
\left(
\frac{(x-\frac12)^2+\gamma^2}
{(x+\frac12)^2+\gamma^2}
\right).
\]

For small \(x\), Taylor expansion gives

\[
u
=
-\frac{x}{\gamma^2+\frac14}
+
O(x^3).
\]

Hence

\[
D_{\mathrm{rad}}(\rho)
=
u^2
=
\frac{x^2}{(\gamma^2+\frac14)^2}
+
O(x^4).
\]

Thus the radial Li-coordinate defect detects horizontal displacement quadratically.

---

# 4. Single-quartet energy

For a symmetric quartet with displacement parameter \(u\), define

\[
Q(u)=u^2.
\]

Then

\[
Q(u)\ge0
\]

and

\[
Q(u)=0
\]

if and only if

\[
u=0.
\]

This avoids the phase cancellation problem from Phase 7B because the phase \(\theta\) does not appear.

---

# 5. Main theorem

## Theorem

For every nontrivial zero candidate

\[
\rho=\beta+i\gamma
\]

with \(\gamma\ne0\), the energy

\[
D_{\mathrm{rad}}(\rho)
=
\left(\log |1-1/\rho|\right)^2
\]

satisfies

\[
D_{\mathrm{rad}}(\rho)\ge0.
\]

Moreover,

\[
D_{\mathrm{rad}}(\rho)=0
\]

if and only if

\[
\beta=\frac12.
\]

For small horizontal displacement

\[
x=\beta-\frac12,
\]

one has

\[
D_{\mathrm{rad}}(\rho)
=
\frac{x^2}{(\gamma^2+\frac14)^2}
+
O(x^4).
\]

## Proof

The nonnegativity follows because \(D_{\mathrm{rad}}\) is a square.

The zero condition follows from

\[
|1-1/\rho|=1
\]

which is equivalent to

\[
(\beta-1)^2+\gamma^2
=
\beta^2+\gamma^2.
\]

Expanding gives

\[
\beta^2-2\beta+1
=
\beta^2,
\]

so

\[
\beta=\frac12.
\]

The small-displacement expansion follows from the expression

\[
u(x)
=
\frac12
\log
\left(
\frac{(x-\frac12)^2+\gamma^2}
{(x+\frac12)^2+\gamma^2}
\right).
\]

This function is odd in \(x\). Its first derivative at zero is

\[
u'(0)
=
-\frac{1}{\gamma^2+\frac14}.
\]

Therefore

\[
u(x)
=
-\frac{x}{\gamma^2+\frac14}
+
O(x^3).
\]

Squaring gives

\[
u(x)^2
=
\frac{x^2}{(\gamma^2+\frac14)^2}
+
O(x^4).
\]

This proves the theorem.

---

# 6. Obstruction still remaining

This energy is positive and faithful on individual zeros.

However, this does not yet make it an RH proof tool.

The hard unresolved question is:

\[
\boxed{
\text{Can this positive radial defect be connected to an explicit arithmetic-side formula?}
}
\]

Without such a bridge, the object is a diagnostic horizontal-defect measure, not a new RH criterion.

---

# 7. Phase conclusion

Phase 7C gives a clean positive detector of horizontal displacement in Li coordinates.

It solves the phase-cancellation problem locally by replacing linear filters with a quadratic radial energy.

It does not solve the aggregation problem.

It does not solve the explicit-formula compatibility problem.

It does not prove RH.

