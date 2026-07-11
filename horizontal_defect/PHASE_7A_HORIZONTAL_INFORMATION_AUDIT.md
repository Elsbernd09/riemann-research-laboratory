# Phase 7A — Horizontal Information Audit

## Purpose

This phase starts the next research program.

The previous project showed that scalar zero-counting discrepancy response is horizontally blind. It can detect ordinates and multiplicities, but it cannot directly distinguish whether a zero is on the critical line.

The new goal is to classify which analytic objects actually see horizontal displacement

\[
\beta-\frac12
\]

for a nontrivial zero

\[
\rho=\beta+i\gamma.
\]

The Riemann Hypothesis is exactly the assertion that every nontrivial zero satisfies

\[
\beta-\frac12=0.
\]

Therefore any serious RH-relevant object must encode horizontal information.

---

# 1. Classification categories

We classify objects into six categories.

## Category A — Horizontally blind

An object is horizontally blind if it depends only on zero ordinates and multiplicities.

Examples:

\[
N(T)
\]

and scalar functions of the zero-counting staircase.

These objects cannot distinguish two zero multisets with identical ordinates but different real parts.

## Category B — Horizontally sensitive but cancellation-prone

An object is horizontally sensitive if it depends on

\[
\beta-\frac12.
\]

It is cancellation-prone if off-critical contributions can cancel after summation over zeros.

## Category C — Positivity-compatible

An object is positivity-compatible if it can be placed inside a nonnegative quadratic, energy, norm, or positive semidefinite form.

This category matters because RH is equivalent to several positivity principles.

## Category D — Explicit-formula compatible

An object is explicit-formula compatible if it can be related to primes or arithmetic data through a Weil/Guinand-type explicit formula.

This category matters because RH is not only a zero-side statement; it is tied to prime-side oscillation.

## Category E — Computationally testable

An object is computationally testable if finite truncations can be evaluated reliably and stress-tested against synthetic zero configurations.

## Category F — Potentially RH-relevant

An object is potentially RH-relevant only if it is horizontally sensitive, not trivially cancellation-destroyed, and either positivity-compatible or explicit-formula compatible.

---

# 2. Audit table

| Object | Horizontally blind? | Horizontally sensitive? | Positivity-compatible? | Explicit-formula compatible? | Computationally testable? | RH-relevant status |
|---|---:|---:|---:|---:|---:|---|
| \(N(T)\) | Yes | No | No | Yes, indirectly | Yes | Not sufficient |
| \(E(T)=N(T)-M(T)\) | Yes | No | No | Yes, indirectly | Yes | Not sufficient |
| \(S(T)\) through \(N(T)\) | Mostly yes | No direct beta data | No | Yes | Yes | Not sufficient |
| Li coefficients \(\lambda_n\) | No | Yes globally | Positivity criterion | Yes | Yes | Classical RH-equivalent |
| Weil quadratic form | No | Yes | Yes | Yes | Partly | Classical RH-equivalent |
| Single-zero Li horizontal contrast | No | Yes | Not globally positive | Limited | Yes | Useful diagnostic |
| Linear Li filters | No | Yes | Generally cancellation-prone | Possibly | Yes | Obstructed |
| Squared horizontal contrast | No | Yes | Yes on single quartet | Hard globally | Yes | Candidate but aggregation issue |
| Defect-weighted zero measure | No | Yes | Yes by construction | Not directly | Synthetic only | Definitional, not analytic |
| Rational Gram form of Li susceptibility | No | Yes in kernel | Indefinite rank two | Limited | Yes | Diagnostic, not positivity proof |

---

# 3. Key obstruction from prior phases

Scalar counting data cannot prove RH because it forgets horizontal position.

If two zero configurations have the same ordinates and multiplicities but different real parts, then

\[
N(T)
\]

is identical for both.

Therefore any theorem depending only on \(N(T)\), \(E(T)\), or their ordinary integrals cannot imply RH.

This is the horizontal-blindness obstruction.

---

# 4. First serious target

The next serious target is not to prove RH.

The next serious target is:

\[
\boxed{
\text{Find a horizontal-defect functional that is explicit-formula compatible and resists cancellation.}
}
\]

A candidate functional should satisfy four requirements:

1. It must detect

\[
\left(\beta-\frac12\right)^2.
\]

2. It must aggregate over zeros without arbitrary sign cancellation.

3. It must have a route to an arithmetic-side expression.

4. It must have finite truncations that can be tested against synthetic off-critical zero configurations.

---

# 5. Candidate research directions

## Direction 1 — Quadratic horizontal defect energy

Study expressions of the form

\[
\mathcal D_\phi
=
\sum_\rho
\phi(\gamma_\rho)
\left(\beta_\rho-\frac12\right)^2.
\]

Problem:

This is definitionally RH-equivalent if \(\phi>0\), but it is not automatically explicit-formula compatible.

Research question:

Can any natural \(\phi\) arise from a Weil-positive test function?

## Direction 2 — Li-coordinate radial defect

Use

\[
w(\rho)=1-\frac1\rho.
\]

Critical-line zeros satisfy

\[
|w(\rho)|=1.
\]

Off-critical zeros satisfy

\[
|w(\rho)|\ne1.
\]

Research question:

Can one create an explicit-formula-compatible energy measuring

\[
\log^2 |w(\rho)|
\]

without cancellation?

## Direction 3 — Weil quadratic finite-rank truncation

Weil positivity is classical and RH-equivalent.

Research question:

Can finite-rank truncations be chosen so that off-critical zeros create a detectable negative direction with quantitative convergence?

## Direction 4 — Obstruction theorem for linear filters

Prior phases suggested that fixed linear Li filters cannot universally detect horizontal defect without cancellation.

Research question:

Can we prove a general impossibility theorem for finite linear horizontal-defect filters?

---

# 6. Phase 7A conclusion

The project should move away from scalar zero-counting response and toward horizontal-defect detection.

The next theorem target should be one of:

1. a positive result constructing a usable horizontal-defect energy;
2. a negative result proving a broad obstruction for linear filters;
3. a finite-rank Weil truncation theorem;
4. a rigorous synthetic-zero testbed for horizontal-defect functionals.

The most realistic next target is the obstruction theorem for linear filters.

