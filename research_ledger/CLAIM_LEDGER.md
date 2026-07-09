# Claim Ledger

Every mathematically important statement must be assigned exactly one status.

## Allowed statuses

### KNOWN THEOREM
A published or standard mathematical result. Assumptions and source must be recorded.

### KNOWN CONJECTURE
A recognized unresolved mathematical claim.

### EQUIVALENT CRITERION
A statement rigorously known to be equivalent to the Riemann Hypothesis or another identified conjecture.

### HEURISTIC
An analogy, model, probabilistic expectation, or informal explanatory mechanism.

### COMPUTATIONAL OBSERVATION
A finite numerical result produced under explicitly recorded computational conditions.

### PROJECT CONJECTURE
A precise mathematical claim formulated during this project after prior-art investigation.

### PROVED IN PROJECT
A statement accompanied by a complete written proof that has survived adversarial review.

### FAILED CLAIM
A proposed claim invalidated by a counterexample, hidden assumption, circularity, or proof failure.

---

# Active Claims

## CL-0001

**Status:** KNOWN CONJECTURE

**Statement:** Every nontrivial zero of the Riemann zeta function has real part 1/2.

**Name:** Riemann Hypothesis

**Project claim?:** No.

---

## CL-0002

**Status:** HEURISTIC

**Statement:** Quantitative comparison of the responses of multiple RH-related diagnostics to controlled symmetric zero perturbations may expose useful differences in their finite-scale detection behavior.

**Project claim?:** No theorem is currently asserted.

**Failure conditions:** The diagnostics may encode equivalent information without a useful quantitative distinction; the proposed response scales may already be known; or synthetic perturbations may fail to preserve enough analytic structure to model a meaningful comparison.

---

## CL-0003

**Status:** FAILED CLAIM PREVENTION RULE

**Statement:** Verification of finitely many critical-line zeros does not prove the Riemann Hypothesis.

**Purpose:** Prevent finite-to-infinite extrapolation.

---

## CL-0004

**Status:** FAILED CLAIM PREVENTION RULE

**Statement:** Numerical positivity of finitely many Li coefficients does not establish positivity for all Li coefficients.

**Purpose:** Prevent finite computation from being mislabeled as a universal theorem.

---

## CL-0005

**Status:** KNOWN THEOREM

**Statement:** The completed Riemann xi-function satisfies the functional-equation symmetry xi(s) = xi(1-s) and conjugation symmetry xi(conjugate(s)) = conjugate(xi(s)).

**Project claim?:** No.

---

## CL-0006

**Status:** KNOWN THEOREM

**Statement:** A generic nonreal zero beta + i gamma of xi generates the symmetry orbit consisting of rho, 1-rho, conjugate(rho), and 1-conjugate(rho), with coincidences possible on symmetry loci.

**Project claim?:** No.

---

## CL-0007

**Status:** HEURISTIC

**Statement:** A finite factor-ratio perturbation replacing selected zero factors may provide a useful controlled model for comparing the finite-scale response of zero-sensitive RH diagnostics.

**Project claim?:** Not currently a theorem.

**Largest danger:** The resulting synthetic entire or meromorphic model may not preserve the arithmetic structures required by some diagnostics.

---

## CL-0008

**Status:** FAILED CLAIM PREVENTION RULE

**Statement:** A symmetry-preserving synthetic zero multiset is not automatically the zero set of a modified zeta function with an Euler product, Dirichlet series, or prime interpretation.

**Purpose:** Prevent synthetic analytic models from being mislabeled as arithmetic zeta functions.

---

## CL-0009

**Status:** HEURISTIC

**Statement:** Symmetry-preserving double-orbit splitting suppresses odd powers of the horizontal displacement parameter in analytic zero-kernel responses, making quadratic response a natural local sensitivity scale.

**Project claim?:** The Taylor mechanism is standard. Its usefulness for comparing RH diagnostics is unproved.

---

## CL-0010

**Status:** PROJECT CONJECTURE CANDIDATE — NOT YET ACTIVATED

**Statement:** Distinct RH-related zero diagnostics may exhibit quantitatively different asymptotic susceptibility scales under signed symmetry-breaking response.

**Reason not activated:** Diagnostic families, normalization conventions, and prior art have not yet been sufficiently specified.

---

## CL-0011

**Status:** FAILED CLAIM

**Statement:** Replacing one simple critical-line conjugate pair by one generic off-line quartet defines a perturbative response that vanishes as the displacement tends to zero.

**Failure:** The quartet converges as a multiset to a doubled critical-line pair. A pair-to-quartet response therefore contains a zeroth-order multiplicity jump.

**Disposition:** Model A rejected as the primary perturbation model.

---

## CL-0012

**Status:** FAILED CLAIM

**Statement:** Raw quadratic susceptibilities from unrelated diagnostic kernels can be ranked directly as universal measures of off-critical sensitivity.

**Failure:** Native kernel scale and normalization may differ across diagnostic families.

**Disposition:** Direct universal ranking by raw susceptibility rejected.

---

## CL-0013

**Status:** FAILED CLAIM

**Statement:** Dividing susceptibility by the absolute baseline pair contribution produces an intrinsic sensitivity metric.

**Failure:** Additive shifts of the kernel preserve the second derivative and hence susceptibility while changing the proposed denominator.

**Disposition:** Baseline-magnitude normalization rejected as intrinsic.

---

## CL-0014

**Status:** HEURISTIC

**Statement:** Separating native response, response orientation, derivative-shape geometry, and logarithmic curvature may provide a more honest comparison of RH-related diagnostic kernels than a single universal sensitivity scalar.

**Project claim?:** Not currently a theorem.

**Required next step:** Apply the formalism to a mathematically standard diagnostic kernel and determine whether the decomposition yields nontrivial structure.

---

## CL-0015

**Status:** PROVED IN PROJECT

**Statement:** For the individual Li kernel, if gamma tends to infinity and n/gamma tends to c > 0, then gamma^2 times the quadratic susceptibility tends to -2c(c cos(c) + 2 sin(c)).

**Proof status:** The scaling limit follows from the exact susceptibility formula, the limit gamma theta_gamma -> 1, and n/gamma -> c. The exact derivative formula has been independently checked symbolically and numerically.

**Originality status:** Unresolved. PROVED IN PROJECT means the project has established the statement internally; it does not mean the statement is novel in the literature.

---

## CL-0016

**Status:** COMPUTATIONAL OBSERVATION PREVENTION RULE

**Statement:** Any future numerical scaling collapse matching the Li susceptibility profile is validation of the derived formula, not by itself evidence of a new theorem or progress toward RH.

**Purpose:** Prevent reproduction of an analytically derived limit from being marketed as numerical discovery.

---

## CL-0017

**Status:** FAILED CLAIM

**Statement:** The initial SymPy factor-and-together validator was sufficient to decide the symbolic derivative identity.

**Failure:** The simplification route failed to expose an exact cancellation involving symbolic integer exponents.

**Disposition:** Validator repaired with stronger symbolic simplification and fixed-integer adversarial fallback.

---

## CL-0018

**Status:** FAILED CLAIM

**Statement:** The default mpmath `almosteq` criterion was an appropriate automated-test implementation of the Phase 1B numerical validation standard.

**Failure:** Its implicit tolerance was inconsistent with the explicitly declared relative-error threshold of 10^-70.

**Disposition:** Automated tests now use the explicit project threshold.

---

## CL-0019

**Status:** FAILED CLAIM

**Statement:** The Li-type derivative functional applied to the single factor \(1-s/\rho\) produces the project kernel \(1-(1-1/\rho)^n\) at the same zero \(\rho\).

**Failure:** The derivative functional produces \(1-(1-1/\rho)^{-n}\).

**Disposition:** Termwise local bridge rejected.

---

## CL-0020

**Status:** PROVED IN PROJECT

**Statement:** For every finite reflection-invariant signed point measure avoiding 0 and 1, the finite-factor Li-type derivative response equals the signed response of the standard Li zero kernel.

**Proof status:** The result follows from the pointwise reflection identity g_n(z) = f_n(1-z) and invariance of the finite signed measure under z -> 1-z. The single-factor derivative kernel, reflection identity, and orbit-level response have undergone symbolic and arbitrary-precision computational validation.

**Originality status:** Unresolved. The project does not claim this identity is new in the literature.

---

## CL-0021

**Status:** HEURISTIC

**Statement:** Symmetry-orbit aggregation may be a more natural unit of local analysis for RH-related zero diagnostics than an individual zero contribution.

**Project claim?:** Not a theorem about RH.

**Motivation:** The Li derivative-side and zero-side kernels agree under reflection-invariant orbit aggregation despite failing to agree term-by-term.

---

## CL-0022

**Status:** PROJECT CONJECTURE CANDIDATE — NOT YET ACTIVATED

**Statement:** For every analytic conjugation-compatible kernel near the critical-line pair, the matched horizontal-minus-vertical four-zero contrast divided by twice the squared displacement converges to the project quadratic susceptibility.

**Reason not activated:** A proof has been written but independent symbolic and numerical validation has not yet been completed.

---

## CL-0023

**Status:** HEURISTIC

**Statement:** Horizontal-versus-vertical zero-geometry contrast is a cleaner structural interpretation of the project susceptibility than doubled-orbit splitting because it compares two multiplicity-conserving reflection-invariant four-zero configurations.

**Project claim?:** Methodological interpretation, not a theorem about RH.

---

## CL-0024

**Status:** FAILED CLAIM PREVENTION RULE

**Statement:** A finite degree-four entire zero factor with xi-like reflection symmetry is not thereby a Riemann xi-function or an arithmetic L-function.

**Purpose:** Prevent finite analytic symmetry from being mislabeled as arithmetic structure.

---

## CL-0025

**Status:** PROVED IN PROJECT

**Statement:** For the matched horizontal-minus-vertical analytic contrast, only even derivative orders congruent to 2 modulo 4 survive. Under conjugation compatibility,
\[
\mathcal A_f(\delta,\gamma)
=
8
\sum_{k\ge0}
\frac{\delta^{4k+2}}{(4k+2)!}
\Re f^{(4k+2)}(1/2+i\gamma)
\]
within the common Taylor convergence range.

**Proof status:** Derived from the symmetric Taylor expansions and the factor \(1-(-1)^m\). Symbolically validated through derivative order 14 and numerically validated for the Li kernel.

**Originality status:** The underlying quarter-turn/root-of-unity filtering mechanism is standard. No literature novelty claim is made.

---

## CL-0026

**Status:** PROVED IN PROJECT

**Statement:** The Li-kernel directional contrast satisfies
\[
\mathcal A_{f_n}(\delta,\gamma)
=
2\delta^2\chi_n^{\mathrm{Li}}(\gamma)
+
\frac{\delta^6}{90}
\Re f_n^{(6)}(1/2+i\gamma)
+
O(\delta^{10})
\]
locally in delta.

**Originality status:** Unresolved as a project-specific formulation. No claim of novelty is made.

---

## CL-0027

**Status:** FAILED CLAIM

**Statement:** The natural next correction to the horizontal-minus-vertical directional contrast is generically fourth order in delta.

**Failure:** The fourth-order terms in the horizontal and vertical symmetric Taylor expansions are identical and cancel exactly.

**Disposition:** The contrast residual begins at sixth order, with subsequent surviving orders congruent to 2 modulo 4.

---

## CL-0028

**Status:** PROVED IN PROJECT

**Statement:** For the amplitude-normalized explicit-formula zero kernel p_L(z) = -exp(Lz)/z, if gamma tends to infinity and L gamma tends to c > 0, then gamma^3 times the normalized quadratic susceptibility tends to -4c cos(c) + 2(2-c^2) sin(c).

**Proof status:** The result follows from the exact second derivative, the limits gamma/rho_gamma -> -i, gamma^2/rho_gamma^2 -> -1, gamma^3/rho_gamma^3 -> i, and L gamma -> c. The derivative and scaling implementation have undergone symbolic and arbitrary-precision validation.

**Originality status:** Unresolved. No claim is made that the scaling profile is new in the literature.

---

## CL-0029

**Status:** HEURISTIC

**Statement:** Parameterized RH-related zero kernels may admit a comparative susceptibility taxonomy based on a phase coordinate, a kernel-native normalization, a height-decay exponent, and a limiting profile.

**Project claim?:** Methodological hypothesis only.

**Required evidence:** At least two independently validated kernel families followed by a third family used as an adversarial out-of-sample test.

---

## CL-0030

**Status:** FAILED CLAIM PREVENTION RULE

**Statement:** The scaling L gamma -> c for the explicit-formula zero kernel must not be described as the natural large-x prime-counting regime.

**Purpose:** The scaling sends L -> 0 and x = exp(L) -> 1 from above. It is a phase-preserving individual-kernel regime, not a standard asymptotic prime-counting regime.

---

## CL-0031

**Status:** FAILED CLAIM

**Statement:** A wrong fixed exponential normalization exponent should necessarily destroy the leading explicit-formula mesoscopic scaling collapse.

**Failure:** Under L gamma -> c, one has L -> 0, so the residual factor exp((1/2-a)L) tends to 1 for every fixed normalization exponent a.

**Disposition:** Exact normalization is justified by critical-line amplitude factorization, not by uniqueness of the leading scaling collapse.

---

## CL-0032

**Status:** COMPUTATIONAL OBSERVATION

**Statement:** Across the Phase 2B parameter grid, the scaled amplitude-normalized explicit-formula susceptibility converged numerically toward the analytically derived profile.

**Interpretation:** Validation of the proved scaling law and implementation.

**Not evidence for:** RH, novelty, or comparative superiority over the Li diagnostic.

---

## CL-0033

**Status:** PROJECT CONJECTURE CANDIDATE — FROZEN PRE-DERIVATION PREDICTION

**Statement:** For the resolvent kernel r_a(z) = 1/(a-z), if gamma tends to infinity and (a-1/2)/gamma tends to c > 0, then gamma^3 times the quadratic susceptibility converges to a nontrivial profile depending on c.

**Predicted profile type:** Rational in c.

**Originality claim:** None.

---

## CL-0034

**Status:** PROJECT CONJECTURE CANDIDATE — FROZEN PRE-DERIVATION PREDICTION

**Statement:** For fixed real a > 1/2, the resolvent-kernel susceptibility is O_a(gamma^-4), with leading coefficient proportional to a-1/2.

**Originality claim:** None.

---

## CL-0035

**Status:** HEURISTIC — FROZEN TAXONOMY PREDICTION

**Statement:** The phrase "phase coordinate" is too restrictive for a general susceptibility scaling taxonomy and should be replaced by "asymptotic similarity coordinate."

**Test case:** Resolvent kernel r_a(z) = 1/(a-z).

---

## CL-0036

**Status:** PROVED IN PROJECT

**Statement:** For the resolvent kernel r_a(z) = 1/(a-z), with d = a-1/2,
\[
\chi_a^{Res}(\gamma)
=
\frac{4d(d^2-3\gamma^2)}{(d^2+\gamma^2)^3}.
\]

**Proof status:** Direct differentiation and algebraic extraction of the real part.

**Originality status:** No originality claim. The calculation is elementary.

---

## CL-0037

**Status:** PROVED IN PROJECT

**Statement:** If gamma tends to infinity and (a-1/2)/gamma tends to c > 0, then
\[
\gamma^3\chi_a^{Res}(\gamma)
\to
\frac{4c(c^2-3)}{(c^2+1)^3}.
\]

**Frozen prediction result:** P-RES-001 PASS and P-RES-002 PASS.

**Originality status:** Unresolved as a taxonomy example; no claim that the asymptotic calculation itself is new.

---

## CL-0038

**Status:** PROVED IN PROJECT

**Statement:** For fixed real a > 1/2,
\[
\chi_a^{Res}(\gamma)
\sim
-12(a-1/2)\gamma^{-4}.
\]

**Frozen prediction result:** P-RES-004 PASS.

---

## CL-0039

**Status:** HEURISTIC — SUPPORTED BY THIRD-FAMILY TEST

**Statement:** "Asymptotic similarity coordinate" is a more general term than "phase coordinate" for the project susceptibility taxonomy.

**Evidence:** The resolvent coordinate (a-1/2)/gamma controls an exact nonoscillatory rational profile and sign transition.

**Status warning:** Methodological terminology, not a theorem.

---

## CL-0040

**Status:** HEURISTIC

**Statement:** A useful cross-diagnostic susceptibility taxonomy may need to record profile zeros and vanishing orders because parameter paths approaching a zero of the limiting profile can exhibit stronger decay than the generic family exponent.

**Motivating example:** Resolvent fixed-a regime.

---

## CL-0041

**Status:** COMPUTATIONAL OBSERVATION

**Statement:** The Phase 2E arbitrary-precision and symbolic validation suite independently reproduced the exact resolvent susceptibility, generic similarity profile, fixed-a boundary law, and profile zero at c = sqrt(3).

**Interpretation:** Validation of the project derivation and frozen prediction scorecard.

**Not evidence for:** RH or originality.

---

## CL-0042

**Status:** HEURISTIC — SUPPORTED BY OUT-OF-SAMPLE TEST

**Statement:** The susceptibility signature language has predictive organizing value across the three kernel families studied in the project.

**Evidence:** Four qualitative predictions for the third family were frozen before derivation and all survived analytic and computational validation.

**Limitation:** The predictions were guided by homogeneity and dimensional analysis. Broader mathematical significance remains unresolved.

---

## CL-0043

**Status:** FAILED CLAIM PREVENTION RULE

**Statement:** The quarter-turn derivative filter must not be described as a project discovery before a prior-art audit.

**Reason:** The mechanism strongly resembles standard roots-of-unity and complex finite-difference filtering.

---

## CL-0044

**Status:** FAILED CLAIM PREVENTION RULE

**Statement:** The susceptibility scaling signature language must not be called a novel taxonomy before the closest asymptotic-scaling and zero-kernel literature is identified.

---

## CL-0045

**Status:** KNOWN PROJECT LIMITATION

**Statement:** As of Phase 3A, the project has no established Level IV RH-relevant consequence such as a new equivalent criterion, zero-free region, positivity theorem, or exclusion of off-critical zeros.

---

## CL-0046

**Status:** PROJECT RESEARCH QUESTION

**Statement:** After known analytic mechanisms are factored out, does the horizontal-versus-vertical zero-orbit contrast support a mathematically useful comparative classification of RH-related zero kernels that is not already subsumed by existing literature?

**Status:** OPEN INSIDE PROJECT.

---

## CL-0047

**Status:** PROJECT RESEARCH PROTOCOL

**Statement:** Prior-art searches must include exact-object, mathematical-ancestor, and RH-application queries. Keyword absence using project terminology is not evidence of novelty.

---

## CL-0048

**Status:** PROJECT PREDICTION — PRIOR-ART RISK

**Statement:** The generic 4k+2 quarter-turn derivative-filter mechanism is expected to have strong prior art under roots-of-unity or cyclic Taylor-coefficient filtering.

**Consequence if confirmed:** CL-0025 remains mathematically true but must be cited as a standard mechanism rather than framed as a project contribution.

---

## CL-0049

**Status:** PROJECT PREDICTION — TERMINOLOGY RISK

**Statement:** The project's use of "mesoscopic scaling" may conflict with established mesoscopic linear-statistics terminology in zeta-zero research.

**Possible disposition:** Rename the project regime to coupled similarity scaling or parameter-height similarity scaling.

---

## CL-0050

**Status:** PROJECT RESEARCH QUESTION

**Statement:** Does prior literature study the differential response of Li coefficients to finite symmetry-preserving displacement of hypothetical zero orbits?

**Priority:** HIGH.

---

## CL-0051

**Status:** FAILED CLAIM

**Statement:** Broad quantitative sensitivity of Li-type coefficients to zero location is absent from established literature.

**Failure:** Generalized Li and tau-Li literature explicitly connects coefficient behavior to off-critical zeros, half-plane zero location, and zero-free regions.

**Disposition:** Broad novelty framing withdrawn.

---

## CL-0052

**Status:** FAILED CLAIM

**Statement:** Reflection-orbit aggregation in Li-type zero sums can be framed as a project-originating structural insight.

**Failure:** Generalized Li literature explicitly pairs reflection-related zeros in Li-type criteria.

**Disposition:** Reflection pairing is treated as prior structural context.

---

## CL-0053

**Status:** FAILED CLAIM

**Statement:** Critical-line phase representation of the Li zero kernel is project-originating.

**Failure:** Prior literature expresses critical-line Li contributions through cosine and Chebyshev phase structure.

**Disposition:** Phase representation treated as prior art.

---

## CL-0054

**Status:** PROJECT RESEARCH QUESTION — NARROWED AFTER PRIOR-ART REVIEW

**Statement:** Has the symmetry-preserving second variation of the fixed Li zero kernel under finite zero-orbit displacement, including the horizontal-versus-vertical four-zero contrast and coupled n/gamma scaling profile, been studied in materially equivalent form?

**Status:** OPEN.

**Current highest prior-art grade:** PA-3.

**PA-4 source identified:** No.

---

## CL-0055

**Status:** FAILED CLAIM

**Statement:** Coupling the Li index n to zero height is project-originating.

**Failure:** Voros's saddle and Darboux analysis already couples large-n Li behavior to individual zero geometry and produces n/tau_k dependence.

**Disposition:** Treat n-versus-zero geometry as prior asymptotic context.

---

## CL-0056

**Status:** FAILED CLAIM

**Statement:** Continuous response analysis of parameterized Li-type coefficients is absent from prior literature.

**Failure:** Freitas differentiates a continuous Li-type coefficient family with respect to tau and derives a differential system.

**Disposition:** The project must distinguish zero-coordinate variation from criterion-parameter variation.

---

## CL-0057

**Status:** FAILED CLAIM

**Statement:** Abstract multiset or signed zero-configuration language is project-originating infrastructure.

**Failure:** Bombieri-Lagarias formulate Li-type criteria for arbitrary complex multisets with convergence and symmetry conditions.

**Disposition:** Cite Bombieri-Lagarias as foundational multiset context.

---

## CL-0058

**Status:** FAILED CLAIM

**Statement:** The horizontal reflection-symmetric four-zero configuration H_{delta,gamma} is project-originating zero geometry.

**Failure:** Shifted products F(s-a)F(s+a) in modified Li-criterion literature realize zeros 1/2 plus-or-minus a plus-or-minus i gamma from a critical-line conjugate pair.

**Disposition:** Horizontal quartet geometry treated as prior structural context.

---

## CL-0059

**Status:** PROJECT RESEARCH QUESTION — FURTHER NARROWED

**Statement:** Has the infinitesimal second variation of the fixed Li zero kernel under symmetry-preserving horizontal zero displacement, its quarter-turn horizontal-versus-vertical contrast, and the simultaneous n/gamma -> c response scaling been studied in materially equivalent form?

**Current highest prior-art grade:** PA-3.

**PA-4 identified in Q4-BC-001:** No.

**Originality status:** Unresolved.

---

## CL-0060

**Status:** FAILED CLAIM

**Statement:** The scaling n proportional to zero height can be framed as project-originating Li sensitivity structure.

**Failure:** Voros quantitatively connects Li-like index sensitivity to the height of RH-violating zeros.

**Disposition:** The bare n-versus-height scale is treated as prior art.

---

## CL-0061

**Status:** FAILED CLAIM

**Statement:** Individual-zero Li sensitivity to off-critical displacement is absent from prior literature.

**Failure:** Maślanka explicitly discusses how deviation from the critical line changes the modulus of an individual Li zero contribution and the Li index needed to feel the deviation.

**Disposition:** Individual-zero sensitivity treated as prior art.

---

## CL-0062

**Status:** PROJECT RESEARCH QUESTION — EXACT COMBINATION

**Statement:** Is the combined theorem package consisting of fixed-Li-kernel quadratic zero-coordinate response, its horizontal-versus-vertical quarter-turn finite-configuration realization, and the explicit n/gamma coupled limiting profile already present in materially equivalent form?

**Current highest prior-art grade:** PA-3.

**PA-4 identified in Q4-EXACT-001:** No.

**Originality status:** Unresolved.

---

## CL-0063

**Status:** FAILED CLAIM PREVENTION RULE

**Statement:** Discovery of no PA-4 source in the uploaded search set is not equivalent to proof of novelty.

**Purpose:** Prevent search incompleteness from being converted into a mathematical originality claim.

---

## CL-0064

**Status:** PROVED IN PROJECT

**Statement:** The positive nonzero zeros of the Li quadratic-response profile are exactly one root c_k in each interval ((k+1/2)pi,(k+1)pi), characterized by tan(c_k) = -c_k/2.

**Originality status:** Unresolved.

---

## CL-0065

**Status:** PROVED IN PROJECT

**Statement:** For q=n/gamma in a fixed compact positive range,
\[
\chi_n^{Li}(\gamma)
=
\gamma^{-2}\Psi_{Li}(q)
+
\gamma^{-4}K_{Li}(q)
+
O_q(\gamma^{-6}),
\]
with
\[
K_{Li}(q)
=
q(q\cos q+2\sin q)
+
\frac{q^2}{6}(-q\sin q+2\cos q).
\]

---

## CL-0066

**Status:** PROVED IN PROJECT

**Statement:** Along exact matched paths n/gamma = c_k, where c_k is a positive Li response-profile zero,
\[
\gamma^4\chi_n^{Li}(\gamma)
\to
\frac{c_k^2(c_k^2+4)}{12}\cos c_k.
\]

**Interpretation:** The individual-kernel quadratic response gains two height-decay powers at an exact profile blind scale.

---

## CL-0067

**Status:** PROVED IN PROJECT

**Statement:** If n/gamma - c_k is asymptotic to beta gamma^{-r}, beta nonzero, then the effective Li quadratic-response exponent follows 2 + min(r,2), except when the displayed leading coefficient cancels at the critical rate r=2.

---

## CL-0068

**Status:** PROVED IN PROJECT

**Statement:** The leading Li susceptibility profile has no unconstrained global magnitude maximizer on c > 0 because its magnitude is unbounded.

**Interpretation:** Any optimal-response claim requires an external cost or admissible-coordinate constraint.

---

## CL-0069

**Status:** FAILED CLAIM PREVENTION RULE

**Statement:** Individual-kernel response blind scales must not be described as blind spots of the complete Li coefficient sequence without a global zero-sum theorem.

**Purpose:** Preserve the distinction between local zero-kernel response and the full RH-equivalent diagnostic.

---

## CL-0070

**Status:** COMPUTATIONAL OBSERVATION

**Statement:** Arbitrary-precision near-blind path experiments reproduced the predicted effective exponents 2.5, 3, 3.5, 4, and 4 for r = 1/2, 1, 3/2, 2, and 3 respectively.

**Interpretation:** Validation of the analytically derived transition hierarchy and implementation.

**Not evidence for:** RH or global Li coefficient blind spots.

---

## CL-0071

**Status:** PROVED IN PROJECT

**Statement:** Integer rounding can invalidate numerical tests of near-blind paths with approach rate r > 1 because rounding n introduces an O(gamma^-1) perturbation in n/gamma.

**Disposition:** Near-blind experiments preserve integer n and solve implicitly for gamma.

---

## CL-0072

**Status:** PROJECT RESEARCH QUESTION

**Statement:** Can the individual-kernel blind-scale hierarchy be lifted to a controlled finite or truncated global Li zero sum without collective zero contributions destroying the profile cancellation?

**Priority:** HIGH.

**Status:** OPEN.

---

## CL-0073

**Status:** PROVED IN PROJECT

**Statement:** For a finite orbit family with relative heights a_j and weights w_j, the coupled aggregate Li quadratic-response profile is
\[
\Psi^{agg}_{a,w}(c)
=
\sum_j
w_j a_j^{-2}
\Psi_{Li}(c/a_j).
\]

---

## CL-0074

**Status:** PROVED IN PROJECT

**Statement:** In the equal-weight two-orbit model with relative heights 1 and a, an individual blind coordinate c_k remains a leading-order aggregate blind coordinate if and only if
\[
a=c_k/c_m
\]
for some positive Li response blind scale c_m.

---

## CL-0075

**Status:** PROVED IN PROJECT

**Statement:** At a two-orbit resonance a=c_k/c_m and common coordinate c_k, the fourth-order aggregate coefficient is
\[
K(c_k)
+
(c_m/c_k)^4 K(c_m).
\]

---

## CL-0076

**Status:** PROVED IN PROJECT

**Statement:** Every same-parity resonant pair k congruent to m modulo 2 has a nonzero fourth-order aggregate coefficient and therefore exact aggregate response exponent 4.

---

## CL-0077

**Status:** PROJECT RESEARCH QUESTION

**Statement:** Do opposite-parity blind-scale resonances admit exact or asymptotically arbitrarily strong fourth-order cancellation?

**Priority:** HIGH.

**Status:** OPEN.

---

## CL-0078

**Status:** FAILED CLAIM PREVENTION RULE

**Statement:** A single-orbit blind scale must not be assumed to survive finite aggregation.

**Reason:** A generic second orbit contributes a nonzero leading aggregate profile at the first orbit's blind coordinate.

---

## CL-0079

**Status:** FAILED CLAIM PREVENTION RULE

**Statement:** Blind-scale ratio resonance in a synthetic finite orbit family must not be attributed to actual Riemann zeta zero heights without an arithmetic theorem or explicit verified zero-height analysis.

---

## CL-0080

**Status:** PROVED IN PROJECT

**Statement:** The blind-scale fourth-order correction has the exact sign-explicit form
\[
K_{Li}(c_k)
=
(-1)^{k+1}
\frac{c_k^2\sqrt{c_k^2+4}}{6}.
\]

---

## CL-0081

**Status:** PROVED IN PROJECT

**Statement:** No equal-weight two-orbit blind-scale ratio resonance has zero fourth-order aggregate coefficient.

**Reason:** After positive rescaling, opposite-parity cancellation would require equality of the strictly increasing function
\[
F(x)=x^6\sqrt{x^2+4}
\]
at two distinct blind scales.

---

## CL-0082

**Status:** PROVED IN PROJECT

**Statement:** For adjacent resonant blind scales,
\[
R_{k,k+1}
\sim
\frac{7\pi}{2c_k},
\]
where R is the normalized fourth-order cancellation ratio.

**Consequence:** Relative cancellation becomes arbitrarily strong as k tends to infinity.

---

## CL-0083

**Status:** PROVED IN PROJECT

**Statement:** The absolute adjacent resonant fourth-order coefficient satisfies
\[
|K_{k,k+1}^{(2)}|
\sim
\frac{7\pi}{6}c_k^2.
\]

**Consequence:** Strong relative cancellation does not imply small absolute aggregate response.

---

## CL-0084

**Status:** COMPUTATIONAL OBSERVATION

**Statement:** An arbitrary-precision scan of 40,000 ordered resonant pairs with indices 0 through 199 found no zero fourth-order coefficient. The minimum normalized cancellation ratio observed was approximately 0.0175859577499984 at ordered pair (199,198).

**Interpretation:** Adversarial implementation validation of analytic results.

---

## CL-0085

**Status:** FAILED CLAIM

**Statement:** Opposite-parity two-orbit resonance may permit exact fourth-order cancellation.

**Failure:** Strict monotonicity of x^6 sqrt(x^2+4) excludes exact cancellation.

**Disposition:** Withdraw deeper exact two-orbit resonance as a research direction.

---

## CL-0086

**Status:** PROJECT RESEARCH QUESTION

**Statement:** Can exact fourth-order cancellation occur in a resonant aggregate with three or more orbit contributions, where multiple signed correction terms may balance?

**Priority:** HIGH.

**Status:** OPEN.

---

## CL-0087

**Status:** PROVED IN PROJECT

**Statement:** For a fully aligned resonant finite orbit family,
\[
6c_{k_1}^4K_{\mathrm{agg}}
=
\sum_j
w_j(-1)^{k_j+1}
A_{k_j},
\]
where
\[
A_k=c_k^6\sqrt{c_k^2+4}.
\]

**Interpretation:** Multi-orbit fourth-order resonance reduces exactly to a signed weighted-moment problem.

---

## CL-0088

**Status:** PROVED IN PROJECT

**Statement:** No positive-weight fully aligned resonant family supported on a single blind-scale parity can cancel at fourth order.

---

## CL-0089

**Status:** PROVED IN PROJECT

**Statement:** Every mixed-parity resonant index family admits strictly positive real weights that cancel the fourth-order coefficient exactly.

**Interpretation:** Arbitrary continuous weight tuning makes exact cancellation a codimension-one linear condition.

---

## CL-0090

**Status:** PROVED IN PROJECT

**Statement:** For fixed mixed-parity indices and normalized positive weights, exact fourth-order cancellation lies on a codimension-one affine slice of the weight simplex and has simplex Lebesgue measure zero.

---

## CL-0091

**Status:** PROVED IN PROJECT

**Statement:** A transverse perturbation of an exactly cancelling weight vector restores the fourth-order aggregate coefficient linearly in the perturbation size.

---

## CL-0092

**Status:** FAILED CLAIM PREVENTION RULE

**Statement:** Exact cancellation found by unconstrained optimization over positive real orbit weights must not be presented as a rigid multi-orbit resonance discovery.

**Reason:** Mixed-parity cancellation is one linear weight constraint and is always continuously tunable.

---

## CL-0093

**Status:** PROVED IN PROJECT

**Statement:** Equal-weight three-orbit exact fourth-order cancellation reduces to
\[
A_r=A_p+A_q
\]
with the unique-parity index satisfying
\[
r>\max(p,q).
\]

---

## CL-0094

**Status:** FAILED CLAIM PREVENTION RULE

**Statement:** The large-index approximation
\[
(r+1/2)^7
\approx
(p+1/2)^7+(q+1/2)^7
\]
does not permit application of Fermat's Last Theorem to the exact blind-scale moment equation.

---

## CL-0095

**Status:** PROJECT RESEARCH QUESTION

**Statement:** Do there exist equal-weight three-orbit blind-scale indices of the required parity satisfying
\[
A_r=A_p+A_q?
\]

**Priority:** HIGH.

**Status:** OPEN.

---

## CL-0096

**Status:** PROJECT RESEARCH QUESTION

**Statement:** If exact equal-weight three-orbit cancellation does not occur in a large search range, how small can the normalized signed defect
\[
D(p,q,r)
=
\frac{|A_r-A_p-A_q|}{A_r+A_p+A_q}
\]
be relative to the natural local spacing scale of the blind-scale moment sequence?

**Priority:** HIGH.

**Status:** OPEN.

---

## CL-0097

**Status:** COMPUTATIONAL OBSERVATION

**Statement:** The strongest equal-weight three-orbit parity-local candidate through blind-scale index 2999 was
\[
(p,q,r)=(1995,2225,2350).
\]

**Global normalized defect:**
approximately
\[
4.4321\times10^{-11}.
\]

**Parity-local defect:**
approximately
\[
1.49203844\times10^{-7}.
\]

---

## CL-0098

**Status:** COMPUTATIONAL OBSERVATION

**Statement:** A 500-decimal-digit independent recomputation preserved the strongest Phase 4F candidate and its normalized defects to extreme relative accuracy and confirmed a nonzero signed residual.

**Interpretation:** The best candidate is not a low-precision numerical artifact.

**Not evidence for:** exact equality or RH.

---

## CL-0099

**Status:** HEURISTIC

**Statement:** Under an iid Uniform(0,1/2) benchmark for parity-local defects, the expected minimum among 3,357,233 candidate records is approximately
\[
1.4893\times10^{-7}.
\]

The observed minimum divided by this benchmark is

\[
1.00182443666\ldots.
\]

**Warning:** Dependence and uniformity have not been proved.

---

## CL-0100

**Status:** HEURISTIC

**Statement:** Under the same crude iid benchmark,
\[
P(
\min E
\le
E_{\min,\mathrm{obs}}
)
\approx
0.632791065.
\]

**Interpretation:** The best observed three-orbit candidate is not anomalously close under the declared simple benchmark.

**This is not a rigorous p-value.**

---

## CL-0101

**Status:** COMPUTATIONAL OBSERVATION

**Statement:** No exact equal-weight three-orbit blind-scale moment relation was certified in the Phase 4F search through index 2999.

**Limitation:** Finite numerical search does not prove global nonexistence.

---

## CL-0102

**Status:** FAILED CLAIM

**Statement:** The tiny global normalized defect of the best three-orbit candidate is by itself evidence of anomalous additive blind-scale resonance.

**Failure:** After parity-local spacing normalization and multiple-search comparison, the observed minimum is approximately equal to the crude benchmark expected minimum.

**Disposition:** No additive-resonance conjecture is promoted from the Phase 4F candidate.

---

## CL-0103

**Status:** FAILED CLAIM PREVENTION RULE

**Statement:** A very small global normalized signed-moment defect must not be interpreted without comparison to parity-admissible local spacing and search multiplicity.

---

## CL-0104

**Status:** PROJECT RESEARCH QUESTION

**Statement:** Can the parity-local defect distribution for blind-scale moment pair sums be analyzed analytically, replacing the crude iid Uniform(0,1/2) benchmark with a deterministic equidistribution, discrepancy, or spacing theorem?

**Priority:** MEDIUM.

**Status:** OPEN.

---

## CL-0105

**Status:** PROJECT RESEARCH QUESTION

**Statement:** Should the project continue deeper into synthetic finite-orbit additive resonance, or redirect toward a controlled bridge to actual zeta zero data and truncated Li zero sums?

**Priority:** CRITICAL STRATEGIC DECISION.

**Status:** OPEN.

---

## CL-0106

**Status:** HEURISTIC — FROZEN CONTINUUM PREDICTION

**Statement:** Under the leading smooth zero-density approximation, the normalized positive-width zeta-zero window susceptibility has response profile
\[
\Phi_\eta(c)
=
\frac{c}{\pi}
\left[
(1+\eta)^{-2}\sin(c/(1+\eta))
-
\sin c
\right].
\]

---

## CL-0107

**Status:** PROVED IN PROJECT

**Statement:** The continuum window-profile integral
\[
\frac{1}{2\pi}
\int_1^{1+\eta}
u^{-2}
\Psi_{Li}(c/u)\,du
\]
reduces exactly to
\[
\frac{c}{\pi}
\left[
(1+\eta)^{-2}\sin(c/(1+\eta))
-
\sin c
\right].
\]

**Scope:** Algebraic identity for the project continuum profile.

---

## CL-0108

**Status:** PROVED IN PROJECT

**Statement:** The narrow-window consistency law is
\[
\lim_{\eta\to0^+}
\frac{\Phi_\eta(c)}{\eta}
=
\frac{\Psi_{Li}(c)}{2\pi}.
\]

---

## CL-0109

**Status:** PROJECT PREDICTION

**Statement:** Positive-width actual-zero windows will generically smear the individual Li quadratic-response blind scales.

**Prediction ID:** P-ZETA-001.

---

## CL-0110

**Status:** PROJECT PREDICTION

**Statement:** H/log H normalized truncated high-zero window susceptibility will show broad agreement with the frozen smooth-density profile.

**Prediction ID:** P-ZETA-002.

---

## CL-0111

**Status:** PROJECT PREDICTION

**Statement:** Empirical window-response zeros will track smooth-density window-profile zeros more closely than individual-kernel blind scales once windows contain sufficiently many computed zero ordinates.

**Prediction ID:** P-ZETA-003.

---

## CL-0112

**Status:** FAILED CLAIM PREVENTION RULE

**Statement:** A finite computational data set of critical-line zeta zeros must not be used to assert that all nontrivial zeta zeros lie on the critical line.

---

## CL-0113

**Status:** PROJECT RESEARCH QUESTION

**Statement:** Does the individual-kernel susceptibility profile survive actual zeta-zero aggregation through the smooth-density window profile predicted in Phase 5A?

**Priority:** CRITICAL.

**Status:** OPEN.

---

## CL-0114

**Status:** COMPUTATIONAL OBSERVATION

**Statement:** The first-500-zero dataset spans ordinates from approximately 14.1347251417 to 811.1843588465.

---

## CL-0115

**Status:** COMPUTATIONAL OBSERVATION

**Statement:** Among complete audited relative-height windows in the first-500-zero dataset, occupancy ranged from 1 to 170 zeros.

---

## CL-0116

**Status:** COMPUTATIONAL OBSERVATION

**Statement:** The occupancy audit found 29 complete windows with at least 10 zeros, 18 with at least 25 zeros, and 10 with at least 50 zeros.

---

## CL-0117

**Status:** PROJECT EXPERIMENTAL PROTOCOL

**Statement:** Phase 5C stratifies actual-zero windows by occupancy and treats windows with at least 25 zeros as primary continuum-profile tests, with windows containing at least 50 zeros forming the strongest initial subset.

---

## CL-0118

**Status:** FAILED CLAIM PREVENTION RULE

**Statement:** Poor agreement in very sparse zero windows must not be treated as a decisive falsification of the smooth-density continuum approximation.

**Reason:** The continuum model suppresses discrete zero fluctuations and is not expected to describe one-zero or few-zero windows accurately.

---

## CL-0119

**Status:** PROJECT RESEARCH QUESTION

**Statement:** At accessible zero heights, how much of the discrepancy between discrete window susceptibility and the frozen asymptotic profile is explained by retaining the finite-height logarithmic zero-density factor?

**Priority:** HIGH.

**Status:** OPEN.

---

## CL-0120

**Status:** COMPUTATIONAL OBSERVATION

**Statement:** Mean frozen-profile correlation increased from approximately 0.995056 to 0.997805 to 0.998216 when restricting actual-zero window comparisons to occupancy thresholds of at least 10, 25, and 50 zeros respectively.

**Interpretation:** More highly populated tested windows exhibited stronger profile-shape agreement.

**Not evidence for:** asymptotic convergence.

---

## CL-0121

**Status:** COMPUTATIONAL OBSERVATION

**Statement:** In the occupancy-at-least-50 subset, the frozen smooth-density window profile achieved mean correlation approximately 0.998216 and mean sign agreement 0.9925 against the normalized discrete actual-zero response.

---

## CL-0122

**Status:** COMPUTATIONAL OBSERVATION

**Statement:** In the occupancy-at-least-50 subset, the frozen leading profile had mean NRMSE approximately 0.304070, while the finite-height logarithmic-density benchmark had mean NRMSE approximately 0.036257.

**Interpretation:** The finite-height benchmark reduced mean NRMSE by a factor of approximately 8.39.

---

## CL-0123

**Status:** COMPUTATIONAL OBSERVATION

**Statement:** For all reported occupancy thresholds, the nearest-root protocol found every recorded empirical response root closer to a window-profile root than to an individual Li blind scale.

**High-occupancy empirical root count:** 60.

---

## CL-0124

**Status:** PROJECT PREDICTION SCORE

**Prediction:** P-ZETA-001.

**Result:** PASS.

**Statement:** Positive-width actual-zero windows smear individual Li response blind scales in the tested finite data.

---

## CL-0125

**Status:** PROJECT PREDICTION SCORE

**Prediction:** P-ZETA-002.

**Result:** PASS WITH FINITE-HEIGHT AMPLITUDE QUALIFICATION.

**Statement:** The frozen H/log H smooth-density profile reproduced high-occupancy curve shape and sign structure strongly, but retained substantial amplitude error at accessible heights.

---

## CL-0126

**Status:** PROJECT PREDICTION SCORE

**Prediction:** P-ZETA-003.

**Result:** PASS.

**Statement:** Empirical response-zero locations preferred window-profile roots over individual blind scales under the frozen nearest-root comparison protocol.

---

## CL-0127

**Status:** COMPUTATIONAL OBSERVATION

**Statement:** The finite actual-zero experiment supports a response-profile transformation from the individual profile Psi_Li to the positive-width smooth window profile Phi_eta at the level of curve shape and response-zero geometry.

**Scope:** First-500-zero computational dataset.

**Not a theorem of:** discrete convergence.

---

## CL-0128

**Status:** FAILED CLAIM PREVENTION RULE

**Statement:** High correlation between discrete actual-zero response and the smooth-density window profile must not be described as proof of a discrete asymptotic theorem.

---

## CL-0129

**Status:** FAILED CLAIM PREVENTION RULE

**Statement:** The actual-zero window response experiment must not be described as evidence that RH is true.

**Reason:** The experiment studies a project-defined response statistic on a finite computational critical-line zero dataset.

---

## CL-0130

**Status:** PROJECT RESEARCH QUESTION

**Statement:** As the zero-height range and window occupancy increase, does the frozen leading-profile NRMSE decrease relative to the finite-height benchmark in a manner consistent with the predicted logarithmic asymptotic correction?

**Priority:** CRITICAL.

**Status:** OPEN.

---

## CL-0131

**Status:** PROJECT RESEARCH QUESTION

**Statement:** Can the discrepancy between the discrete actual-zero window response and the smooth-density benchmark be decomposed into an explicit finite-height deterministic term plus a fluctuation term tied to zeta zero-counting error?

**Priority:** CRITICAL.

**Status:** OPEN.

---

## CL-0132

**Status:** PROVED IN PROJECT

**Statement:** For the frozen finite zero dataset, the discrete Li window response admits the exact Stieltjes decomposition
\[
\mathcal W_n
=
S_{\mathrm{exact}}
+
R_{\mathrm{count}},
\]
where the counting remainder is expressed through the empirical counting remainder E_D, endpoint terms, and an E_D-weighted susceptibility derivative integral.

**Scope:** Finite empirical counting function.

---

## CL-0133

**Status:** PROVED IN PROJECT

**Statement:** The Phase 5C finite-height profile discrepancy decomposes exactly as
\[
\mathcal W_n-S_{\mathrm{profile}}
=
R_{\mathrm{count}}
+
R_{\mathrm{kernel}}.
\]

---

## CL-0134

**Status:** PROVED IN PROJECT

**Statement:** Under the validated compact-range two-term susceptibility expansion and fixed relative-window geometry, the normalized smooth kernel truncation has candidate scale
\[
\frac H{\log H}R_{\mathrm{kernel}}
=
O(H^{-2}).
\]

---

## CL-0135

**Status:** HEURISTIC SCALE PREDICTION

**Statement:** If the empirical or classical zero-counting remainder is on a logarithmic scale, the normalized counting contribution has candidate scale
\[
\frac H{\log H}R_{\mathrm{count}}
=
O(H^{-1}).
\]

**Not a new zero-counting theorem.**

---

## CL-0136

**Status:** PROVED IN PROJECT

**Statement:** The counting remainder satisfies the computable certificate
\[
|R_{\mathrm{count}}|
\le
|f(H)|\Delta N_D(H)
+
|f(B)||E_D(B)|
+
|f(H)||E_D(H)|
+
\|E_D\|_\infty
\int_H^B|f'(t)|dt.
\]

---

## CL-0137

**Status:** PROJECT EXPERIMENTAL CORRECTION

**Statement:** Because the Phase 5C window anchors H are dataset zero ordinates and the discrete statistic uses [H,B], the exact decomposition contains an explicit left-endpoint atom
\[
R_{\mathrm{atom}}
=
\chi_n^{Li}(H).
\]

---

## CL-0138

**Status:** PROJECT PREDICTION

**Prediction ID:** P-DEC-001.

**Statement:** The numerical discrepancy decomposition will close to arbitrary-precision quadrature tolerance.

---

## CL-0139

**Status:** PROJECT PREDICTION

**Prediction ID:** P-DEC-002.

**Statement:** Counting-remainder RMS will generally exceed kernel-remainder RMS in dense and high-occupancy tested windows.

---

## CL-0140

**Status:** PROJECT PREDICTION

**Prediction ID:** P-DEC-003.

**Statement:** Normalized kernel-remainder magnitude will exhibit a steeper height-decay trend than normalized counting-remainder magnitude.

---

## CL-0141

**Status:** PROJECT PREDICTION

**Prediction ID:** P-DEC-004.

**Statement:** Removing the explicit left-endpoint atom will improve smooth-model agreement slightly but will not explain most high-occupancy finite-height residual.

---

## CL-0142

**Status:** PROJECT RESEARCH QUESTION

**Statement:** Does the Phase 5C residual decompose empirically according to the candidate asymptotic hierarchy counting fluctuation O(H^-1) versus smooth kernel truncation O(H^-2) after H/log H normalization?

**Priority:** CRITICAL.

**Status:** OPEN.

---

## CL-0143

**Status:** FAILED VALIDATION IMPLEMENTATION — ENDPOINT PROVENANCE ERROR

**Statement:** The initial Phase 5E Stieltjes evaluator failed to reproduce the direct empirical counting remainder, with maximum discrepancy approximately
\[
0.0354075785.
\]

**Root cause:** The atomic left endpoint H was reconstructed from a rounded 60-digit display serialization while the theoretical decomposition assumed H was exactly an authoritative dataset zero ordinate.

**Disposition:** Repaired by recovering H from the stored anchor zero index.

---

## CL-0144

**Status:** COMPUTATIONAL OBSERVATION

**Statement:** Among 40 complete occupancy records, zero serialized H values were exactly equal to the authoritative 75-digit stored zero ordinate; 12 were rounded below and 28 were rounded above.

---

## CL-0145

**Status:** PROVED IN PROJECT — IMPLEMENTATION CORRECTNESS RULE

**Statement:** For an atomic counting measure, an arbitrarily small coordinate perturbation of an interval endpoint can change the discrete integral by a full atomic contribution.

**Consequence:** Decimal closeness of endpoint coordinates does not preserve closed-interval membership.

---

## CL-0146

**Status:** COMPUTATIONAL OBSERVATION

**Statement:** After authoritative-anchor recovery and piecewise constant-count quadrature, a six-case targeted Stieltjes validation achieved maximum direct-versus-Stieltjes counting-remainder error approximately
\[
4.08\times10^{-82}.
\]

---

## CL-0147

**Status:** PROJECT REVALIDATION REQUIREMENT

**Statement:** Phase 5C exact metrics require authoritative-anchor rerunning because the original actual-zero window experiment reconstructed atomic window anchors from rounded occupancy-file H values.

**Disposition:** Prior Phase 5C conclusions are marked REVALIDATION REQUIRED pending corrected execution.

---

## CL-0148

**Status:** PROVED IN PROJECT — NUMERICALLY INDEPENDENTLY VALIDATED

**Statement:** After authoritative atomic-anchor repair, the finite-dataset discrepancy identity
\[
\mathcal W_n-S_{\mathrm{profile}}
=
R_{\mathrm{count}}
+
R_{\mathrm{kernel}}
\]
closed with maximum numerical error approximately
\[
6.19\times10^{-61}.
\]

---

## CL-0149

**Status:** PROJECT PREDICTION SCORE

**Prediction ID:** P-DEC-001.

**Result:** PASS.

**Statement:** The independent Stieltjes counting-remainder evaluator reproduces the direct empirical counting residual to arbitrary-precision computational tolerance after endpoint-provenance repair.

---

## CL-0150

**Status:** COMPUTATIONAL OBSERVATION

**Statement:** Counting-remainder RMS exceeded kernel-remainder RMS in every tested dense complete window and every tested high-occupancy window.

**Dense dominance rate:** 1.0.

**High-occupancy dominance rate:** 1.0.

---

## CL-0151

**Status:** COMPUTATIONAL OBSERVATION

**Statement:** The ratio of mean high-occupancy normalized counting RMS to mean high-occupancy normalized kernel RMS was approximately
\[
3115.303893.
\]

**Scope:** Frozen first-500-zero dataset and Phase 5E window protocol.

---

## CL-0152

**Status:** PROJECT PREDICTION SCORE

**Prediction ID:** P-DEC-002.

**Result:** PASS.

**Statement:** Empirical counting-remainder RMS generally exceeds Li-kernel asymptotic truncation RMS in the tested dense windows.

---

## CL-0153

**Status:** COMPUTATIONAL OBSERVATION

**Statement:** Corrected finite-range log-log height slopes were approximately
\[
-1.7339233393
\]
for normalized counting-remainder RMS and
\[
-1.8570110118
\]
for normalized kernel-remainder RMS.

**Interpretation:** The kernel component exhibited the steeper descriptive finite-range decay trend.

**Not evidence for:** exact asymptotic exponents -1 and -2.

---

## CL-0154

**Status:** PROJECT PREDICTION SCORE

**Prediction ID:** P-DEC-003.

**Result:** PASS WITH FINITE-RANGE QUALIFICATION.

---

## CL-0155

**Status:** FAILED PROJECT PREDICTION

**Prediction ID:** P-DEC-004.

**Prediction:** Removing the left-endpoint atom would slightly improve smooth-profile agreement.

**Observed result:** The mean high-occupancy open-to-closed residual RMS ratio was approximately
\[
2.4349109619.
\]

**Failure:** Removing the atom worsened residual RMS by approximately 2.43 times.

**Disposition:** Withdraw the assumption that the anchor atom merely degrades smooth-model agreement.

---

## CL-0156

**Status:** COMPUTATIONAL OBSERVATION

**Statement:** The mean normalized high-occupancy left-atom RMS was approximately
\[
0.01248.
\]

**Interpretation:** The atom is measurable and participates materially in signed residual cancellation, but it does not dominate the full counting-remainder RMS.

---

## CL-0157

**Status:** PROJECT RESEARCH QUESTION

**Statement:** Can the empirical counting-remainder contribution be expressed more directly as a response transform of the zero-counting error, allowing deterministic or conditional bounds in terms of variation norms of the Li susceptibility kernel?

**Priority:** CRITICAL.

**Status:** OPEN.

---

## CL-0158

**Status:** PROJECT RESEARCH QUESTION

**Statement:** Do higher zero-height windows preserve the observed separation between counting-remainder and kernel-truncation scales, and do the descriptive height slopes move toward theoretically predicted asymptotic regimes?

**Priority:** CRITICAL.

**Status:** OPEN.

---

## CL-0159

**Status:** COMPUTATIONAL OBSERVATION — CORRECTED PHASE 5C METRIC

**Statement:** After authoritative-anchor correction, the occupancy-at-least-50 frozen-profile mean NRMSE was approximately
\[
0.2996280740.
\]

---

## CL-0160

**Status:** COMPUTATIONAL OBSERVATION — CORRECTED PHASE 5C METRIC

**Statement:** After authoritative-anchor correction, the occupancy-at-least-50 finite-height mean NRMSE was approximately
\[
0.03598349127.
\]

**Consequence:** The finite-height benchmark improved NRMSE over the frozen leading profile by a factor of approximately 8.33.

---

## CL-0161

**Status:** COMPUTATIONAL OBSERVATION — CORRECTED PHASE 5C METRIC

**Statement:** After authoritative-anchor correction, the occupancy-at-least-50 frozen-profile mean correlation was approximately
\[
0.9986389173
\]
and mean sign agreement was
\[
0.9975.
\]

---

## CL-0162

**Status:** COMPUTATIONAL OBSERVATION — CORRECTED PHASE 5C METRIC

**Statement:** The authoritative-anchor high-occupancy subset retained 60 empirical response roots and a frozen window-profile root win rate of 1.0 versus individual Li blind scales.

---

## CL-0163

**Status:** PROJECT PREDICTION SCORE — REVALIDATED

**Prediction ID:** P-ZETA-001.

**Result:** PASS.

**Statement:** The window-smearing prediction survives authoritative endpoint reconstruction.

---

## CL-0164

**Status:** PROJECT PREDICTION SCORE — REVALIDATED

**Prediction ID:** P-ZETA-002.

**Result:** PASS WITH FINITE-HEIGHT AMPLITUDE QUALIFICATION.

**Statement:** The frozen smooth-density profile retains extremely strong shape and sign agreement after endpoint correction, while finite-height amplitude error remains material.

---

## CL-0165

**Status:** PROJECT PREDICTION SCORE — REVALIDATED

**Prediction ID:** P-ZETA-003.

**Result:** PASS.

**Statement:** The corrected nearest-root protocol retains a 1.0 window-profile win rate against individual blind scales in every reported occupancy subset.

---

## CL-0166

**Status:** PROVED IN PROJECT — DATA PROVENANCE RULE

**Statement:** Atomic window endpoints in zero-measure experiments must be reconstructed from authoritative indexed zero data rather than rounded display coordinates.

**Reason:** Closed-interval membership is discontinuous under endpoint perturbation across an atom.

---

## CL-0167

**Status:** COMPUTATIONAL OBSERVATION

**Statement:** After authoritative-anchor correction, the frozen leading window profile had slightly higher mean high-occupancy correlation than the finite-height benchmark, while the finite-height benchmark retained approximately 8.33 times lower NRMSE.

**Interpretation:** Curve-shape correlation and amplitude accuracy are distinct comparison criteria.

---

## CL-0168

**Status:** PROJECT REVALIDATION RESOLUTION

**Statement:** The Phase 5C REVALIDATION REQUIRED status is resolved.

**Disposition:** The broad response-profile conclusion survives. Final reporting must use authoritative-anchor corrected metrics rather than the archived pre-repair metrics.

---

## CL-0169

**Status:** PROVED IN PROJECT

**Statement:** The non-atomic counting response transform
\[
\mathcal T[E]
=
f(B)E(B)
-
f(H)E(H)
-
\int_H^B E(t)f'(t)dt
\]
satisfies
\[
|\mathcal T[E]|
\le
\Lambda_n(H,\eta)
\|E\|_\infty,
\]
where
\[
\Lambda_n(H,\eta)
=
|f(H)|
+
|f(B)|
+
\int_H^B|f'(t)|dt.
\]

---

## CL-0170

**Status:** PROVED IN PROJECT

**Statement:** The exact sup-norm response-transfer coefficient can be written
\[
\Lambda_n(H,\eta)
=
|f(H)|
+
|f(B)|
+
\operatorname{Var}_{[H,B]}(f).
\]

---

## CL-0171

**Status:** PROVED IN PROJECT

**Statement:** For Holder-conjugate exponents p and q,
\[
|\mathcal T[E]|
\le
|f(B)||E(B)|
+
|f(H)||E(H)|
+
\|E\|_p\|f'\|_q.
\]

---

## CL-0172

**Status:** PROVED IN PROJECT

**Statement:** The leading Li derivative-response profile is
\[
J_{Li}(q)
=
2\Psi_{Li}(q)+q\Psi_{Li}'(q)
=
2q^3\sin q
-
12q^2\cos q
-
12q\sin q.
\]

---

## CL-0173

**Status:** PROVED IN PROJECT

**Statement:** Under matched-scale compact-coordinate and fixed-relative-window assumptions,
\[
H^2\Lambda_n(H,\eta)
\to
\mathcal L_\eta(c),
\]
where
\[
\mathcal L_\eta(c)
=
|\Psi(c)|
+
(1+\eta)^{-2}|\Psi(c/(1+\eta))|
+
\int_1^{1+\eta}u^{-3}|J(c/u)|du.
\]

---

## CL-0174

**Status:** PROJECT COMPARATIVE QUANTITY

**Statement:** Define
\[
Q_\eta(c)
=
\frac{|\Phi_\eta(c)|}
{\mathcal L_\eta(c)}
\]
when the denominator is positive.

**Interpretation:** Smooth window-profile magnitude relative to worst-case sup-norm counting-discrepancy transfer.

**Originality:** UNRESOLVED.

---

## CL-0175

**Status:** PROVED IN PROJECT

**Statement:** At every exact smooth window-profile root with positive transfer envelope,
\[
Q_\eta(c)=0.
\]

**Interpretation:** Smooth response blindness does not imply robustness to counting discrepancy.

---

## CL-0176

**Status:** FAILED CLAIM PREVENTION RULE

**Statement:** A zero of the smooth window-response profile must not automatically be described as a counting-stability point.

**Reason:** The smooth main signal vanishes there while the counting-response transfer coefficient need not vanish.

---

## CL-0177

**Status:** PROJECT PREDICTION

**Prediction ID:** P-TRN-001.

**Statement:** Exact matched-scale transfer coefficients converge numerically to the continuum transfer envelope.

---

## CL-0178

**Status:** PROJECT PREDICTION

**Prediction ID:** P-TRN-002.

**Statement:** The exact sup-norm transfer certificate holds at every tested dense-window decomposition point.

---

## CL-0179

**Status:** PROJECT PREDICTION

**Prediction ID:** P-TRN-003.

**Statement:** The L2 Holder certificate is generally tighter than the L-infinity variation certificate in empirical dense windows.

---

## CL-0180

**Status:** PROJECT PREDICTION

**Prediction ID:** P-TRN-004.

**Statement:** Empirical response-root neighborhoods exhibit lower profile-to-transfer ratio than generic coordinates.

---

## CL-0181

**Status:** PROJECT PREDICTION — HIGH RISK

**Prediction ID:** P-TRN-005.

**Statement:** A coordinate-dependent residual predictor involving the continuum transfer envelope correlates more strongly with corrected empirical residual magnitude than height alone.

---

## CL-0182

**Status:** PROJECT RESEARCH QUESTION

**Statement:** Does the deterministic response-transfer envelope provide explanatory power for actual signed zero-counting residuals, or is it primarily a loose worst-case stability bound?

**Priority:** CRITICAL.

**Status:** OPEN.

---

## CL-0183

**Status:** COMPUTATIONAL VALIDATION

**Statement:** The matched-scale exact transfer coefficient numerically converged to the continuum transfer envelope in all frozen Phase 5G validation cases.

**Prediction ID:** P-TRN-001.

**Result:** PASS.

---

## CL-0184

**Status:** COMPUTATIONAL VALIDATION OF PROVED INEQUALITY

**Statement:** The deterministic sup-norm counting-response transfer certificate passed at all 360 tested dense-window decomposition points.

**Pass rate:** 1.0.

**Prediction ID:** P-TRN-002.

**Result:** PASS.

---

## CL-0185

**Status:** COMPUTATIONAL OBSERVATION

**Statement:** The L2 Holder transfer certificate was tighter than the L-infinity variation certificate at all 360 tested dense-window points.

**L2 tighter rate:** 1.0.

**No general certificate-ordering theorem is claimed.**

---

## CL-0186

**Status:** PROJECT PREDICTION SCORE

**Prediction ID:** P-TRN-003.

**Result:** PASS.

---

## CL-0187

**Status:** COMPUTATIONAL OBSERVATION

**Statement:** Across 108 corrected empirical response roots, the median profile-to-transfer ratio was approximately
\[
7.3711\times10^{-5}.
\]

Across 1008 generic coordinates at least 0.5 away from every empirical root in the same window, the median ratio was approximately
\[
7.1325\times10^{-3}.
\]

The root-to-generic median ratio was approximately
\[
0.0103346.
\]

---

## CL-0188

**Status:** PROJECT PREDICTION SCORE

**Prediction ID:** P-TRN-004.

**Result:** PASS.

**Statement:** Empirical response-root neighborhoods exhibited substantially lower profile-to-transfer ratio than generic coordinates under the frozen comparison protocol.

---

## CL-0189

**Status:** COMPUTATIONAL OBSERVATION

**Statement:** The natural-log correlation between corrected normalized counting-remainder magnitude and the continuum transfer predictor was approximately
\[
0.848764.
\]

The corresponding correlation with the height-only predictor \(1/H\) was approximately
\[
0.394907.
\]

The correlation difference was approximately
\[
0.453858.
\]

---

## CL-0190

**Status:** PROJECT PREDICTION SCORE — HIGH-RISK PREDICTION

**Prediction ID:** P-TRN-005.

**Result:** PASS.

**Statement:** The coordinate-dependent continuum transfer predictor had greater empirical explanatory correlation with corrected counting-remainder magnitude than the frozen height-only baseline.

---

## CL-0191

**Status:** COMPUTATIONAL OBSERVATION

**Statement:** In the tested corrected finite data, the deterministic response-transfer envelope was not merely a valid worst-case certificate; a predictor incorporating its coordinate dependence showed substantial empirical explanatory power for residual magnitude.

**Scope:** Phase 5G protocol and first-500-zero dataset.

**Not a theorem of:** sharp signed fluctuation prediction.

---

## CL-0192

**Status:** FAILED CLAIM PREVENTION RULE

**Statement:** The 360/360 empirical superiority of the L2 certificate must not be generalized to a universal theorem that the L2 Holder certificate is always tighter than the L-infinity variation certificate.

---

## CL-0193

**Status:** PROJECT RESEARCH QUESTION

**Statement:** Can a signed or dual-norm transfer model retain cancellation information discarded by \(\mathcal L_\eta(c)\) and improve empirical prediction beyond the absolute-value continuum transfer predictor?

**Priority:** CRITICAL.

**Status:** OPEN.

---

## CL-0194

**Status:** PROJECT RESEARCH QUESTION

**Statement:** Does the large separation between empirical-root and generic-coordinate Q values persist at substantially higher zero heights and under alternative window-width protocols?

**Priority:** HIGH.

**Status:** OPEN.

---

## CL-0195

**Status:** PRIOR-ART AUDIT REQUIRED

**Statement:** Before describing the \((\Phi_\eta,\mathcal L_\eta,Q_\eta)\) response architecture as original or novel, the project must audit prior work on explicit-formula test-function norms, zero-counting discrepancy transfer, bounded-variation Stieltjes estimates, and stability of Li/Keiper-type zero sums.

**Priority:** CRITICAL.

---

## CL-0196

**Status:** PRIOR-ART AUDIT PROTOCOL

**Statement:** The exact Stieltjes and bounded-variation mechanisms underlying the Phase 5F transfer inequality are presumed standard pending precise historical attribution.

---

## CL-0197

**Status:** ORIGINALITY UNRESOLVED

**Statement:** The originality status of the positive-width Li response profile Phi_eta is unresolved and requires targeted primary-source review.

---

## CL-0198

**Status:** ORIGINALITY UNRESOLVED

**Statement:** The originality status of the Li-specific continuum transfer envelope L_eta is unresolved.

---

## CL-0199

**Status:** ORIGINALITY UNRESOLVED

**Statement:** The project-defined profile-to-transfer ratio Q_eta must be compared with explicit-formula test-function optimization, dual-norm stability ratios, and zero-statistic discrepancy literature.

---

## CL-0200

**Status:** NOVELTY QUARANTINE

**Statement:** The combined architecture
\[
(\Psi_{Li},\Phi_\eta,\mathcal L_\eta,Q_\eta)
\]
must not be called novel, new theory, or progress toward proving RH before the Phase 6 prior-art audit is completed.

---

## CL-0201

**Status:** KNOWN PROJECT LIMITATION

**Statement:** As of Phase 6A, the project has no new RH-equivalent criterion, Li positivity theorem, zero-free region, exclusion theorem for off-critical zeros, or proof of RH.

---

## CL-0202

**Status:** PRIOR-ART RESEARCH QUESTION

**Statement:** Does prior Li/Keiper literature explicitly study differential response of zero-side contributions to zero-coordinate displacement followed by positive-width height-window aggregation?

**Priority:** CRITICAL.

---

## CL-0203

**Status:** PRIOR-ART RESEARCH QUESTION

**Statement:** Does prior explicit-formula or zero-statistic literature contain a mathematically equivalent specialization of the Li continuum transfer envelope or profile-to-transfer ratio?

**Priority:** CRITICAL.

---

## CL-0204

**Status:** PRIOR-ART DISPOSITION

**Source:** K. D. Maślanka, "Analytic Extension of Keiper-Li Coefficients" (2022), arXiv:2211.08993.

**Question:** Q9.

**PA Grade:** PA-2 — CONCEPTUAL OVERLAP.

**Statement:** Maślanka studies Keiper-Li structures through the standard zero-side representation and considers response to hypothetical altered zeta-zero geometry. The paper's explicit random perturbation experiment perturbs zeros of the analytically extended Keiper-Li entire function rather than Riemann zeta zero coordinates.

**Difference from project:** No zero-coordinate derivative, symmetry-preserving quadratic response, Li susceptibility profile, matched n/gamma scaling, or positive-width response aggregation was identified.

**Disposition:** Broad claims that Li/Keiper zero sensitivity is unprecedented are prohibited. The specific differential response construction remains originality unresolved.

---

## CL-0205

**Status:** PRIOR-ART DISPOSITION — STRONG STRUCTURAL OVERLAP

**Source family:** André Voros, Keiper-Li asymptotic and discretized criteria papers.

**Question:** Q9.

**PA Grade:** PA-3.

**Statement:** Voros explicitly studies the large-index sensitivity of Keiper-Li quantities to off-critical zero locations. Using the conformal zero coordinate
\[
z_\rho=1-1/\rho,
\]
his asymptotic analysis describes exponentially growing oscillatory signals from zeros with real part greater than one half and gives detectability scales depending on the zero height and horizontal displacement.

**Disposition:** Broad claims that the project discovered Li/Keiper sensitivity to altered zero geometry are prohibited.

---

## CL-0206

**Status:** PRIOR-ART DISTINCTION

**Statement:** The finite differences in Voros's discretized Keiper-Li constructions replace derivatives or degenerate contour poles by evaluations at distinct basepoints. They are not the same mathematical operation as a symmetry-preserving second finite difference in the zeta zero coordinate.

---

## CL-0207

**Status:** ORIGINALITY UNRESOLVED — NARROWED Q9 OBJECT

**Statement:** No source inspected in the Phase 6B Q9 campaign has yet been identified that explicitly develops the local symmetry-preserving second zero-coordinate variation
\[
f_n(\rho+\delta)+f_n(\rho-\delta)-2f_n(\rho),
\]
the susceptibility
\[
2\Re f_n''(\rho),
\]
its matched \(n/\gamma\) response profile, and subsequent positive-width height-window aggregation.

**Disposition:** This is an absence-of-identification statement only. It is not a novelty claim.

---

## CL-0208

**Status:** PRIOR-ART DISPOSITION

**Source:** Frederik Salzmann, "A Curvature-Minimum Reformulation of the Riemann Hypothesis" (2026).

**Question:** Q9.

**PA Grade:** PA-2.

**Statement:** Symmetry-centered second-derivative and curvature analysis of xi-derived functions exists in prior work. Salzmann differentiates |xi(sigma+it)|^2 with respect to the evaluation coordinate sigma.

**Distinction:** This does not equal differentiation of an individual Li zero-side kernel with respect to a zeta zero coordinate.

---

## CL-0209

**Status:** PRIOR-ART DISPOSITION — STRONG STRUCTURAL OVERLAP

**Source:** Matthew J. Goss, Jr., UMR v6.16 (2026).

**Question:** Q9.

**PA Grade:** PA-3.

**Statement:** Local geometric response to horizontal displacement of symmetric off-line zero pairs, including quadratic small-displacement behavior, is present in prior work.

**Disposition:** The project must not describe symmetric zero-pair displacement response or quadratic zero-displacement analysis as unprecedented.

---

## CL-0210

**Status:** ORIGINALITY UNRESOLVED — FURTHER NARROWED Q9 OBJECT

**Statement:** After the current Q9 search campaign, no inspected source has been identified that explicitly develops the Li-kernel-specific susceptibility
\[
2\Re f_n''(1/2+i\gamma),
\]
its exact n and gamma formula, its matched n/gamma profile Psi_Li, and its positive-width susceptibility aggregation.

**Disposition:** Absence of an identified PA-4 source is not a novelty conclusion.

---

## CL-0211

**Status:** PRIOR-ART DISPOSITION

**Source:** Emmerson and Buchanan, truncated quasiconformal energy for the Riemann xi-function, 2026.

**Question:** Q10.

**PA Grade:** PA-2.

**Statement:** Finite height-window analysis and windowed deformation of symmetric zeta-zero pairs exists in prior work.

**Disposition:** Broad claims that the project introduced height-windowed zero deformation are prohibited.

---

## CL-0212

**Status:** STANDARD-MECHANISM PRESUMPTION

**Statement:** Replacing a zero statistic by a leading continuum integral using the Riemann-von Mangoldt density is presumed standard analytic machinery.

**Disposition:** The project does not claim originality for the smooth-density substitution.

---

## CL-0213

**Status:** ORIGINALITY UNRESOLVED — Q10 OBJECT

**Statement:** No source inspected in the current Q10 campaign has been identified that derives the positive-width multiplicative Li susceptibility profile
\[
\Phi_\eta(c)
=
\frac{1}{2\pi}
\int_1^{1+\eta}
u^{-2}\Psi_{Li}(c/u)\,du
\]
or its equivalent sine closed form from the local Li zero-coordinate susceptibility.

**Disposition:** No PA-4 source identified in the current source set. This is not a novelty claim.

---

## CL-0214

**Status:** PRIOR-ART CORRECTION

**Statement:** The broad coupled Li index/zero-height phase is established prior art.

**Evidence:** Classical and generalized Li zero contributions contain phases equivalent to
\[
n\arctan(1/(2\gamma)),
\]
so a finite high-zero phase under fixed \(n/\gamma\) is structurally present in prior work.

**Disposition:** The project must not claim discovery of the general \(n/\gamma\) Li scaling variable.

---

## CL-0215

**Status:** PRIOR-ART DISPOSITION — PA-3

**Source:** Juan Arias de Reyna, "Asymptotics of Keiper-Li Coefficients" (2011).

**Statement:** Arias de Reyna writes the critical-line Li zero sum using
\[
\sin^2(m\arctan(1/(2\gamma)))
\]
and converts the zero sum into a Stieltjes integral against \(dN(t)\), decomposed into smooth zero density and counting remainder.

**Disposition:** Li-kernel index/height phase and zero-density integration are strong structural prior art.

---

## CL-0216

**Status:** PRIOR-ART DISPOSITION — PA-3

**Source family:** Chebyshev integral representations of Li coefficients, including Mazhouda-Smajlović and the formal He-Jejjala-Minic treatment.

**Statement:** Li coefficients admit counting-function or zero-side representations involving Chebyshev kernels whose oscillatory phase is equivalent to
\[
n\arctan(1/(2\gamma)).
\]

**Disposition:** Broad matched Li index/height phase language is prohibited.

---

## CL-0217

**Status:** PRIOR-ART DISPOSITION

**Statement:** Incomplete Li coefficients truncated to \(|\Im\rho|<T\), including index-dependent choices such as \(T=\sqrt n\), exist in the generalized Li literature.

**Disposition:** Finite-height truncation of Li zero sums is prior art.

---

## CL-0218

**Status:** ORIGINALITY UNRESOLVED — NARROWED Q10 OBJECT

**Statement:** No inspected source has yet been identified that applies positive-width multiplicative height-window aggregation to the local second zero-coordinate susceptibility
\[
\chi_n^{Li}(\gamma)=2\Re f_n''(1/2+i\gamma)
\]
and derives the exact profile
\[
\Phi_\eta(c)
=
\frac c\pi
\left[
(1+\eta)^{-2}\sin(c/(1+\eta))
-
\sin c
\right].
\]

**Disposition:** No PA-4 source identified in the current audit. This is not a novelty claim.

---

## CL-0219

**Status:** PRIOR-ART DISPOSITION — PA-3

**Source:** Sergey K. Sekatskii, generalized Li criterion.

**Statement:** Parameterized individual Li-type zero kernels are prior art. The family
\[
1-
\left(
\frac{\rho-a}{\rho+a-1}
\right)^n
\]
contains the classical Li zero kernel exactly at \(a=1\).

**Disposition:** The project must not claim discovery of parameterized Li-kernel deformation.

---

## CL-0220

**Status:** PRIOR-ART DISTINCTION

**Statement:** Variation of Sekatskii's parameter \(a\) is not the same differential direction as variation of the zero coordinate \(\rho\).

**Disposition:** No inspected Sekatskii result has been identified that computes the rho-coordinate second derivative of the fixed classical Li zero kernel.

---

## CL-0221

**Status:** PRIOR-ART DISPOSITION — PA-3

**Source family:** Modified tau-Li criteria for symmetrically shifted products \(F(s-a)F(s+a)\).

**Statement:** Symmetric global zero-set shifts inside Li-type constructions are prior art.

**Disposition:** Broad symmetric zero-shift Li-response language is prohibited.

---

## CL-0222

**Status:** ORIGINALITY UNRESOLVED — PRECISION OBJECT

**Statement:** No inspected source has been identified that explicitly develops the zero-coordinate Hessian
\[
f_n''(\rho)
=
\lim_{\delta\to0}
\frac{
f_n(\rho+\delta)+f_n(\rho-\delta)-2f_n(\rho)
}{
\delta^2
}
\]
for the fixed classical Li kernel and then derives the critical-line susceptibility, matched susceptibility profile, and positive-width multiplicative-window profile.

**Disposition:** No PA-4 source identified in the current search set. This remains an absence-of-identification statement only.


---

## CL-0223

**Status:** ADVERSARIAL AUDIT — UNDERJUSTIFIED PROOF DEPENDENCY

**Statement:** CL-0173 was initially labeled PROVED IN PROJECT before the derivative asymptotic required for the total-variation term had been established directly.

The susceptibility expansion alone does not justify differentiating its big-O remainder.

**Disposition:** Numerical Phase 5G convergence does not close this proof dependency.

---

## CL-0224

**Status:** PROVED IN PROJECT

**Statement:** Uniformly for

\[
q=n/\gamma
\]

in a compact positive set,

\[
\gamma^3\chi_n'(\gamma)
=
-J_{Li}(q)
+
O_K(\gamma^{-2}).
\]

**Proof method:** Direct reparameterization of the exact susceptibility derivative using

\[
x=1/\gamma,
\qquad
q=n/\gamma.
\]

The scaled exact derivative is smooth and even in \(x\) near \(x=0\), with value

\[
-J_{Li}(q)
\]

at \(x=0\).

---

## CL-0225

**Status:** PROVED IN PROJECT — REPAIRED DEPENDENCY

**Statement:** For fixed \(\eta>0\) and \(c_H=n/H\) in a compact positive set,

\[
H^2\Lambda_n(H,\eta)
=
\mathcal L_\eta(c_H)
+
O(H^{-2})
\]

uniformly.

If \(c_H\to c>0\), then

\[
H^2\Lambda_n(H,\eta)
\to
\mathcal L_\eta(c).
\]

**Proof dependency:** CL-0224 and the inequality

\[
\big||a+r|-|a|\big|\le|r|.
\]

---

## CL-0226

**Status:** FAILURE-PREVENTION RULE

**Statement:** Numerical convergence can validate a proved asymptotic or expose a false prediction, but numerical convergence cannot repair a missing analytical proof dependency.

---

## CL-0227

**Status:** PRIOR-ART DISPOSITION — Q11

**Statement:** Bounded-variation test functions, variation-controlled approximation estimates, and explicit-formula applications to BV-type test classes are established prior art in zeta-zero and Li-related analysis.

**Sources inspected:** Smajlović; Rodgers; Maples–Rodgers.

**PA Grade:** PA-4 for the generic BV/TV transfer mechanism.

**Disposition:** The project claims no originality for controlling a discrepancy transform by endpoint magnitude and total variation.

---

## CL-0228

**Status:** ORIGINALITY UNRESOLVED — Q11 SPECIALIZATION

**Statement:** No inspected Q11 source has been identified that derives the matched-scale continuum envelope

\[
\mathcal L_\eta(c)
\]

as the scaled endpoint-plus-total-variation norm of the differentiated classical Li zero-coordinate susceptibility.

**Disposition:** No PA-4 source identified for the Li-specific specialization in the current source set. This is not a novelty claim.

---

## CL-0229

**Status:** PRIOR-ART DISPOSITION — PA-3

**Source:** Julius Stricker, "Spectral Visibility of Zeta Zeros on LHS of the Explicit Formula" (2026).

**Question:** Q12.

**Statement:** Matched-filter scoring, direct frequency-selective projection, window-stability analysis, and quantitative visibility of zeta-zero spectral modes exist in prior work.

**Disposition:** Broad matched-response or zeta-signal visibility language is prohibited as an originality claim.

---

## CL-0230

**Status:** PRIOR-ART DISPOSITION

**Statement:** The generic idea of comparing a zero-related signal with noise, fluctuation, instability, amplification, or an error scale is established broadly and is not originality-sensitive.

---

## CL-0231

**Status:** ORIGINALITY UNRESOLVED — Q12 PRECISION OBJECT

**Statement:** No inspected Q12 source has been identified that forms a quotient mathematically equivalent to

\[
Q_\eta(c)
=
\frac{|\Phi_\eta(c)|}{\mathcal L_\eta(c)},
\]

where the numerator is the smooth positive-width Li zero-coordinate susceptibility profile and the denominator is the matched-scale endpoint-plus-total-variation discrepancy-transfer envelope of the same susceptibility kernel.

**Disposition:** No PA-4 source identified in the current source set. This is not a novelty claim.

---

## CL-0232

**Status:** ADVERSARIAL INTERPRETATION AUDIT

**Statement:** At every exact smooth profile root with positive transfer envelope,

\[
\Phi_\eta(c)=0
\quad\Longrightarrow\quad
Q_\eta(c)=0.
\]

Therefore the Phase 5G observation that root-associated coordinates have much smaller Q_eta than generic coordinates is partly implied by the definition of Q_eta together with the already observed tracking of empirical roots by Phi_eta roots.

---

## CL-0233

**Status:** FAILURE-PREVENTION RULE

**Statement:** P-TRN-004 must not be described as independent evidence that profile roots are transfer-stable or as an independently predictive discovery.

**Permitted interpretation:** Q_eta is a comparative conditioning or relative-sensitivity descriptor. Its collapse near Phi_eta roots expresses vanishing smooth signal relative to a nonzero worst-case transfer envelope.

---

## CL-0234

**Status:** TERMINOLOGY DISCIPLINE

**Statement:** The project must distinguish:

1. empirical matched-filter visibility of zero frequencies;
2. explicit-formula residue amplification;
3. generic signal-to-noise ratios;
4. the deterministic Li-susceptibility profile-to-transfer quotient Q_eta.

These are related conceptually but are not mathematically interchangeable.

---

## CL-0235

**Status:** PRIOR-ART DISPOSITION

**Statement:** Vanishing leading terms, degeneracy-induced order changes, and exposure of higher-order asymptotic contributions are standard phenomena in perturbative and asymptotic analysis.

**Disposition:** The project claims no originality for the generic degeneracy mechanism.

---

## CL-0236

**Status:** PRIOR-ART DISPOSITION — PA-2

**Source:** Anderson, restricted Goldbach transfer analysis, 2026.

**Statement:** Main-term versus transferred-error comparison appears in adjacent analytic-number-theory work.

**Distinction:** The prior source studies persistence of a positive restricted-Goldbach main term under twisted-sum error, not vanishing of a smooth Li-susceptibility profile while a deterministic discrepancy-transfer envelope remains positive.

---

## CL-0237

**Status:** ORIGINALITY UNRESOLVED — Q13 PRECISION OBJECT

**Statement:** No inspected Q13 source has been identified that explicitly interprets zeros of the positive-width Li zero-coordinate susceptibility profile

\[
\Phi_\eta(c)
\]

through the simultaneous comparison

\[
\Phi_\eta(c)=0,
\qquad
\mathcal L_\eta(c)>0,
\]

or an equivalent deterministic Li-susceptibility response-to-transfer construction.

**Disposition:** No PA-4 source identified in the current Q13 source set. This is not a novelty claim.

---

## CL-0238

**Status:** TERMINOLOGY DISCIPLINE

**Statement:** The project-specific Q13 observation must be described as a specialization to the positive-width local Li-susceptibility aggregate.

Broad claims concerning discovery of degeneracy, cancellation sensitivity, vanishing-main-term instability, or error dominance are prohibited.

---

## CL-0239

**Status:** PHASE 5H DEFINITION

**Statement:** The empirical counting-response residual is decomposed as

\[
R_{\mathrm{count}}
=
R_{\mathrm{atom}}
+
R_{\mathrm{end}}
+
R_{\mathrm{int}},
\]

where

\[
R_{\mathrm{end}}
=
\chi_n(B)E_D(B)
-
\chi_n(H)E_D(H)
\]

and

\[
R_{\mathrm{int}}
=
-\int_H^B E_D(t)\chi_n'(t)dt.
\]

---

## CL-0240

**Status:** PHASE 5H DEFINITION

**Statement:** When the denominator is nonzero, define

\[
\kappa_{n,H,\eta}
=
\frac{
\int_H^B E_D(t)\chi_n'(t)dt
}{
\|E_D\|_2\|\chi_n'\|_2
}.
\]

By Cauchy-Schwarz,

\[
|\kappa_{n,H,\eta}|\le1.
\]

---

## CL-0241

**Status:** PROVED IN PROJECT / DEFINITIONAL IDENTITY

**Statement:**

\[
R_{\mathrm{int}}
=
-\kappa_{n,H,\eta}
\|E_D\|_2
\|\chi_n'\|_2.
\]

**Interpretive restriction:** This identity cannot be scored as empirical evidence that kappa predicts the interior residual.

---

## CL-0242

**Status:** PHASE 5H DEFINITION

**Statement:** Define the scalar cancellation coefficient

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

Whenever the denominator is positive,

\[
0\le C_{\mathrm{scalar}}\le1.
\]

---

## CL-0243

**Status:** FROZEN COMPUTATIONAL PREDICTION

**Prediction ID:** P-SGN-001.

**Statement:** Maximum signed decomposition closure error is below \(10^{-45}\).

---

## CL-0244

**Status:** FROZEN COMPUTATIONAL PREDICTION

**Prediction ID:** P-SGN-002.

**Statement:** Median empirical absolute alignment satisfies

\[
\operatorname{median}|\kappa|>0.05.
\]

---

## CL-0245

**Status:** FROZEN COMPUTATIONAL PREDICTION

**Prediction ID:** P-SGN-003.

**Statement:** The in-sample descriptive log-correlation of count-residual magnitude with

\[
P_\kappa
=
|\kappa|\|E_D\|_2\|\chi_n'\|_2
+
|R_{\mathrm{atom}}|
+
|R_{\mathrm{end}}|
\]

exceeds the corresponding correlation with

\[
P_{\mathrm{abs}}
=
\|E_D\|_2\|\chi_n'\|_2.
\]

---

## CL-0246

**Status:** FROZEN COMPUTATIONAL PREDICTION

**Prediction ID:** P-SGN-004.

**Statement:** At least 25 percent of dense-window coordinates satisfy

\[
C_{\mathrm{scalar}}<0.5.
\]

---

## CL-0247

**Status:** FROZEN COMPUTATIONAL PREDICTION

**Prediction ID:** P-SGN-005.

**Statement:** Absolute correlation between log deterministic-certificate tightness and log scalar cancellation exceeds the corresponding absolute correlation with log inverse height.

---

## CL-0248

**Status:** FAILURE-PREVENTION RULE

**Statement:** Phase 5H statistics computed from the same empirical zero-discrepancy window are in-sample descriptive quantities and must not be described as out-of-sample predictors.


---

## CL-0249

**Status:** COMPUTATIONAL OBSERVATION

**Prediction ID:** P-SGN-001.

**Result:** PASS.

**Statement:** Across 360 dense-window signed decompositions, the maximum stored signed closure error was zero at 60-digit working precision.

The maximum definitional identity error was approximately

\[
3.80\times10^{-65},
\]

and the maximum reconstruction discrepancy against the frozen Phase 5G non-atomic response was approximately

\[
6.08\times10^{-62}.
\]

**Interpretation:** Implementation validation only.

---

## CL-0250

**Status:** FAILED COMPUTATIONAL PREDICTION

**Prediction ID:** P-SGN-002.

**Result:** FAIL.

**Statement:** The frozen prediction

\[
\operatorname{median}|\kappa|>0.05
\]

failed.

Observed:

\[
\operatorname{median}|\kappa|
\approx
0.00722966.
\]

All 360 tested coordinates satisfied

\[
|\kappa|<0.05.
\]

**Disposition:** The strong interior-alignment hypothesis is not supported by the tested finite dataset.

---

## CL-0251

**Status:** COMPUTATIONAL OBSERVATION — FINITE-DATA QUALIFICATION

**Statement:** The observed kappa range was approximately

\[
[-0.0446977,0.0443058].
\]

The mean absolute alignment was approximately

\[
0.0106295.
\]

**Interpretation:** The empirical discrepancy and Li susceptibility derivative had small normalized \(L^2\) inner products across the tested dense windows.

**Restriction:** This does not prove asymptotic orthogonality, independence, or randomness.

---

## CL-0252

**Status:** COMPUTATIONAL OBSERVATION

**Prediction ID:** P-SGN-003.

**Result:** PASS WITH WEAK EFFECT.

**Statement:** The in-sample log-correlation with count-residual magnitude increased from approximately

\[
0.837459
\]

for \(P_{\mathrm{abs}}\) to

\[
0.841444
\]

for \(P_\kappa\).

The increase was approximately

\[
0.003985.
\]

**Disposition:** The frozen strict-greater-than rule passed, but the effect is marginal and must not be described as strong explanatory or predictive evidence.

---

## CL-0253

**Status:** COMPUTATIONAL OBSERVATION

**Prediction ID:** P-SGN-004.

**Result:** PASS STRONGLY.

**Statement:** The median scalar cancellation coefficient was approximately

\[
0.239756.
\]

Approximately

\[
74.44\%
\]

of tested coordinates had

\[
C_{\mathrm{scalar}}<0.5,
\]

and approximately

\[
51.39\%
\]

had

\[
C_{\mathrm{scalar}}<0.25.
\]

**Interpretation:** Signed cancellation among atom, endpoint, and interior response components is common and quantitatively material in the tested finite population.

---

## CL-0254

**Status:** COMPUTATIONAL OBSERVATION

**Prediction ID:** P-SGN-005.

**Result:** PASS STRONGLY.

**Statement:** The observed log-correlation between sup-certificate tightness and scalar cancellation was approximately

\[
0.918758,
\]

versus approximately

\[
0.200653
\]

for inverse height.

**Interpretation:** In the tested finite dataset, scalar cancellation is substantially more strongly associated with deterministic certificate tightness than height alone.

**Restriction:** In-sample descriptive association only.

---

## CL-0255

**Status:** PROJECT DIRECTION CORRECTION

**Statement:** Phase 5H does not support strong \(E_D\)-versus-\(\chi_n'\) interior alignment as the principal explanation for signed response size.

The next research question should analyze the joint sign and magnitude geometry of

\[
R_{\mathrm{atom}},
\qquad
R_{\mathrm{end}},
\qquad
R_{\mathrm{int}}.
\]

---

## CL-0256

**Status:** FAILURE-PREVENTION RULE

**Statement:** A failed frozen prediction must redirect the research program when the observed data contradict the proposed mechanism.

The project will not reinterpret the small observed kappa values as evidence for strong alignment.


---

## CL-0257

**Status:** PHASE 5I DEFINITION

**Statement:** Phase 5I classifies each non-boundary signed response triple

\[
(R_{\mathrm{atom}},R_{\mathrm{end}},R_{\mathrm{int}})
\]

into one of eight sign chambers.

The frozen zero-sign tolerance is

\[
10^{-50}.
\]

---

## CL-0258

**Status:** PROVED IN PROJECT — ELEMENTARY

**Statement:** If

\[
R_{\mathrm{atom}},
R_{\mathrm{end}},
R_{\mathrm{int}}
\]

all have the same sign and are nonzero, then

\[
C_{\mathrm{scalar}}=1.
\]

**Proof:** Equality holds in the scalar triangle inequality for same-sign real summands.

---

## CL-0259

**Status:** FROZEN COMPUTATIONAL PREDICTION

**Prediction ID:** P-CHM-001.

**Statement:** All 360 Phase 5H points occupy exactly one of the eight non-boundary sign chambers under the \(10^{-50}\) tolerance.

---

## CL-0260

**Status:** FROZEN COMPUTATIONAL PREDICTION

**Prediction ID:** P-CHM-002.

**Statement:** Every same-sign chamber point satisfies

\[
|C_{\mathrm{scalar}}-1|<10^{-45}.
\]

---

## CL-0261

**Status:** FROZEN COMPUTATIONAL PREDICTION

**Prediction ID:** P-CHM-003.

**Statement:** At least 95 percent of points with

\[
C_{\mathrm{scalar}}<0.25
\]

lie in mixed-sign chambers.

---

## CL-0262

**Status:** FROZEN COMPUTATIONAL PREDICTION

**Prediction ID:** P-CHM-004.

**Statement:** Among mixed-sign chambers with at least 10 points, the range of conditional extreme-cancellation rates exceeds 0.25.

---

## CL-0263

**Status:** FROZEN COMPUTATIONAL PREDICTION

**Prediction ID:** P-CHM-005.

**Statement:** At least one sign chamber has bottom-quartile deterministic-certificate-looseness enrichment exceeding 1.5.

---

## CL-0264

**Status:** FROZEN COMPUTATIONAL PREDICTION

**Prediction ID:** P-CHM-006.

**Statement:** Mean chamber-transition count across the 18 frozen windows exceeds 5 transitions per 19 adjacent c-grid steps.

---

## CL-0265

**Status:** FROZEN COMPUTATIONAL PREDICTION

**Prediction ID:** P-CHM-007.

**Statement:** Median scalar cancellation is lower for points within one c-grid step of a chamber transition than for points at least three c-grid steps from the nearest transition.

---

## CL-0266

**Status:** FAILURE-PREVENTION RULE

**Statement:** Sign-chamber classification is derived from the response components themselves.

Algebraic consequences of the sign labels must not be presented as independent empirical evidence.


---

## CL-0267

**Status:** COMPUTATIONAL OBSERVATION

**Prediction ID:** P-CHM-001.

**Result:** PASS.

**Statement:** All 360 Phase 5H points occupied one of the eight non-boundary sign chambers under the frozen \(10^{-50}\) tolerance.

---

## CL-0268

**Status:** COMPUTATIONAL VALIDATION / ELEMENTARY CONSEQUENCE

**Prediction ID:** P-CHM-002.

**Result:** PASS.

**Statement:** All eight same-sign points satisfied

\[
C_{\mathrm{scalar}}=1
\]

to stored precision.

**Interpretation:** Algebraic and implementation validation only.

---

## CL-0269

**Status:** COMPUTATIONAL OBSERVATION — DEFINITION-DRIVEN QUALIFICATION

**Prediction ID:** P-CHM-003.

**Result:** PASS.

**Statement:** All 185 extreme-cancellation points were mixed-sign.

**Qualification:** This is largely implied by the same-sign identity \(C_{\mathrm{scalar}}=1\).

---

## CL-0270

**Status:** FAILED COMPUTATIONAL PREDICTION

**Prediction ID:** P-CHM-004.

**Result:** FAIL.

**Statement:** Among eligible mixed-sign chambers, the observed range of extreme-cancellation rates was approximately

\[
0.09242,
\]

below the frozen threshold of

\[
0.25.
\]

**Disposition:** Coarse mixed-chamber identity did not strongly discriminate cancellation propensity in the tested population.

---

## CL-0271

**Status:** FAILED COMPUTATIONAL PREDICTION

**Prediction ID:** P-CHM-005.

**Result:** FAIL.

**Statement:** Maximum observed bottom-quartile certificate-looseness chamber enrichment was approximately

\[
1.3012,
\]

below the frozen threshold of

\[
1.5.
\]

**Disposition:** No chamber was strongly enriched under the frozen rule.

---

## CL-0272

**Status:** COMPUTATIONAL OBSERVATION

**Prediction ID:** P-CHM-006.

**Result:** PASS STRONGLY.

**Statement:** Mean chamber transitions per frozen 19-step c-window were approximately

\[
12.3333.
\]

Median transitions were

\[
13.
\]

**Interpretation:** Signed response chamber changes are frequent on the tested integer c-grid.

**Restriction:** No chaos or randomness claim follows.

---

## CL-0273

**Status:** FAILED COMPUTATIONAL PREDICTION — NON-DISCRIMINATING OPERATIONALIZATION

**Prediction ID:** P-CHM-007.

**Result:** FAIL.

**Statement:** The observed transition density produced 357 near-transition points and zero far-transition points under the frozen distance categories.

**Disposition:** The test could not compare near and far populations.

No post-hoc threshold modification is permitted.

The failure does not establish either presence or absence of a transition-proximity cancellation effect.

---

## CL-0274

**Status:** PROJECT DIRECTION CORRECTION

**Statement:** Phase 5I shows that sign-chamber labels alone are too coarse to explain scalar cancellation severity.

The next phase should retain normalized component magnitudes through the simplex coordinates

\[
(a,e,i)
=
\frac{
(|R_{\mathrm{atom}}|,|R_{\mathrm{end}}|,|R_{\mathrm{int}}|)
}{
|R_{\mathrm{atom}}|+|R_{\mathrm{end}}|+|R_{\mathrm{int}}|
}.
\]

---

## CL-0275

**Status:** FAILURE-PREVENTION RULE

**Statement:** A post-hoc redefinition of near and far transition thresholds is prohibited for the Phase 5I scorecard.

A future transition analysis may define a new protocol and freeze new rules before inspecting new derived results.

