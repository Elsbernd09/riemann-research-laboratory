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
