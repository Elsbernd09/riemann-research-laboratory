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
