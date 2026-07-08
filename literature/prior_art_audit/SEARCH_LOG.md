# Prior-Art Search Log

## Rules

Every search campaign should record:

- date;
- audit question identifier;
- exact query;
- search system or database;
- candidate sources opened;
- sources retained;
- sources rejected;
- reason for rejection.

Do not report "no prior art found" without preserving the search queries and candidate-source trail.

---


## Campaign Q4-GS-001

**Date:** 2026-07-07

**Audit question:** Q4 — Li coefficient response to zero displacement

**Platform:** Google Scholar

**Scope:** First two pages of results for each query.

### Queries

1. `"Li coefficients" "off critical line" zeros`
2. `"Li coefficients" perturbation zeros`
3. `"Li criterion" "off critical zeros" asymptotic`
4. `"Li coefficients" "individual zero contribution"`
5. `"Keiper Li coefficients" "off critical line"`
6. `"Li coefficients" "Riemann hypothesis violation" zeros`
7. `"Li coefficients" sensitivity zeros`
8. `"variation of Li coefficients" zeros`

**Selection rule:**

Retain papers with explicit individual-zero analysis, off-critical-zero asymptotics, variation with zero location, perturbation language, or quantitative RH-violation effects on Li coefficients.

**Status:** SEARCH IN PROGRESS


### Q4-GS-001 preliminary result

Retained sources:

- Smajlović (2010), Journal of Number Theory.
- Palojärvi (2020), PhD thesis.
- Mazhouda and Smajlović (2017), Functiones et Approximatio.
- Bucur, Ernvall-Hytönen, Odžak, and Smajlović (2016), LMS Journal of Computation and Mathematics.
- Johansson, high-precision Hurwitz zeta and Keiper-Li computation.

Rejected candidates:

- Structured-prime stabilization and forward-prediction paper: rejected as not mathematically responsive to Q4.
- Zero-inflated count-data variable-selection paper: rejected as keyword noise unrelated to zeta zeros.

Preliminary conclusion:

Existing literature substantially overlaps with broad Li zero-location sensitivity, reflection pairing, and critical-line phase geometry.

No source reviewed in this campaign was found to contain the project's specific symmetry-preserving second zero-location variation or coupled n/gamma susceptibility profile.

Highest preliminary grade:

PA-3.

Status:

GOOGLE SCHOLAR PRELIMINARY REVIEW COMPLETE.

Follow-up required:

1. inspect Voros source cited by Smajlović for off-critical-zero induced Li oscillations;
2. inspect Freitas on generalized Li criteria and paired rho, 1-rho terms;
3. inspect Bombieri-Lagarias multiset generalization;
4. run targeted exact-object searches for second variation, Taylor expansion in beta, and derivatives with respect to zero position.

## Campaign Q4-BC-001

**Date:** 2026-07-07

**Audit question:** Q4 — Li coefficient response to zero displacement

**Campaign type:** Targeted backward-citation PA-4 strike search

### Target 1

A. Voros,
"Sharpenings of Li's criterion for the Riemann Hypothesis,"
Math. Phys. Anal. Geom. 9 (2006), 53-63.

Search target:

Explicit dependence of individual off-critical-zero contributions on zero location; Taylor or differential response in real part; coupled n/height asymptotics.

### Target 2

P. Freitas,
"A Li-type criterion for zero-free half planes of Riemann's zeta function,"
J. London Math. Soc. 73(2) (2006), 399-414.

Search target:

Expansion of reflection-paired zero contributions around the critical line; derivatives or Taylor response with respect to horizontal zero displacement.

### Target 3

E. Bombieri and J. C. Lagarias,
"Complements to Li's Criterion for the Riemann Hypothesis,"
J. Number Theory 77 (1999), 274-287.

Search target:

Variation or sensitivity of Li-type sums under perturbation of a multiset of complex numbers.

### Target 4

Droll and related modified/tau-Li literature.

Search target:

Individual-zero real-part dependence, perturbation, Taylor expansion in zero location, or n/height coupled asymptotics.

### PA-4 trigger

A source triggers PA-4 review if it contains a materially equivalent version of one or more of:

1. second variation of the fixed Li zero kernel with respect to horizontal zero location;
2. Taylor expansion at Re(rho)=1/2 of a reflection-symmetric finite zero-orbit contribution;
3. horizontal-versus-vertical symmetric four-zero response;
4. susceptibility proportional to 2 Re f_n''(1/2+i gamma);
5. coupled n/gamma scaling of that response.

**Status:** SEARCH IN PROGRESS


### Q4-BC-001 result

Voros:

PA-3.

Established large-n individual off-critical-zero asymptotics and explicit coupling between Li index and zero geometry.

Freitas:

PA-3.

Established continuous parameter response and differential equations for a parameterized Li-type coefficient family. Differentiated criterion parameter, not zero coordinates.

Bombieri-Lagarias:

PA-3.

Established arbitrary complex multiset framework and functional-equation symmetry context.

Droll:

PA-3.

Established generalized tau-Li criteria and multiset-based zero-free-region analysis.

Modified Li criterion paper:

PA-3 with very strong structural overlap.

The shifted product F(s-a)F(s+a) realizes exactly the horizontal quartet geometry H_{a,gamma} when the baseline function has a critical-line conjugate zero pair.

Generalized Li asymptotics:

PA-3.

Established large-n asymptotics for tau-Li coefficients and shifted products.

PA-4 trigger search:

No second zero-coordinate variation identified.

No critical-line orbit Taylor expansion in displacement identified.

No horizontal-versus-vertical four-zero response identified.

No 2 Re f_n'' zero-location susceptibility identified.

No coupled n/gamma scaling of that second response identified.

Highest grade:

PA-3.

Status:

TARGETED BACKWARD-CITATION STRIKE SEARCH COMPLETE.

Further action:

Search the exact mathematical combination rather than broad Li sensitivity language.

## Campaign Q4-EXACT-001

**Date:** 2026-07-08

**Audit question:** Q4 — narrowed Li zero-coordinate response question

**Campaign type:** Exact-combination PA-4 strike search

## Surviving originality-sensitive object

The infinitesimal second variation of the fixed Li zero kernel under symmetry-preserving horizontal zero displacement, its quarter-turn horizontal-versus-vertical contrast, and the simultaneous n/gamma -> c scaling of that response.

## Trigger A — Shift derivative of Li coefficients

Search for derivatives with respect to a in Li coefficients attached to shifted products such as

\[
F(s-a)F(s+a).
\]

Primary danger:

\[
\left.
\frac{d^2}{da^2}
\lambda_n(F(s-a)F(s+a))
\right|_{a=0}.
\]

## Trigger B — Zero-coordinate variation

Search for derivatives, Hessians, Taylor expansions, or second variations of Li-type sums with respect to rho, Re(rho), beta, or finite multiset coordinates.

## Trigger C — Horizontal versus vertical deformation

Search for comparisons between real symmetric shifts and imaginary symmetric shifts, including

\[
F(s-a)F(s+a)
\]

versus

\[
F(s-ia)F(s+ia).
\]

## Trigger D — Coupled n/height scaling

Search for simultaneous asymptotics in Li index and zero height, especially

\[
n/\gamma\to c.
\]

## Trigger E — Logarithmic shift variation

Search for symmetric-shift second derivatives

\[
\left.
\partial_a^2
\log[F(s-a)F(s+a)]
\right|_{a=0}
=
2(\log F)''(s)
\]

when explicitly connected to Li or zero-response questions.

## PA-4 rule

A paper receives PA-4 review if it contains a materially equivalent form of the project's surviving combination.

Individual standard ingredients do not trigger PA-4 by themselves.

**Status:** SEARCH IN PROGRESS


### Q4-EXACT-001 result

Shifted-product Li literature:

PA-3.

The horizontal quartet is exactly realized by zeros of F(s-a)F(s+a), but no second derivative of Li coefficients with respect to a at a=0 was identified.

Voros 2022:

PA-3.

The index required to signal an RH-violating zero is quantitatively related to zero height. Therefore n-versus-zero-height sensitivity is prior-art territory.

No quadratic zero-coordinate response profile under n/gamma -> c was identified.

Maślanka 2022:

PA-3.

Explicitly analyzes how off-critical displacement changes the modulus of an individual Li zero contribution and why high zeros require very large Li indices for detection.

No second zero-coordinate variation identified.

Coffey:

PA-2.

Zero sums and derivative identities reviewed. A horizontal deviation parameter epsilon appears in zero estimates, but no Hessian or second variation in epsilon was identified.

Generalized Li asymptotic literature:

PA-2 to PA-3.

No project-specific second response profile identified.

Contemporary zero-response preprint:

PA-2.

Uses logarithmic derivative derivatives and perturbation stability but is not a Li zero-coordinate response theory.

Several broad-search sources rejected as keyword noise.

PA-4 triggers found:

0 / 5.

Highest grade:

PA-3.

Status:

EXACT-COMBINATION STRIKE SEARCH COMPLETE.

Further narrowed surviving object:

Fixed-Li-kernel quadratic zero-coordinate response plus quarter-turn realization plus explicit coupled n/gamma limiting profile.
