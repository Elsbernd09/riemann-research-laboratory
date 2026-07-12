# Phase 12B Source Scan Report

## Purpose

Search local project files for previously extracted Bombieri/Weil source objects.

## Top hits

### research_ledger/CLAIM_LEDGER.md

score: 11

```text
71: **Status:** FAILED CLAIM PREVENTION RULE
72: 
73: **Statement:** Numerical positivity of finitely many Li coefficients does not establish positivity for all Li coefficients.
74: 
75: **Purpose:** Prevent finite computation from being mislabeled as a universal theorem.
```

```text
560: **Status:** KNOWN PROJECT LIMITATION
561: 
562: **Statement:** As of Phase 3A, the project has no established Level IV RH-relevant consequence such as a new equivalent criterion, zero-free region, positivity theorem, or exclusion of off-critical zeros.
563: 
564: ---
```

```text
692: **Statement:** Abstract multiset or signed zero-configuration language is project-originating infrastructure.
693: 
694: **Failure:** Bombieri-Lagarias formulate Li-type criteria for arbitrary complex multisets with convergence and symmetry conditions.
695: 
696: **Disposition:** Cite Bombieri-Lagarias as foundational multiset context.
```

```text
694: **Failure:** Bombieri-Lagarias formulate Li-type criteria for arbitrary complex multisets with convergence and symmetry conditions.
695: 
696: **Disposition:** Cite Bombieri-Lagarias as foundational multiset context.
697: 
698: ---
```

```text
2499: **Status:** KNOWN PROJECT LIMITATION
2500: 
2501: **Statement:** As of Phase 6A, the project has no new RH-equivalent criterion, Li positivity theorem, zero-free region, exclusion theorem for off-critical zeros, or proof of RH.
2502: 
2503: ---
```

### scripts/run_phase12b_source_scan.py

score: 11

```text
3: 
4: ROOT = Path(".")
5: OUT = Path("original_results/finite_bombieri_stability/level4_candidate/true_weil_form_import")
6: OUT.mkdir(parents=True, exist_ok=True)
7: 
```

```text
7: 
8: patterns = [
9:     "T[f]",
10:     "T[f^*]",
11:     "sum_\\rho",
```

```text
8: patterns = [
9:     "T[f]",
10:     "T[f^*]",
11:     "sum_\\rho",
12:     "sum\\_rho",
```

```text
9:     "T[f]",
10:     "T[f^*]",
11:     "sum_\\rho",
12:     "sum\\_rho",
13:     "Bombieri",
```

```text
10:     "T[f^*]",
11:     "sum_\\rho",
12:     "sum\\_rho",
13:     "Bombieri",
14:     "Weil",
```

### weil_reconstruction/sources/CONVENTION_LOCK_TABLE.md

score: 11

```text
1: # Convention Lock Table
2: 
3: This table must be filled before implementing any exact Weil quadratic form.
4: 
5: | Object | Chosen convention | Source | Status |
```

```text
5: | Object | Chosen convention | Source | Status |
6: |---|---|---|---|
7: | Primary reconstruction path | Bombieri-style Weil quadratic form | Bombieri source card | LOCKED |
8: | Primary source section | Bombieri Sections 2 and 3 | Bombieri extraction cards | LOCKED |
9: | Weil positivity as RH-equivalent framework | Positive semidefinite Weil quadratic functional iff RH | Bombieri / Suzuki source cards | LOCKED |
```

```text
6: |---|---|---|---|
7: | Primary reconstruction path | Bombieri-style Weil quadratic form | Bombieri source card | LOCKED |
8: | Primary source section | Bombieri Sections 2 and 3 | Bombieri extraction cards | LOCKED |
9: | Weil positivity as RH-equivalent framework | Positive semidefinite Weil quadratic functional iff RH | Bombieri / Suzuki source cards | LOCKED |
10: | Primary test-function ambient space | \(C_0^\infty((0,\infty))\) | Bombieri Theorem 1 and 2 cards | LOCKED |
```

```text
7: | Primary reconstruction path | Bombieri-style Weil quadratic form | Bombieri source card | LOCKED |
8: | Primary source section | Bombieri Sections 2 and 3 | Bombieri extraction cards | LOCKED |
9: | Weil positivity as RH-equivalent framework | Positive semidefinite Weil quadratic functional iff RH | Bombieri / Suzuki source cards | LOCKED |
10: | Primary test-function ambient space | \(C_0^\infty((0,\infty))\) | Bombieri Theorem 1 and 2 cards | LOCKED |
11: | Involution | \(f^*(x)=x^{-1}f(1/x)\) | Bombieri Section 2 | LOCKED |
```

```text
8: | Primary source section | Bombieri Sections 2 and 3 | Bombieri extraction cards | LOCKED |
9: | Weil positivity as RH-equivalent framework | Positive semidefinite Weil quadratic functional iff RH | Bombieri / Suzuki source cards | LOCKED |
10: | Primary test-function ambient space | \(C_0^\infty((0,\infty))\) | Bombieri Theorem 1 and 2 cards | LOCKED |
11: | Involution | \(f^*(x)=x^{-1}f(1/x)\) | Bombieri Section 2 | LOCKED |
12: | Mellin transform | \(f(s)=\int_0^\infty f(x)x^{s-1}dx\) | Bombieri Section 2 | LOCKED |
```

### research_ledger/PHASE_LEDGER.md

score: 9

```text
2741: None.
2742: 
2743: The project has no new RH-equivalent criterion, positivity theorem, zero-free region, exclusion theorem for off-critical zeros, or proof of RH.
2744: 
2745: ### Current frontier
```

```text
4217: ### Next required action
4218: 
4219: Targeted prior-art audit of classical integrated zero-counting remainders, \(S(T)\), \(S_1(T)\), Littlewood-type bounds, and repeated-integration smoothing of the explicit formula.
4220: 
4221: ### RH consequence
```

```text
4754: dN_{w_2}(t)
4755: =
4756: \sum_\rho
4757: \left(
4758: \Re\rho-\frac12
```

```text
4791: ---
4792: 
4793: ## Phase 5Q — Linear Li-Filter Positivity Obstruction
4794: 
4795: Status: COMPLETE
```

```text
4954: ### Next required audit
4955: 
4956: Weil positivity.
4957: 
4958: Guinand–Weil explicit formula.
```

### weil_reconstruction/sources/extractions/PHASE_8H_FULL_T_FUNCTIONAL_EXTRACTION.md

score: 9

```text
1: # Phase 8H — Full Bombieri T[f] Formula Extraction
2: 
3: ## Purpose
```

```text
3: ## Purpose
4: 
5: Phase 8G created the extraction worksheet for Bombieri's full linear functional
6: 
7: \[
```

```text
6: 
7: \[
8: T[f].
9: \]
10: 
```

```text
9: \]
10: 
11: Phase 8H fills the worksheet from Bombieri's source text.
12: 
13: This is not a proof of RH.
```

```text
13: This is not a proof of RH.
14: 
15: This is not a new Weil criterion.
16: 
17: This is a source-grounded extraction of a known classical formula.
```

### weil_reconstruction/sources/extractions/PHASE_8F_BOMBIERI_THEOREM_EXTRACTION.md

score: 8

```text
1: # Phase 8F — Bombieri Theorem 1 and Theorem 2 Extraction
2: 
3: ## Purpose
```

```text
3: ## Purpose
4: 
5: Phase 8E locked only high-level structural facts from Bombieri and Suzuki.
6: 
7: Phase 8F extracts the first exact theorem-level objects from Bombieri's Section 3.
```

```text
5: Phase 8E locked only high-level structural facts from Bombieri and Suzuki.
6: 
7: Phase 8F extracts the first exact theorem-level objects from Bombieri's Section 3.
8: 
9: This is not a proof of RH.
```

```text
9: This is not a proof of RH.
10: 
11: This is not a new Weil criterion.
12: 
13: This is a reconstruction of known classical source material.
```

```text
17: # 1. Source
18: 
19: Enrico Bombieri, **Remarks on Weil's quadratic functional in the theory of prime numbers, I**, Rend. Mat. Acc. Lincei, Serie 9, Vol. 11, 183-233, 2000.
20: 
21: Relevant section:
```

### weil_reconstruction/sources/extractions/PHASE_8G_T_FUNCTIONAL_EXTRACTION_WORKSHEET.md

score: 8

```text
1: # Phase 8G — Full T[f] Functional Extraction Worksheet
2: 
3: ## Purpose
```

```text
3: ## Purpose
4: 
5: Phase 8F extracted Bombieri Theorem 1 and Theorem 2 at statement level.
6: 
7: The next task is to extract the exact full formula for Bombieri's linear functional
```

```text
5: Phase 8F extracted Bombieri Theorem 1 and Theorem 2 at statement level.
6: 
7: The next task is to extract the exact full formula for Bombieri's linear functional
8: 
9: \[
```

```text
8: 
9: \[
10: T[f].
11: \]
12: 
```

```text
17: This is not a proof of RH.
18: 
19: This is not a new Weil criterion.
20: 
21: This is not a novelty claim.
```

### weil_reconstruction/sources/extractions/T_FUNCTIONAL_EXTRACTED_FORMULA.md

score: 8

```text
1: # Extracted Bombieri T[f] Formula
2: 
3: ## Function class
```

```text
10: 
11: \[
12: f^*(x)=\frac1x f\left(\frac1x\right).
13: \]
14: 
```

```text
13: \]
14: 
15: ## Mellin transform
16: 
17: \[
```

```text
22: 
23: \[
24: T[f]
25: =
26: \int_0^\infty f(x)\,dx
```

```text
26: \int_0^\infty f(x)\,dx
27: +
28: \int_0^\infty f^*(x)\,dx
29: -
30: \sum_{n=1}^{\infty}
```

### scripts/audit_phase8h_full_t_functional.py

score: 7

```text
2: 
3: files = [
4:     Path("weil_reconstruction/sources/extractions/PHASE_8H_FULL_T_FUNCTIONAL_EXTRACTION.md"),
5:     Path("weil_reconstruction/sources/extractions/T_FUNCTIONAL_EXTRACTED_FORMULA.md"),
6:     Path("weil_reconstruction/sources/extractions/T_FUNCTIONAL_TERM_TABLE.md"),
```

```text
3: files = [
4:     Path("weil_reconstruction/sources/extractions/PHASE_8H_FULL_T_FUNCTIONAL_EXTRACTION.md"),
5:     Path("weil_reconstruction/sources/extractions/T_FUNCTIONAL_EXTRACTED_FORMULA.md"),
6:     Path("weil_reconstruction/sources/extractions/T_FUNCTIONAL_TERM_TABLE.md"),
7:     Path("weil_reconstruction/sources/extractions/T_FUNCTIONAL_LOCK_REQUIREMENTS.md"),
```

```text
4:     Path("weil_reconstruction/sources/extractions/PHASE_8H_FULL_T_FUNCTIONAL_EXTRACTION.md"),
5:     Path("weil_reconstruction/sources/extractions/T_FUNCTIONAL_EXTRACTED_FORMULA.md"),
6:     Path("weil_reconstruction/sources/extractions/T_FUNCTIONAL_TERM_TABLE.md"),
7:     Path("weil_reconstruction/sources/extractions/T_FUNCTIONAL_LOCK_REQUIREMENTS.md"),
8:     Path("weil_reconstruction/sources/CONVENTION_LOCK_TABLE.md"),
```

```text
5:     Path("weil_reconstruction/sources/extractions/T_FUNCTIONAL_EXTRACTED_FORMULA.md"),
6:     Path("weil_reconstruction/sources/extractions/T_FUNCTIONAL_TERM_TABLE.md"),
7:     Path("weil_reconstruction/sources/extractions/T_FUNCTIONAL_LOCK_REQUIREMENTS.md"),
8:     Path("weil_reconstruction/sources/CONVENTION_LOCK_TABLE.md"),
9: ]
```

```text
6:     Path("weil_reconstruction/sources/extractions/T_FUNCTIONAL_TERM_TABLE.md"),
7:     Path("weil_reconstruction/sources/extractions/T_FUNCTIONAL_LOCK_REQUIREMENTS.md"),
8:     Path("weil_reconstruction/sources/CONVENTION_LOCK_TABLE.md"),
9: ]
10: 
```

### weil_reconstruction/objects/OBJECT_GLOSSARY.md

score: 7

```text
36: 
37: \[
38: \sum_\rho h(\rho).
39: \]
40: 
```

```text
43: ## Test function
44: 
45: An admissible function used in an explicit formula.
46: 
47: Temporary notation:
```

```text
57: ## Transform
58: 
59: A Fourier/Mellin-type operation on the test function.
60: 
61: Temporary notation:
```

```text
69: ---
70: 
71: ## Explicit formula
72: 
73: A formula relating zero-side data to prime-side/arithmetic-side data.
```

```text
75: ---
76: 
77: ## Weil quadratic form
78: 
79: A quadratic functional
```

### weil_reconstruction/objects/PHASE_8B_WEIL_OBJECT_DEFINITIONS.md

score: 7

```text
1: # Phase 8B — Weil Object Definitions
2: 
3: ## Purpose
```

```text
3: ## Purpose
4: 
5: Phase 8A started the classical Weil criterion reconstruction program.
6: 
7: Phase 8B defines the objects that future phases must handle carefully.
```

```text
9: This is not a proof of RH.
10: 
11: This is not a new Weil criterion.
12: 
13: This is a notation and object-definition phase.
```

```text
25: 3. zero-side terms;
26: 4. prime-side terms;
27: 5. quadratic forms;
28: 6. positivity statements;
29: 7. negative directions.
```

```text
26: 4. prime-side terms;
27: 5. quadratic forms;
28: 6. positivity statements;
29: 7. negative directions.
30: 
```

### weil_reconstruction/sources/extractions/T_FUNCTIONAL_TERM_TABLE.md

score: 7

```text
1: # T[f] Term Table
2: 
3: | Term | Exact source expression | Project notation | Status |
```

```text
4: |---|---|---|---|
5: | Test-function class | \(f\in C_0^\infty((0,\infty))\) | \(\mathcal A_B\) | LOCKED |
6: | Involution | \(f^*(x)=x^{-1}f(1/x)\) | \(f^*\) | LOCKED |
7: | Mellin transform | \(f(s)=\int_0^\infty f(x)x^{s-1}dx\) | \(\mathcal M f\) | LOCKED |
8: | Mass term 1 | \(\int_0^\infty f(x)dx\) | \(M_1[f]\) | LOCKED |
```

```text
5: | Test-function class | \(f\in C_0^\infty((0,\infty))\) | \(\mathcal A_B\) | LOCKED |
6: | Involution | \(f^*(x)=x^{-1}f(1/x)\) | \(f^*\) | LOCKED |
7: | Mellin transform | \(f(s)=\int_0^\infty f(x)x^{s-1}dx\) | \(\mathcal M f\) | LOCKED |
8: | Mass term 1 | \(\int_0^\infty f(x)dx\) | \(M_1[f]\) | LOCKED |
9: | Mass term 2 | \(\int_0^\infty f^*(x)dx\) | \(M_2[f]\) | LOCKED |
```

```text
7: | Mellin transform | \(f(s)=\int_0^\infty f(x)x^{s-1}dx\) | \(\mathcal M f\) | LOCKED |
8: | Mass term 1 | \(\int_0^\infty f(x)dx\) | \(M_1[f]\) | LOCKED |
9: | Mass term 2 | \(\int_0^\infty f^*(x)dx\) | \(M_2[f]\) | LOCKED |
10: | Prime-side term | \(-\sum_{n=1}^\infty\Lambda(n)\{f(n)+f^*(n)\}\) | \(P[f]\) | LOCKED |
11: | Constant term | \(-(\log4\pi+\gamma_E)f(1)\) | \(C[f]\) | LOCKED |
```

```text
10: | Prime-side term | \(-\sum_{n=1}^\infty\Lambda(n)\{f(n)+f^*(n)\}\) | \(P[f]\) | LOCKED |
11: | Constant term | \(-(\log4\pi+\gamma_E)f(1)\) | \(C[f]\) | LOCKED |
12: | Archimedean integral | \(-\int_1^\infty(f(x)+f^*(x)-2f(1)/x)\frac{x\,dx}{x^2-1}\) | \(A[f]\) | LOCKED |
13: | Zero-side identity | \(T[f]=T[f^*]=\sum_\rho f(\rho)\) | \(Z[f]\) | LOCKED |
14: | Full \(T[f]\) formula | Sum of all extracted terms above | \(T[f]\) | LOCKED |
```

### weil_reconstruction/symbolic/PHASE_8J_COMPLEX_STAR_CONVENTION_AUDIT.md

score: 7

```text
12: 
13: \[
14: f^*(x)=x^{-1}f(1/x).
15: \]
16: 
```

```text
15: \]
16: 
17: However, Bombieri's positivity statements involve complex-valued test functions.
18: 
19: For complex-valued functions, there is a major convention risk:
```

```text
20: 
21: \[
22: f^*(x)=x^{-1}f(1/x)
23: \]
24: 
```

```text
35: This is not a proof of RH.
36: 
37: This is not a new Weil criterion.
38: 
39: This phase blocks finite-rank positivity code until the source convention is fully locked.
```

```text
37: This is not a new Weil criterion.
38: 
39: This phase blocks finite-rank positivity code until the source convention is fully locked.
40: 
41: ---
```

### horizontal_defect/PHASE_7A_HORIZONTAL_INFORMATION_AUDIT.md

score: 6

```text
57: It is cancellation-prone if off-critical contributions can cancel after summation over zeros.
58: 
59: ## Category C — Positivity-compatible
60: 
61: An object is positivity-compatible if it can be placed inside a nonnegative quadratic, energy, norm, or positive semidefinite form.
```

```text
59: ## Category C — Positivity-compatible
60: 
61: An object is positivity-compatible if it can be placed inside a nonnegative quadratic, energy, norm, or positive semidefinite form.
62: 
63: This category matters because RH is equivalent to several positivity principles.
```

```text
61: An object is positivity-compatible if it can be placed inside a nonnegative quadratic, energy, norm, or positive semidefinite form.
62: 
63: This category matters because RH is equivalent to several positivity principles.
64: 
65: ## Category D — Explicit-formula compatible
```

```text
65: ## Category D — Explicit-formula compatible
66: 
67: An object is explicit-formula compatible if it can be related to primes or arithmetic data through a Weil/Guinand-type explicit formula.
68: 
69: This category matters because RH is not only a zero-side statement; it is tied to prime-side oscillation.
```

```text
75: ## Category F — Potentially RH-relevant
76: 
77: An object is potentially RH-relevant only if it is horizontally sensitive, not trivially cancellation-destroyed, and either positivity-compatible or explicit-formula compatible.
78: 
79: ---
```

### horizontal_defect/theorems/PHASE_7D_AGGREGATION_BARRIER.md

score: 6

```text
104: 
105: \[
106: \sum_\rho
107: \phi(\gamma_\rho)
108: \left(\log |1-1/\rho|\right)^2
```

```text
130: \mathcal D_\phi
131: =
132: \sum_\rho
133: \phi(\gamma_\rho)
134: \left(\log |1-1/\rho|\right)^2.
```

```text
151: We have only defined a nonnegative quantity that would vanish if RH holds.
152: 
153: The difficult part is not positivity.
154: 
155: The difficult part is proving vanishing or deriving an arithmetic-side identity strong enough to force vanishing.
```

```text
165: \]
166: 
167: Classical explicit formulae are naturally linear sums over zeros of test functions:
168: 
169: \[
```

```text
168: 
169: \[
170: \sum_\rho h(\rho).
171: \]
172: 
```

### horizontal_defect/theorems/PHASE_7F_QUADRATIC_LI_FILTER_POSITIVITY.md

score: 6

```text
1: # Phase 7F — Quadratic Li-Filter Positivity Lift
2: 
3: ## Purpose
```

```text
7: This phase shows that quadratic lifting fixes the phase-sign problem.
8: 
9: The price is that the resulting object is nonlinear and no longer automatically compatible with the classical linear explicit formula.
10: 
11: This phase does not prove RH.
```

```text
73: ---
74: 
75: # 3. Phase-uniform positivity theorem
76: 
77: ## Theorem
```

```text
209: ---
210: 
211: # 5. General quadratic form version
212: 
213: Let
```

```text
225: \]
226: 
227: the quadratic form
228: 
229: \[
```

### horizontal_defect/weil_interface/PHASE_7G_WEIL_POSITIVE_INTERFACE_AUDIT.md

score: 6

```text
1: # Phase 7G — Weil-Positive Interface Audit
2: 
3: ## Purpose
```

```text
15: It is strictly positive for every nonzero horizontal displacement parameter \(u\).
16: 
17: However, positivity alone is not enough.
18: 
19: The real question is whether such positivity can interface with classical Weil-positive machinery.
```

```text
17: However, positivity alone is not enough.
18: 
19: The real question is whether such positivity can interface with classical Weil-positive machinery.
20: 
21: This phase audits that interface.
```

```text
23: This phase does not prove RH.
24: 
25: It does not claim a new Weil criterion.
26: 
27: ---
```

```text
29: # 1. Classical interface principle
30: 
31: The classical explicit formula naturally relates arithmetic information to linear sums over zeros of test functions:
32: 
33: \[
```

### original_results/finite_bombieri_stability/contribution_branch/classical_import_map/PHASE_10AN_CLASSICAL_IMPORT_MAP.md

score: 6

```text
3: ## Purpose
4: 
5: Phase 10AM defined a toy-but-honest Weil-form abstraction:
6: 
7: \[
```

```text
9: \]
10: 
11: Phase 10AN maps each toy object to the classical Weil/Bombieri object that must eventually replace it.
12: 
13: This phase does not prove RH.
```

```text
25: | Toy abstraction | Classical object needed | Current status |
26: |---|---|---|
27: | \(\mathcal D\) | admissible Weil/Bombieri test-function space | missing |
28: | \(Q_\infty\) | true infinite Weil/Bombieri quadratic form | missing |
29: | \(B_\infty\) | true Hermitian Weil/Bombieri bilinear or sesquilinear form | missing |
```

```text
26: |---|---|---|
27: | \(\mathcal D\) | admissible Weil/Bombieri test-function space | missing |
28: | \(Q_\infty\) | true infinite Weil/Bombieri quadratic form | missing |
29: | \(B_\infty\) | true Hermitian Weil/Bombieri bilinear or sesquilinear form | missing |
30: | \(V_N\) | finite-dimensional truncation or approximation space | missing |
```

```text
27: | \(\mathcal D\) | admissible Weil/Bombieri test-function space | missing |
28: | \(Q_\infty\) | true infinite Weil/Bombieri quadratic form | missing |
29: | \(B_\infty\) | true Hermitian Weil/Bombieri bilinear or sesquilinear form | missing |
30: | \(V_N\) | finite-dimensional truncation or approximation space | missing |
31: | \(M_N\) | finite Bombieri/Weil matrix from the classical construction | partially modeled |
```

### proofs/PHASE_5S_SECOND_LOG_MOMENT_LI_WEIL_BRIDGE.md

score: 6

```text
1: # Phase 5S — Second Log-Moment Li Test Function and Weil Bridge
2: 
3: ## Status
```

```text
3: ## Status
4: 
5: EXACT MELLIN BRIDGE PROVED.
6: 
7: FINITE SIGNED WEIL-RANK QUESTION OPEN.
```

```text
5: EXACT MELLIN BRIDGE PROVED.
6: 
7: FINITE SIGNED WEIL-RANK QUESTION OPEN.
8: 
9: ## Prior-art correction
```

```text
17: \]
18: 
19: is already explicitly embedded into Guinand-Weil explicit-formula machinery in the classical Li literature.
20: 
21: Bombieri-Lagarias derive arithmetic formulas for Li coefficients through the Guinand-Weil explicit formula.
```

```text
19: is already explicitly embedded into Guinand-Weil explicit-formula machinery in the classical Li literature.
20: 
21: Bombieri-Lagarias derive arithmetic formulas for Li coefficients through the Guinand-Weil explicit formula.
22: 
23: Later treatments record the corresponding inverse-Mellin test function explicitly.
```

### weil_reconstruction/sources/extractions/BOMBIERI_THEOREM_2_CARD.md

score: 6

```text
1: # Bombieri Theorem 2 Card
2: 
3: ## Source
```

```text
3: ## Source
4: 
5: Bombieri, Section 3.
6: 
7: ## Theorem type
```

```text
11: ## Statement
12: 
13: Bombieri defines a linear functional
14: 
15: \[
```

```text
14: 
15: \[
16: T[f]
17: \]
18: 
```

```text
26: 
27: \[
28: T[f]=T[f^*]=\sum_\rho f(\rho).
29: \]
30: 
```

## Exact audit strings

PHASE_12B_SOURCE_SCAN_COMPLETE

LOCAL_SOURCE_SCAN_PERFORMED

