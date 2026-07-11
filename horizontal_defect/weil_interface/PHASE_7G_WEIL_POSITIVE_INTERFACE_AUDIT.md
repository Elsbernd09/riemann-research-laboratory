# Phase 7G — Weil-Positive Interface Audit

## Purpose

Phase 7F constructed a positive quadratic Li-filter detector:

\[
Q_{1,2}(u,\theta)
=
\Delta_1(u,\theta)^2
+
\Delta_2(u,\theta)^2.
\]

It is strictly positive for every nonzero horizontal displacement parameter \(u\).

However, positivity alone is not enough.

The real question is whether such positivity can interface with classical Weil-positive machinery.

This phase audits that interface.

This phase does not prove RH.

It does not claim a new Weil criterion.

---

# 1. Classical interface principle

The classical explicit formula naturally relates arithmetic information to linear sums over zeros of test functions:

\[
\sum_\rho h(\rho).
\]

Weil positivity upgrades this into a quadratic positivity statement over test functions.

Therefore a useful horizontal-defect detector must eventually connect to one of the following:

1. a linear zero-side test function;
2. a Weil-positive quadratic form;
3. a limiting family of test functions;
4. an operator whose positivity is equivalent to RH;
5. an arithmetic-side quantity that can force vanishing.

---

# 2. Why the quadratic detector is not automatically enough

The Phase 7F detector has the form

\[
Q_{1,2}
=
\Delta_1^2+\Delta_2^2.
\]

This is positive, but it is quadratic in zero-side features.

Classical explicit formula terms are usually linear in zeros:

\[
\sum_\rho h(\rho).
\]

Thus the expression

\[
\sum_\rho Q_{1,2}(\rho)
\]

is not automatically a standard explicit-formula object.

The positivity is local and geometric.

The missing bridge is arithmetic.

---

# 3. Three possible bridges

## Bridge A — Exact Weil representation

Find a Weil test function or family of test functions whose quadratic form equals the horizontal-defect energy.

Target form:

\[
\mathcal W(f)
=
\sum_\rho Q(\rho)
+
\text{controlled classical terms}.
\]

Status:

Open.

Risk:

May reduce to already-known Weil positivity theory.

## Bridge B — Comparison theorem

Prove that a Weil-positive quadratic form dominates a horizontal-defect energy:

\[
\mathcal W(f)
\ge
c
\sum_\rho
\phi(\gamma_\rho)
D_{\mathrm{rad}}(\rho).
\]

Status:

Open.

Risk:

A uniform positive lower bound may fail because of phase, localization, or test-function constraints.

## Bridge C — Finite-rank negative-direction detection

Given a synthetic off-critical quartet, construct a finite-dimensional test subspace where the Weil quadratic form detects a negative direction.

Status:

Most computationally accessible.

Risk:

This may reproduce known finite-truncation behavior without new theory.

---

# 4. Interface table

| Object | Positive? | Horizontal-sensitive? | Explicit-formula compatible? | Current status |
|---|---:|---:|---:|---|
| \(D_{\mathrm{rad}}\) | Yes | Yes | Not established | Diagnostic |
| \(Q_{1,2}\) | Yes | Yes | Not established | Quadratic detector |
| Linear Li filters | No universal positivity | Yes | More plausible | Obstructed |
| Weil quadratic form | Yes under RH / equivalent framework | Yes globally | Yes | Classical anchor |
| Finite-rank Weil truncations | Mixed | Potentially | Partly | Best next testbed |

---

# 5. Main conclusion

The current project has crossed from scalar zero-counting into horizontal-defect detection.

It has found:

1. a negative theorem for linear filters;
2. a positive quadratic local detector;
3. an aggregation barrier;
4. a no-go comparison between radial defect and finite linear filters.

The remaining bridge is:

\[
\boxed{
\text{Weil-positive or explicit-formula-compatible representation.}
}
\]

Without that bridge, the detector remains diagnostic.

---

# 6. Next theorem target

The next target should be finite-rank Weil negative-direction detection.

Working question:

Given a synthetic off-critical zero quartet, can a finite-dimensional quadratic test space detect an induced negative direction?

This is not an RH proof.

It is a controlled laboratory version of classical Weil positivity.

