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
