# Phase 12C Quadratic Form Source Scan Report

## Purpose

Search local project files for an exact imported Weil positivity quadratic form.

## Search target

\[
Q_W(g)=T[F_g]
\]

or an equivalent source-grounded quadratic/Hermitian Weil positivity form.

## Top hits

### scripts/run_phase12c_quadratic_source_scan.py

score: 17

```text
1: from pathlib import Path
2: 
3: ROOT = Path(".")
4: OUT = Path("original_results/finite_bombieri_stability/level4_candidate/quadratic_form_import")
5: OUT.mkdir(parents=True, exist_ok=True)
6: 
7: patterns = [
```

```text
5: OUT.mkdir(parents=True, exist_ok=True)
6: 
7: patterns = [
8:     "Q_W",
9:     "B_W",
10:     "quadratic form",
11:     "Hermitian form",
```

```text
6: 
7: patterns = [
8:     "Q_W",
9:     "B_W",
10:     "quadratic form",
11:     "Hermitian form",
12:     "positive definite",
```

```text
7: patterns = [
8:     "Q_W",
9:     "B_W",
10:     "quadratic form",
11:     "Hermitian form",
12:     "positive definite",
13:     "positive semidefinite",
```

```text
8:     "Q_W",
9:     "B_W",
10:     "quadratic form",
11:     "Hermitian form",
12:     "positive definite",
13:     "positive semidefinite",
14:     "Weil positivity",
```

```text
9:     "B_W",
10:     "quadratic form",
11:     "Hermitian form",
12:     "positive definite",
13:     "positive semidefinite",
14:     "Weil positivity",
15:     "positivity criterion",
```

```text
10:     "quadratic form",
11:     "Hermitian form",
12:     "positive definite",
13:     "positive semidefinite",
14:     "Weil positivity",
15:     "positivity criterion",
16:     "RH iff",
```

```text
11:     "Hermitian form",
12:     "positive definite",
13:     "positive semidefinite",
14:     "Weil positivity",
15:     "positivity criterion",
16:     "RH iff",
17:     "Riemann hypothesis if and only if",
```

### original_results/finite_bombieri_stability/level4_candidate/true_weil_form_import/PHASE_12B_TRUE_WEIL_FORM_IMPORT_ATTEMPT.md

score: 11

```text
1: # Phase 12B — True Weil/Bombieri Form Import Attempt
2: 
3: ## Purpose
4: 
```

```text
8: \text{no more architecture-only phases.}
9: \]
10: 
11: Phase 12B attempts to import the true Weil/Bombieri object needed for the Level 4 target.
12: 
13: The required objects are:
14: 
```

```text
13: The required objects are:
14: 
15: \[
16: Q_W,\quad \mathcal D_W,\quad B_W.
17: \]
18: 
19: The Level 4 target cannot proceed honestly without them.
```

```text
22: 
23: # 1. Source-grounded object already extracted in the project
24: 
25: The project previously extracted a Bombieri-style explicit formula functional \(T[f]\).
26: 
27: The extracted formula was recorded in the project as:
28: 
```

```text
27: The extracted formula was recorded in the project as:
28: 
29: \[
30: T[f]
31: =
32: \int_0^\infty f(x)\,dx
33: +
```

```text
53: The zero-side identity was recorded as:
54: 
55: \[
56: T[f]=T[f^*]=\sum_\rho f(\rho).
57: \]
58: 
59: ## Classification
```

```text
64: \boxed{\text{SOURCE-EXTRACTED BOMBIIERI EXPLICIT FORMULA FUNCTIONAL}}
65: \]
66: 
67: It is not yet the complete imported quadratic positivity form \(Q_W\).
68: 
69: ---
70: 
```

```text
73: The following object can be imported from the existing project extraction:
74: 
75: \[
76: T[f].
77: \]
78: 
79: Status:
```

### research_ledger/CLAIM_LEDGER.md

score: 11

```text
691: 
692: **Statement:** Abstract multiset or signed zero-configuration language is project-originating infrastructure.
693: 
694: **Failure:** Bombieri-Lagarias formulate Li-type criteria for arbitrary complex multisets with convergence and symmetry conditions.
695: 
696: **Disposition:** Cite Bombieri-Lagarias as foundational multiset context.
697: 
```

```text
693: 
694: **Failure:** Bombieri-Lagarias formulate Li-type criteria for arbitrary complex multisets with convergence and symmetry conditions.
695: 
696: **Disposition:** Cite Bombieri-Lagarias as foundational multiset context.
697: 
698: ---
699: 
```

```text
6563: 
6564: **Status:** CRITICAL PRIOR-ART QUESTION
6565: 
6566: **Statement:** Before defining a positive quadratic horizontal-defect transform, audit whether the target is already subsumed by Weil positivity, Guinand–Weil explicit-formula quadratic forms, Bombieri–Lagarias criteria, de Branges-type Hilbert-space formulations, or Nyman–Beurling/Báez-Duarte \(L^2\) criteria.
6567: 
6568: ---
6569: 
```

```text
6590: 1-\left(1-\frac1s\right)^n
6591: \]
6592: 
6593: is already explicitly embedded into Guinand-Weil explicit-formula machinery.
6594: 
6595: Bombieri-Lagarias derive Li arithmetic formulas via Guinand-Weil, and the corresponding inverse-Mellin Li test function is explicitly recorded in the literature.
6596: 
```

```text
6592: 
6593: is already explicitly embedded into Guinand-Weil explicit-formula machinery.
6594: 
6595: Bombieri-Lagarias derive Li arithmetic formulas via Guinand-Weil, and the corresponding inverse-Mellin Li test function is explicitly recorded in the literature.
6596: 
6597: **Disposition:** PA-4.
6598: 
```

```text
6661: 
6662: **Status:** PRIOR-ART DISPOSITION
6663: 
6664: **Statement:** Classical Weil positivity does not directly give a sign for the Li susceptibility merely from CL-0414.
6665: 
6666: The second log-moment Li test function is not automatically a Hermitian convolution square or positive-type test function.
6667: 
```

```text
6663: 
6664: **Statement:** Classical Weil positivity does not directly give a sign for the Li susceptibility merely from CL-0414.
6665: 
6666: The second log-moment Li test function is not automatically a Hermitian convolution square or positive-type test function.
6667: 
6668: The sign-changing susceptibility profile is consistent with this fact.
6669: 
```

```text
6679: G_n^{(2)}(y)=y^2G_n(y)
6680: \]
6681: 
6682: admits a finite signed convolution-square decomposition or finite-signature representation in Weil quadratic-form coordinates.
6683: 
6684: A useful result would require explicit control of the rank, signature, or asymptotic matched-scale structure.
6685: 
```

### original_results/finite_bombieri_stability/level4_candidate/true_weil_form_import/NEXT_PHASE_12C_QUADRATIC_FORM_IMPORT.md

score: 8

```text
1: # Next Phase 12C — Quadratic Weil Positivity Form Import
2: 
3: ## Goal
4: 
```

```text
5: Import or honestly fail to import the exact quadratic positivity form:
6: 
7: \[
8: Q_W(g)=T[F_g].
9: \]
10: 
11: ## Required objects
```

```text
10: 
11: ## Required objects
12: 
13: 1. \(F_g\): the exact test function built from \(g\).
14: 2. \(Q_W(g)\): the exact quadratic form.
15: 3. \(B_W(f,g)\): the exact Hermitian form.
16: 4. \(\mathcal D_W\): the exact admissible domain.
```

```text
11: ## Required objects
12: 
13: 1. \(F_g\): the exact test function built from \(g\).
14: 2. \(Q_W(g)\): the exact quadratic form.
15: 3. \(B_W(f,g)\): the exact Hermitian form.
16: 4. \(\mathcal D_W\): the exact admissible domain.
17: 5. The exact RH positivity theorem.
```

```text
12: 
13: 1. \(F_g\): the exact test function built from \(g\).
14: 2. \(Q_W(g)\): the exact quadratic form.
15: 3. \(B_W(f,g)\): the exact Hermitian form.
16: 4. \(\mathcal D_W\): the exact admissible domain.
17: 5. The exact RH positivity theorem.
18: 
```

```text
20: 
21: No guessing.
22: 
23: No placeholder \(Q_W\).
24: 
25: If the project sources do not contain this, record that external source review is required.
26: 
```

### original_results/finite_bombieri_stability/level4_candidate/true_weil_form_import/PHASE_12B_SOURCE_SCAN_REPORT.md

score: 8

```text
2: 
3: ## Purpose
4: 
5: Search local project files for previously extracted Bombieri/Weil source objects.
6: 
7: ## Top hits
8: 
```

```text
29: ```text
30: 692: **Statement:** Abstract multiset or signed zero-configuration language is project-originating infrastructure.
31: 693: 
32: 694: **Failure:** Bombieri-Lagarias formulate Li-type criteria for arbitrary complex multisets with convergence and symmetry conditions.
33: 695: 
34: 696: **Disposition:** Cite Bombieri-Lagarias as foundational multiset context.
35: ```
```

```text
31: 693: 
32: 694: **Failure:** Bombieri-Lagarias formulate Li-type criteria for arbitrary complex multisets with convergence and symmetry conditions.
33: 695: 
34: 696: **Disposition:** Cite Bombieri-Lagarias as foundational multiset context.
35: ```
36: 
37: ```text
```

```text
35: ```
36: 
37: ```text
38: 694: **Failure:** Bombieri-Lagarias formulate Li-type criteria for arbitrary complex multisets with convergence and symmetry conditions.
39: 695: 
40: 696: **Disposition:** Cite Bombieri-Lagarias as foundational multiset context.
41: 697: 
```

```text
37: ```text
38: 694: **Failure:** Bombieri-Lagarias formulate Li-type criteria for arbitrary complex multisets with convergence and symmetry conditions.
39: 695: 
40: 696: **Disposition:** Cite Bombieri-Lagarias as foundational multiset context.
41: 697: 
42: 698: ---
43: ```
```

```text
57: ```text
58: 3: 
59: 4: ROOT = Path(".")
60: 5: OUT = Path("original_results/finite_bombieri_stability/level4_candidate/true_weil_form_import")
61: 6: OUT.mkdir(parents=True, exist_ok=True)
62: 7: 
63: ```
```

```text
65: ```text
66: 7: 
67: 8: patterns = [
68: 9:     "T[f]",
69: 10:     "T[f^*]",
70: 11:     "sum_\\rho",
71: ```
```

```text
66: 7: 
67: 8: patterns = [
68: 9:     "T[f]",
69: 10:     "T[f^*]",
70: 11:     "sum_\\rho",
71: ```
72: 
```

### research_ledger/PHASE_LEDGER.md

score: 8

```text
4953: 
4954: ### Next required audit
4955: 
4956: Weil positivity.
4957: 
4958: Guinand–Weil explicit formula.
4959: 
```

```text
4955: 
4956: Weil positivity.
4957: 
4958: Guinand–Weil explicit formula.
4959: 
4960: Bombieri–Lagarias quadratic criteria.
4961: 
```

```text
4957: 
4958: Guinand–Weil explicit formula.
4959: 
4960: Bombieri–Lagarias quadratic criteria.
4961: 
4962: de Branges-type Hilbert-space RH criteria.
4963: 
```

```text
4970: 
4971: ---
4972: 
4973: ## Phase 5S — Second Log-Moment Li Test Function and Weil Bridge
4974: 
4975: Status: EXACT MELLIN BRIDGE COMPLETE
4976: 
```

```text
4976: 
4977: ### Prior-art correction
4978: 
4979: The Li kernel itself is classically embedded in Guinand-Weil machinery.
4980: 
4981: Li-kernel explicit-formula embedding:
4982: 
```

```text
5024: 
5025: The Li susceptibility is the critical-line cosine response of the second log-moment deformation of the classical Li explicit-formula test family.
5026: 
5027: ### Weil positivity status
5028: 
5029: No direct positivity follows.
5030: 
```

```text
5028: 
5029: No direct positivity follows.
5030: 
5031: The susceptibility test function is not automatically a convolution square or positive-type function.
5032: 
5033: ### Next theorem target
5034: 
```

```text
5032: 
5033: ### Next theorem target
5034: 
5035: Finite signed Weil-rank audit for
5036: 
5037: \[
5038: G_n^{(2)}.
```

### weil_reconstruction/sources/CONVENTION_LOCK_TABLE.md

score: 7

```text
1: # Convention Lock Table
2: 
3: This table must be filled before implementing any exact Weil quadratic form.
4: 
5: | Object | Chosen convention | Source | Status |
6: |---|---|---|---|
```

```text
4: 
5: | Object | Chosen convention | Source | Status |
6: |---|---|---|---|
7: | Primary reconstruction path | Bombieri-style Weil quadratic form | Bombieri source card | LOCKED |
8: | Primary source section | Bombieri Sections 2 and 3 | Bombieri extraction cards | LOCKED |
9: | Weil positivity as RH-equivalent framework | Positive semidefinite Weil quadratic functional iff RH | Bombieri / Suzuki source cards | LOCKED |
10: | Primary test-function ambient space | \(C_0^\infty((0,\infty))\) | Bombieri Theorem 1 and 2 cards | LOCKED |
```

```text
5: | Object | Chosen convention | Source | Status |
6: |---|---|---|---|
7: | Primary reconstruction path | Bombieri-style Weil quadratic form | Bombieri source card | LOCKED |
8: | Primary source section | Bombieri Sections 2 and 3 | Bombieri extraction cards | LOCKED |
9: | Weil positivity as RH-equivalent framework | Positive semidefinite Weil quadratic functional iff RH | Bombieri / Suzuki source cards | LOCKED |
10: | Primary test-function ambient space | \(C_0^\infty((0,\infty))\) | Bombieri Theorem 1 and 2 cards | LOCKED |
11: | Involution | \(f^*(x)=x^{-1}f(1/x)\) | Bombieri Section 2 | LOCKED |
```

```text
6: |---|---|---|---|
7: | Primary reconstruction path | Bombieri-style Weil quadratic form | Bombieri source card | LOCKED |
8: | Primary source section | Bombieri Sections 2 and 3 | Bombieri extraction cards | LOCKED |
9: | Weil positivity as RH-equivalent framework | Positive semidefinite Weil quadratic functional iff RH | Bombieri / Suzuki source cards | LOCKED |
10: | Primary test-function ambient space | \(C_0^\infty((0,\infty))\) | Bombieri Theorem 1 and 2 cards | LOCKED |
11: | Involution | \(f^*(x)=x^{-1}f(1/x)\) | Bombieri Section 2 | LOCKED |
12: | Mellin transform | \(f(s)=\int_0^\infty f(x)x^{s-1}dx\) | Bombieri Section 2 | LOCKED |
```

```text
7: | Primary reconstruction path | Bombieri-style Weil quadratic form | Bombieri source card | LOCKED |
8: | Primary source section | Bombieri Sections 2 and 3 | Bombieri extraction cards | LOCKED |
9: | Weil positivity as RH-equivalent framework | Positive semidefinite Weil quadratic functional iff RH | Bombieri / Suzuki source cards | LOCKED |
10: | Primary test-function ambient space | \(C_0^\infty((0,\infty))\) | Bombieri Theorem 1 and 2 cards | LOCKED |
11: | Involution | \(f^*(x)=x^{-1}f(1/x)\) | Bombieri Section 2 | LOCKED |
12: | Mellin transform | \(f(s)=\int_0^\infty f(x)x^{s-1}dx\) | Bombieri Section 2 | LOCKED |
13: | Primary zero-side product theorem | \(\sum_\rho g(\rho)g(1-\rho)>0\) for nonzero \(g\) | Bombieri Theorem 1 card | LOCKED |
```

```text
8: | Primary source section | Bombieri Sections 2 and 3 | Bombieri extraction cards | LOCKED |
9: | Weil positivity as RH-equivalent framework | Positive semidefinite Weil quadratic functional iff RH | Bombieri / Suzuki source cards | LOCKED |
10: | Primary test-function ambient space | \(C_0^\infty((0,\infty))\) | Bombieri Theorem 1 and 2 cards | LOCKED |
11: | Involution | \(f^*(x)=x^{-1}f(1/x)\) | Bombieri Section 2 | LOCKED |
12: | Mellin transform | \(f(s)=\int_0^\infty f(x)x^{s-1}dx\) | Bombieri Section 2 | LOCKED |
13: | Primary zero-side product theorem | \(\sum_\rho g(\rho)g(1-\rho)>0\) for nonzero \(g\) | Bombieri Theorem 1 card | LOCKED |
14: | Primary quadratic positivity object | \(T[f*f^*]\ge0\) | Bombieri Theorem 2 card | LOCKED |
```

```text
9: | Weil positivity as RH-equivalent framework | Positive semidefinite Weil quadratic functional iff RH | Bombieri / Suzuki source cards | LOCKED |
10: | Primary test-function ambient space | \(C_0^\infty((0,\infty))\) | Bombieri Theorem 1 and 2 cards | LOCKED |
11: | Involution | \(f^*(x)=x^{-1}f(1/x)\) | Bombieri Section 2 | LOCKED |
12: | Mellin transform | \(f(s)=\int_0^\infty f(x)x^{s-1}dx\) | Bombieri Section 2 | LOCKED |
13: | Primary zero-side product theorem | \(\sum_\rho g(\rho)g(1-\rho)>0\) for nonzero \(g\) | Bombieri Theorem 1 card | LOCKED |
14: | Primary quadratic positivity object | \(T[f*f^*]\ge0\) | Bombieri Theorem 2 card | LOCKED |
15: | Primary zero-side identity | \(T[f]=T[f^*]=\sum_\rho f(\rho)\) | Bombieri Theorem 2 card | LOCKED |
```

```text
10: | Primary test-function ambient space | \(C_0^\infty((0,\infty))\) | Bombieri Theorem 1 and 2 cards | LOCKED |
11: | Involution | \(f^*(x)=x^{-1}f(1/x)\) | Bombieri Section 2 | LOCKED |
12: | Mellin transform | \(f(s)=\int_0^\infty f(x)x^{s-1}dx\) | Bombieri Section 2 | LOCKED |
13: | Primary zero-side product theorem | \(\sum_\rho g(\rho)g(1-\rho)>0\) for nonzero \(g\) | Bombieri Theorem 1 card | LOCKED |
14: | Primary quadratic positivity object | \(T[f*f^*]\ge0\) | Bombieri Theorem 2 card | LOCKED |
15: | Primary zero-side identity | \(T[f]=T[f^*]=\sum_\rho f(\rho)\) | Bombieri Theorem 2 card | LOCKED |
16: | Full \(T[f]\) formula | Mass terms + prime term + constant term + archimedean integral | Phase 8H extraction | LOCKED |
```

### weil_reconstruction/sources/extractions/PHASE_8E_INITIAL_SOURCE_EXTRACTION.md

score: 7

```text
8: 
9: This is not a proof of RH.
10: 
11: This is not a new Weil criterion.
12: 
13: This is a source-notes phase.
14: 
```

```text
18: 
19: ## Source A
20: 
21: Enrico Bombieri, **Remarks on Weil's quadratic functional in the theory of prime numbers, I**, Rend. Mat. Acc. Lincei, Serie 9, Vol. 11, 183-233, 2000.
22: 
23: ## Source B
24: 
```

```text
22: 
23: ## Source B
24: 
25: Masatoshi Suzuki, **Weil's Quadratic Form via the Screw Function**, uploaded source excerpt.
26: 
27: ---
28: 
```

```text
26: 
27: ---
28: 
29: # 2. Bombieri extraction
30: 
31: ## Bibliographic identity
32: 
```

```text
30: 
31: ## Bibliographic identity
32: 
33: Author: Enrico Bombieri.
34: 
35: Title: Remarks on Weil's quadratic functional in the theory of prime numbers, I.
36: 
```

```text
32: 
33: Author: Enrico Bombieri.
34: 
35: Title: Remarks on Weil's quadratic functional in the theory of prime numbers, I.
36: 
37: Venue: Rendiconti Lincei, Matematica e Applicazioni.
38: 
```

```text
42: 
43: ## Extracted classical claims
44: 
45: Bombieri studies Weil's explicit formula and the associated quadratic functional.
46: 
47: The source states that the associated quadratic functional is positive semidefinite if and only if RH is true.
48: 
```

```text
44: 
45: Bombieri studies Weil's explicit formula and the associated quadratic functional.
46: 
47: The source states that the associated quadratic functional is positive semidefinite if and only if RH is true.
48: 
49: The source studies finite truncations and eigenvalues of an infinite quadratic form obtained from the Fourier transform of the functional.
50: 
```

### original_results/finite_bombieri_stability/contribution_branch/bombieri_weil_template/PHASE_10AL_BOMBIIERI_WEIL_SPECIALIZATION_TEMPLATE.md

score: 6

```text
1: # Phase 10AL — Bombieri/Weil Specialization Template
2: 
3: ## Purpose
4: 
```

```text
10: Q,\quad Q_N,\quad P_N
11: \]
12: 
13: to a Bombieri/Weil-style template.
14: 
15: This phase does not prove RH.
16: 
```

```text
27: Let
28: 
29: \[
30: Q_W:\mathcal D\to\mathbb R
31: \]
32: 
33: denote an infinite Weil/Bombieri-style quadratic form.
```

```text
30: Q_W:\mathcal D\to\mathbb R
31: \]
32: 
33: denote an infinite Weil/Bombieri-style quadratic form.
34: 
35: The RH-relevant positivity dream is:
36: 
```

```text
35: The RH-relevant positivity dream is:
36: 
37: \[
38: Q_W(f)\geq0
39: \quad
40: \text{for all } f\in\mathcal D.
41: \]
```

```text
40: \text{for all } f\in\mathcal D.
41: \]
42: 
43: In classical RH-related positivity frameworks, positivity of a Weil-type form is expected to encode RH-like information.
44: 
45: This project does not prove that equivalence.
46: 
```

```text
44: 
45: This project does not prove that equivalence.
46: 
47: Instead, it asks what finite certified computations would need in order to say something rigorous about \(Q_W\).
48: 
49: ---
50: 
```

```text
66: 
67: be a finite Hermitian matrix built from the finite symbolic \(H\)-kernel.
68: 
69: Define the finite quadratic form
70: 
71: \[
72: Q_N(v)=v^*M_Nv.
```

### original_results/finite_bombieri_stability/contribution_branch/convergence_skeleton/PHASE_10AP_CONVERGENCE_THEOREM_SKELETON.md

score: 6

```text
5: Phase 10AO identified the central contribution bottleneck:
6: 
7: \[
8: |Q_N(P_N^W f)-Q_W(f)|\leq \varepsilon_N(f),
9: \qquad
10: \varepsilon_N(f)\to0.
11: \]
```

```text
27: Let
28: 
29: \[
30: Q_W:\mathcal D_W\to\mathbb R
31: \]
32: 
33: be the true Weil/Bombieri quadratic form on an admissible test-function domain
```

```text
30: Q_W:\mathcal D_W\to\mathbb R
31: \]
32: 
33: be the true Weil/Bombieri quadratic form on an admissible test-function domain
34: 
35: \[
36: \mathcal D_W.
```

```text
36: \mathcal D_W.
37: \]
38: 
39: At this stage, \(Q_W\) is still not fully imported.
40: 
41: Therefore this phase treats \(Q_W\) as the target classical object.
42: 
```

```text
38: 
39: At this stage, \(Q_W\) is still not fully imported.
40: 
41: Therefore this phase treats \(Q_W\) as the target classical object.
42: 
43: ---
44: 
```

```text
58: M_N^W
59: \]
60: 
61: be Hermitian matrices representing finite Weil/Bombieri-style forms.
62: 
63: Define
64: 
```

```text
81: The weakest required convergence is:
82: 
83: \[
84: Q_N^W(P_N^Wf)\to Q_W(f)
85: \]
86: 
87: for every fixed
```

```text
99: A stronger and more useful target is:
100: 
101: \[
102: |Q_N^W(P_N^Wf)-Q_W(f)|
103: \leq
104: \varepsilon_N(f),
105: \]
```

### original_results/finite_bombieri_stability/contribution_branch/final_professor_package/POLISHED_CONDITIONAL_THEOREM_NOTE.md

score: 6

```text
1: # A Conditional Finite-to-Infinite Transfer Framework for Certified Gram-Matrix Approximations in Weil/Bombieri-Style Models
2: 
3: ## Abstract
4: 
```

```text
2: 
3: ## Abstract
4: 
5: We develop a conditional finite-to-infinite transfer framework for finite Gram-matrix approximations associated with Weil/Bombieri-style quadratic forms. For a finite bounded test class
6: 
7: \[
8: \mathcal F_R^{(m)}
```

```text
41: \right).
42: \]
43: 
44: We also include a certified numerical model for the computational term \(C_{ij}^{(N)}\), based on interval enclosures. The result is conditional: it does not import the true Weil/Bombieri form, does not prove unconditional convergence, and does not prove or advance the Riemann Hypothesis. Its intended use is as a reviewable framework for clarifying what would be required to make finite certified computations meaningful for infinite Weil/Bombieri positivity questions.
45: 
46: ---
47: 
```

```text
47: 
48: ## 1. Motivation
49: 
50: Finite matrix computations can be misleading unless their relationship to the intended infinite mathematical object is controlled. In RH-adjacent Weil/Bombieri-style settings, a finite matrix may exhibit positivity, negativity, or stable eigenvalue counts, but such finite behavior is meaningful only if it transfers to a genuine infinite form.
51: 
52: This note asks a narrower question:
53: 
```

```text
51: 
52: This note asks a narrower question:
53: 
54: Given a finite test class, what error bounds are sufficient to transfer finite Gram-matrix information to an infinite quadratic form?
55: 
56: The answer is conditional but explicit.
57: 
```

```text
81: 
82: \[
83: \sup_{f\in\mathcal F_R^{(m)}}
84: |Q_N^W(P_N^Wf)-Q_W(f)|.
85: \]
86: 
87: ---
```

```text
88: 
89: ## 3. Infinite and finite Gram matrices
90: 
91: Let \(B_W\) be the Hermitian form associated to the infinite quadratic form \(Q_W\). Define
92: 
93: \[
94: G^{(\infty)}_{ij}=B_W(\phi_i,\phi_j).
```

```text
91: Let \(B_W\) be the Hermitian form associated to the infinite quadratic form \(Q_W\). Define
92: 
93: \[
94: G^{(\infty)}_{ij}=B_W(\phi_i,\phi_j).
95: \]
96: 
97: Let \(B_N^W\) be the finite Hermitian form associated to \(Q_N^W\), and let
```

### original_results/finite_bombieri_stability/contribution_branch/gram_convergence_problem/PHASE_10AR_GRAM_CONVERGENCE_PROBLEM.md

score: 6

```text
6: 
7: \[
8: \sup_{f\in\mathcal F_R^{(m)}}
9: |Q_N^W(P_N^Wf)-Q_W(f)|
10: \leq
11: R^2\|G^{(N)}-G^{(\infty)}\|_2.
12: \]
```

```text
51: 
52: # 2. Infinite Gram matrix
53: 
54: Let \(B_W\) be the Hermitian form associated with the infinite Weil/Bombieri quadratic form \(Q_W\).
55: 
56: Define
57: 
```

```text
58: \[
59: G^{(\infty)}_{ij}
60: =
61: B_W(\phi_i,\phi_j).
62: \]
63: 
64: Then
```

```text
64: Then
65: 
66: \[
67: Q_W(f)=a^*G^{(\infty)}a.
68: \]
69: 
70: ---
```

```text
71: 
72: # 3. Finite Gram matrix
73: 
74: Let \(B_N^W\) be the finite Hermitian form represented by \(M_N^W\).
75: 
76: Let
77: 
```

```text
142: 
143: \[
144: \sup_{f\in\mathcal F_R^{(m)}}
145: |Q_N^W(P_N^Wf)-Q_W(f)|
146: \leq
147: R^2m\delta_N^{(m)}.
148: \]
```

```text
156: then
157: 
158: \[
159: Q_N^W(P_N^Wf)\to Q_W(f)
160: \]
161: 
162: uniformly for
```

```text
214: we get
215: 
216: \[
217: |Q_N^W(P_N^Wf)-Q_W(f)|
218: =
219: |a^*\Delta_N^{(m)}a|
220: \leq
```

### original_results/finite_bombieri_stability/level4_candidate/classical_object_import/PHASE_12A_CLASSICAL_OBJECT_IMPORT_GATE.md

score: 6

```text
9: The target is a serious RH-adjacent finite-to-infinite detection theorem:
10: 
11: \[
12: Q_W(f)<0
13: \Longrightarrow
14: Q_N(P_Nf)<0
15: \]
```

```text
18: 
19: This would still not prove RH.
20: 
21: But it would be a serious contribution candidate because it would connect finite certified computation to a genuine infinite Weil/Bombieri obstruction.
22: 
23: ---
24: 
```

```text
28: 
29: ## Target Theorem 12-T
30: 
31: Let \(Q_W\) be the true Weil/Bombieri quadratic form on an admissible test-function domain \(\mathcal D_W\).
32: 
33: Let \(Q_N\) be finite approximating forms and let
34: 
```

```text
41: Suppose \(f\in\mathcal D_W\) satisfies
42: 
43: \[
44: Q_W(f)\leq-\eta
45: \]
46: 
47: for some \(\eta>0\).
```

```text
49: If
50: 
51: \[
52: |Q_N(P_Nf)-Q_W(f)|<\eta/2
53: \]
54: 
55: for all sufficiently large \(N\), then
```

```text
65: The breakthrough-candidate work is to prove the error bound for real classical objects:
66: 
67: \[
68: |Q_N(P_Nf)-Q_W(f)|<\eta/2.
69: \]
70: 
71: ---
```

```text
90: We must import or explicitly mark as missing:
91: 
92: \[
93: Q_W,
94: \quad
95: \mathcal D_W,
96: \quad
```

```text
94: \quad
95: \mathcal D_W,
96: \quad
97: B_W,
98: \quad
99: V_N,
100: \quad
```

### weil_reconstruction/symbolic/PHASE_8J_COMPLEX_STAR_CONVENTION_AUDIT.md

score: 6

```text
14: f^*(x)=x^{-1}f(1/x).
15: \]
16: 
17: However, Bombieri's positivity statements involve complex-valued test functions.
18: 
19: For complex-valued functions, there is a major convention risk:
20: 
```

```text
34: 
35: This is not a proof of RH.
36: 
37: This is not a new Weil criterion.
38: 
39: This phase blocks finite-rank positivity code until the source convention is fully locked.
40: 
```

```text
138: 
139: Before any positivity computation, the repository must source-lock:
140: 
141: 1. whether Bombieri's \(g^*\) includes complex conjugation;
142: 2. whether \(f^*\) in \(T[f]=T[f^*]\) is the same operation as the positivity adjoint;
143: 3. whether convolution \(f*f^*\) is algebraic, Hermitian, or context-dependent;
144: 4. how complex-valued test functions are paired;
```

```text
139: Before any positivity computation, the repository must source-lock:
140: 
141: 1. whether Bombieri's \(g^*\) includes complex conjugation;
142: 2. whether \(f^*\) in \(T[f]=T[f^*]\) is the same operation as the positivity adjoint;
143: 3. whether convolution \(f*f^*\) is algebraic, Hermitian, or context-dependent;
144: 4. how complex-valued test functions are paired;
145: 5. which formula yields the nonnegative sum under RH.
```

```text
140: 
141: 1. whether Bombieri's \(g^*\) includes complex conjugation;
142: 2. whether \(f^*\) in \(T[f]=T[f^*]\) is the same operation as the positivity adjoint;
143: 3. whether convolution \(f*f^*\) is algebraic, Hermitian, or context-dependent;
144: 4. how complex-valued test functions are paired;
145: 5. which formula yields the nonnegative sum under RH.
146: 
```

```text
158: f^*(s)=f(1-s).
159: \]
160: 
161: Multiplicative convolution identity:
162: 
163: \[
164: (f*g)(s)=f(s)g(s).
```

```text
166: 
167: ## PARTIAL
168: 
169: Bombieri theorem statement involving
170: 
171: \[
172: g(\rho)g(1-\rho).
```

```text
176: 
177: Hermitian positivity convention for complex-valued test functions.
178: 
179: Exact role of complex conjugation in Bombieri's \(g^*\).
180: 
181: Exact role of complex conjugation in Bombieri's \(f*f^*\).
182: 
```

### horizontal_defect/PHASE_7A_HORIZONTAL_INFORMATION_AUDIT.md

score: 5

```text
58: 
59: ## Category C — Positivity-compatible
60: 
61: An object is positivity-compatible if it can be placed inside a nonnegative quadratic, energy, norm, or positive semidefinite form.
62: 
63: This category matters because RH is equivalent to several positivity principles.
64: 
```

```text
64: 
65: ## Category D — Explicit-formula compatible
66: 
67: An object is explicit-formula compatible if it can be related to primes or arithmetic data through a Weil/Guinand-type explicit formula.
68: 
69: This category matters because RH is not only a zero-side statement; it is tied to prime-side oscillation.
70: 
```

```text
85: | \(N(T)\) | Yes | No | No | Yes, indirectly | Yes | Not sufficient |
86: | \(E(T)=N(T)-M(T)\) | Yes | No | No | Yes, indirectly | Yes | Not sufficient |
87: | \(S(T)\) through \(N(T)\) | Mostly yes | No direct beta data | No | Yes | Yes | Not sufficient |
88: | Li coefficients \(\lambda_n\) | No | Yes globally | Positivity criterion | Yes | Yes | Classical RH-equivalent |
89: | Weil quadratic form | No | Yes | Yes | Yes | Partly | Classical RH-equivalent |
90: | Single-zero Li horizontal contrast | No | Yes | Not globally positive | Limited | Yes | Useful diagnostic |
91: | Linear Li filters | No | Yes | Generally cancellation-prone | Possibly | Yes | Obstructed |
```

```text
86: | \(E(T)=N(T)-M(T)\) | Yes | No | No | Yes, indirectly | Yes | Not sufficient |
87: | \(S(T)\) through \(N(T)\) | Mostly yes | No direct beta data | No | Yes | Yes | Not sufficient |
88: | Li coefficients \(\lambda_n\) | No | Yes globally | Positivity criterion | Yes | Yes | Classical RH-equivalent |
89: | Weil quadratic form | No | Yes | Yes | Yes | Partly | Classical RH-equivalent |
90: | Single-zero Li horizontal contrast | No | Yes | Not globally positive | Limited | Yes | Useful diagnostic |
91: | Linear Li filters | No | Yes | Generally cancellation-prone | Possibly | Yes | Obstructed |
92: | Squared horizontal contrast | No | Yes | Yes on single quartet | Hard globally | Yes | Candidate but aggregation issue |
```

```text
161: 
162: Research question:
163: 
164: Can any natural \(\phi\) arise from a Weil-positive test function?
165: 
166: ## Direction 2 — Li-coordinate radial defect
167: 
```

```text
193: 
194: without cancellation?
195: 
196: ## Direction 3 — Weil quadratic finite-rank truncation
197: 
198: Weil positivity is classical and RH-equivalent.
199: 
```

```text
195: 
196: ## Direction 3 — Weil quadratic finite-rank truncation
197: 
198: Weil positivity is classical and RH-equivalent.
199: 
200: Research question:
201: 
```

```text
219: 
220: 1. a positive result constructing a usable horizontal-defect energy;
221: 2. a negative result proving a broad obstruction for linear filters;
222: 3. a finite-rank Weil truncation theorem;
223: 4. a rigorous synthetic-zero testbed for horizontal-defect functionals.
224: 
225: The most realistic next target is the obstruction theorem for linear filters.
```

### original_results/finite_bombieri_stability/contribution_branch/classical_import_map/PHASE_10AN_CLASSICAL_IMPORT_MAP.md

score: 5

```text
2: 
3: ## Purpose
4: 
5: Phase 10AM defined a toy-but-honest Weil-form abstraction:
6: 
7: \[
8: Q_\infty,\quad Q_N,\quad P_N,\quad E_N(f).
```

```text
8: Q_\infty,\quad Q_N,\quad P_N,\quad E_N(f).
9: \]
10: 
11: Phase 10AN maps each toy object to the classical Weil/Bombieri object that must eventually replace it.
12: 
13: This phase does not prove RH.
14: 
```

```text
24: 
25: | Toy abstraction | Classical object needed | Current status |
26: |---|---|---|
27: | \(\mathcal D\) | admissible Weil/Bombieri test-function space | missing |
28: | \(Q_\infty\) | true infinite Weil/Bombieri quadratic form | missing |
29: | \(B_\infty\) | true Hermitian Weil/Bombieri bilinear or sesquilinear form | missing |
30: | \(V_N\) | finite-dimensional truncation or approximation space | missing |
```

```text
25: | Toy abstraction | Classical object needed | Current status |
26: |---|---|---|
27: | \(\mathcal D\) | admissible Weil/Bombieri test-function space | missing |
28: | \(Q_\infty\) | true infinite Weil/Bombieri quadratic form | missing |
29: | \(B_\infty\) | true Hermitian Weil/Bombieri bilinear or sesquilinear form | missing |
30: | \(V_N\) | finite-dimensional truncation or approximation space | missing |
31: | \(M_N\) | finite Bombieri/Weil matrix from the classical construction | partially modeled |
```

```text
26: |---|---|---|
27: | \(\mathcal D\) | admissible Weil/Bombieri test-function space | missing |
28: | \(Q_\infty\) | true infinite Weil/Bombieri quadratic form | missing |
29: | \(B_\infty\) | true Hermitian Weil/Bombieri bilinear or sesquilinear form | missing |
30: | \(V_N\) | finite-dimensional truncation or approximation space | missing |
31: | \(M_N\) | finite Bombieri/Weil matrix from the classical construction | partially modeled |
32: | \(P_N\) | projection/sampling/truncation map | missing |
```

```text
28: | \(Q_\infty\) | true infinite Weil/Bombieri quadratic form | missing |
29: | \(B_\infty\) | true Hermitian Weil/Bombieri bilinear or sesquilinear form | missing |
30: | \(V_N\) | finite-dimensional truncation or approximation space | missing |
31: | \(M_N\) | finite Bombieri/Weil matrix from the classical construction | partially modeled |
32: | \(P_N\) | projection/sampling/truncation map | missing |
33: | \(E_N(f)\) | finite-to-infinite approximation error | missing |
34: | \(\varepsilon_N(f)\) | quantitative convergence rate | missing |
```

```text
43: \mathcal D.
44: \]
45: 
46: The classical project must replace this with the correct Weil/Bombieri test-function space.
47: 
48: The needed object is:
49: 
```

```text
53: 
54: Requirements:
55: 
56: 1. closed under the operations used in the Weil/Bombieri formula;
57: 2. compatible with Mellin transform or Fourier-transform normalization;
58: 3. compatible with the involution/star operation;
59: 4. supports positivity statements;
```

### original_results/finite_bombieri_stability/contribution_branch/tractable_convergence_model/PHASE_10AQ_TRACTABLE_FINITE_TEST_CLASS_MODEL.md

score: 5

```text
6: 
7: \[
8: \sup_{f\in\mathcal F}
9: |Q_N^W(P_N^Wf)-Q_W(f)|
10: \leq
11: \varepsilon_N(\mathcal F),
12: \qquad
```

```text
57: 
58: # 2. Infinite Gram matrix
59: 
60: Define the infinite Weil/Bombieri Gram matrix on this finite test family by
61: 
62: \[
63: G^{(\infty)}_{ij}
```

```text
62: \[
63: G^{(\infty)}_{ij}
64: =
65: B_W(\phi_i,\phi_j),
66: \]
67: 
68: where \(B_W\) is the Hermitian form associated to \(Q_W\).
```

```text
65: B_W(\phi_i,\phi_j),
66: \]
67: 
68: where \(B_W\) is the Hermitian form associated to \(Q_W\).
69: 
70: Then for
71: 
```

```text
76: we have
77: 
78: \[
79: Q_W(f)=a^*G^{(\infty)}a.
80: \]
81: 
82: ---
```

```text
116: Then
117: 
118: \[
119: |Q_N^W(P_N^W f)-Q_W(f)|
120: =
121: |a^*\Delta_N^{(m)}a|.
122: \]
```

```text
138: we get
139: 
140: \[
141: |Q_N^W(P_N^W f)-Q_W(f)|
142: \leq
143: R^2\|\Delta_N^{(m)}\|_2.
144: \]
```

```text
163: 
164: \[
165: \sup_{f\in\mathcal F_R^{(m)}}
166: |Q_N^W(P_N^W f)-Q_W(f)|
167: \leq
168: R^2\|G^{(N)}-G^{(\infty)}\|_2.
169: \]
```

### proofs/PHASE_5S_SECOND_LOG_MOMENT_LI_WEIL_BRIDGE.md

score: 5

```text
1: # Phase 5S — Second Log-Moment Li Test Function and Weil Bridge
2: 
3: ## Status
4: 
```

```text
4: 
5: EXACT MELLIN BRIDGE PROVED.
6: 
7: FINITE SIGNED WEIL-RANK QUESTION OPEN.
8: 
9: ## Prior-art correction
10: 
```

```text
16: 1-\left(1-\frac1s\right)^n
17: \]
18: 
19: is already explicitly embedded into Guinand-Weil explicit-formula machinery in the classical Li literature.
20: 
21: Bombieri-Lagarias derive arithmetic formulas for Li coefficients through the Guinand-Weil explicit formula.
22: 
```

```text
18: 
19: is already explicitly embedded into Guinand-Weil explicit-formula machinery in the classical Li literature.
20: 
21: Bombieri-Lagarias derive arithmetic formulas for Li coefficients through the Guinand-Weil explicit formula.
22: 
23: Later treatments record the corresponding inverse-Mellin test function explicitly.
24: 
```

```text
92: }
93: \]
94: 
95: This is classical Li/Guinand-Weil machinery.
96: 
97: ---
98: 
```

```text
316: 
317: 2. its zero-side summation in the Li coefficients;
318: 
319: 3. its Guinand-Weil explicit-formula arithmetic interpretation;
320: 
321: 4. its inverse-Mellin test-function realization.
322: 
```

```text
338: 
339: ---
340: 
341: # 7. Weil quadratic-form question
342: 
343: The Weil quadratic form is built from Hermitian convolution structures.
344: 
```

```text
340: 
341: # 7. Weil quadratic-form question
342: 
343: The Weil quadratic form is built from Hermitian convolution structures.
344: 
345: The test function
346: 
```

### proofs/PHASE_5T_HERMITIAN_SYMMETRIZATION_AND_WEIL_RANK_OBSTRUCTION.md

score: 5

```text
1: # Phase 5T — Hermitian Symmetrization and Weil-Rank Obstruction
2: 
3: ## Status
4: 
```

```text
16: y^2G_n(y)
17: \]
18: 
19: admits a finite signed Hermitian convolution-square decomposition.
20: 
21: The answer is no.
22: 
```

```text
22: 
23: The obstruction is exact and follows from reflection symmetry.
24: 
25: The correct Weil-side object corresponding to the real Li susceptibility is instead the Hermitian symmetrization of \(G_n^{(2)}\).
26: 
27: ---
28: 
```

```text
36: \overline{u(-y)}.
37: \]
38: 
39: Define the Hermitian autocorrelation
40: 
41: \[
42: h
```

```text
103: }
104: \]
105: 
106: Thus every real autocorrelation is even.
107: 
108: ---
109: 
```

```text
143: }
144: \]
145: 
146: Hence every finite real signed sum of Hermitian convolution squares remains in the Hermitian reflection class.
147: 
148: The signs do not alter this constraint.
149: 
```

```text
220: 
221: ---
222: 
223: # 4. Finite signed Weil-rank obstruction
224: 
225: Suppose, for contradiction, that
226: 
```

```text
293: 
294: # 5. Correction to the Phase 5S target
295: 
296: The finite signed Weil-rank question posed directly for
297: 
298: \[
299: G_n^{(2)}
```

### scripts/run_phase12b_source_scan.py

score: 5

```text
2: import re
3: 
4: ROOT = Path(".")
5: OUT = Path("original_results/finite_bombieri_stability/level4_candidate/true_weil_form_import")
6: OUT.mkdir(parents=True, exist_ok=True)
7: 
8: patterns = [
```

```text
6: OUT.mkdir(parents=True, exist_ok=True)
7: 
8: patterns = [
9:     "T[f]",
10:     "T[f^*]",
11:     "sum_\\rho",
12:     "sum\\_rho",
```

```text
7: 
8: patterns = [
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
15:     "explicit formula",
16:     "f^*(x)",
```

```text
11:     "sum_\\rho",
12:     "sum\\_rho",
13:     "Bombieri",
14:     "Weil",
15:     "explicit formula",
16:     "f^*(x)",
17:     "Mellin",
```

```text
15:     "explicit formula",
16:     "f^*(x)",
17:     "Mellin",
18:     "quadratic form",
19:     "positivity",
20: ]
21: 
```

```text
53: report = []
54: report.append("# Phase 12B Source Scan Report\n\n")
55: report.append("## Purpose\n\n")
56: report.append("Search local project files for previously extracted Bombieri/Weil source objects.\n\n")
57: report.append("## Top hits\n\n")
58: 
59: for hit in hits[:20]:
```

### weil_reconstruction/finite_truncations/PHASE_8N_FINITE_TRUNCATION_EXTRACTION_WORKSHEET.md

score: 5

```text
4: 
5: Phase 8M recorded the off-critical negative-direction mechanism at statement level.
6: 
7: Phase 8N prepares the source-grounded extraction of Bombieri's finite truncation construction.
8: 
9: This phase does not implement a matrix.
10: 
```

```text
12: 
13: This phase does not prove RH.
14: 
15: This phase does not claim a new Weil criterion.
16: 
17: ---
18: 
```

```text
18: 
19: # 1. Why this phase is necessary
20: 
21: The project now knows the symbolic Bombieri-Weil object:
22: 
23: \[
24: T[f*f^*].
```

```text
21: The project now knows the symbolic Bombieri-Weil object:
22: 
23: \[
24: T[f*f^*].
25: \]
26: 
27: It also knows the high-level source claim that finite truncations and negative eigenvalues are studied in Bombieri's framework.
```

```text
24: T[f*f^*].
25: \]
26: 
27: It also knows the high-level source claim that finite truncations and negative eigenvalues are studied in Bombieri's framework.
28: 
29: However, the project does not yet know the exact finite truncation construction.
30: 
```

```text
36: 
37: # 2. Extraction target
38: 
39: The next source-extraction target is Bombieri's finite-dimensional approximation to the Weil quadratic form.
40: 
41: The extraction must identify:
42: 
```

```text
40: 
41: The extraction must identify:
42: 
43: 1. the infinite quadratic form;
44: 2. the variable basis;
45: 3. the indexing set;
46: 4. the matrix entries;
```

```text
68: 
69: ## Infinite object
70: 
71: Record the exact infinite quadratic form.
72: 
73: ## Basis
74: 
```

### weil_reconstruction/formulations/PHASE_8C_EXACT_FORMULATION_SELECTION.md

score: 5

```text
2: 
3: ## Purpose
4: 
5: Phase 8A began the classical Weil reconstruction program.
6: 
7: Phase 8B defined the object map.
8: 
```

```text
10: 
11: This is not a proof of RH.
12: 
13: This is not a new Weil criterion.
14: 
15: This is not a novelty claim.
16: 
```

```text
20: 
21: # 1. Why a selection is necessary
22: 
23: The phrase "Weil criterion" can refer to several closely related forms:
24: 
25: 1. the Weil explicit formula;
26: 2. Weil positivity;
```

```text
22: 
23: The phrase "Weil criterion" can refer to several closely related forms:
24: 
25: 1. the Weil explicit formula;
26: 2. Weil positivity;
27: 3. Bombieri's quadratic form formulation;
28: 4. Li-type positivity criteria;
```

```text
23: The phrase "Weil criterion" can refer to several closely related forms:
24: 
25: 1. the Weil explicit formula;
26: 2. Weil positivity;
27: 3. Bombieri's quadratic form formulation;
28: 4. Li-type positivity criteria;
29: 5. Guinand-Weil explicit formula variants;
```

```text
24: 
25: 1. the Weil explicit formula;
26: 2. Weil positivity;
27: 3. Bombieri's quadratic form formulation;
28: 4. Li-type positivity criteria;
29: 5. Guinand-Weil explicit formula variants;
30: 6. operator-theoretic formulations;
```

```text
26: 2. Weil positivity;
27: 3. Bombieri's quadratic form formulation;
28: 4. Li-type positivity criteria;
29: 5. Guinand-Weil explicit formula variants;
30: 6. operator-theoretic formulations;
31: 7. finite truncation models.
32: 
```

```text
40: 
41: \[
42: \boxed{
43: \text{Bombieri-style Weil quadratic form reconstruction.}
44: }
45: \]
46: 
```

### weil_reconstruction/fourier_side/PHASE_8P_FOURIER_SIDE_EXTRACTION_WORKSHEET.md

score: 5

```text
1: # Phase 8P — Fourier-Side Infinite Quadratic Form Extraction Worksheet
2: 
3: ## Purpose
4: 
```

```text
2: 
3: ## Purpose
4: 
5: Phase 8O source-locked the roadmap for Bombieri's finite truncation program.
6: 
7: Phase 8P prepares the extraction of the Fourier-side infinite quadratic form from Bombieri Sections 5 and 6.
8: 
```

```text
4: 
5: Phase 8O source-locked the roadmap for Bombieri's finite truncation program.
6: 
7: Phase 8P prepares the extraction of the Fourier-side infinite quadratic form from Bombieri Sections 5 and 6.
8: 
9: This phase does not implement a matrix.
10: 
```

```text
12: 
13: This phase does not prove RH.
14: 
15: This phase does not claim a new Weil criterion.
16: 
17: ---
18: 
```

```text
18: 
19: # 1. Why this phase comes before Section 8
20: 
21: Bombieri's Section 8 finite approximations approximate an earlier Fourier-side reformulation.
22: 
23: Therefore, before extracting finite matrices, the project must extract the infinite object being approximated.
24: 
```

```text
25: The correct order is:
26: 
27: \[
28: \text{Weil functional}
29: \rightarrow
30: \text{Fourier-side infinite quadratic form}
31: \rightarrow
```

```text
27: \[
28: \text{Weil functional}
29: \rightarrow
30: \text{Fourier-side infinite quadratic form}
31: \rightarrow
32: \text{finite approximation}
33: \rightarrow
```

```text
42: 
43: # 2. Extraction target
44: 
45: The next source target is Bombieri Sections 5 and 6.
46: 
47: The extraction must identify:
48: 
```

### weil_reconstruction/fourier_side/PHASE_8R_LOG_COORDINATE_BRIDGE.md

score: 5

```text
2: 
3: ## Purpose
4: 
5: Phase 8Q recorded the source evidence chain for Bombieri's Fourier-side program.
6: 
7: Phase 8R builds the algebraic bridge from the multiplicative \(x\)-variable to the additive log-coordinate.
8: 
```

```text
42: f(e^u)=e^{-u/2}F(u).
43: \]
44: 
45: This is the natural log-coordinate normalization because it converts the mass terms in Bombieri's \(T[f]\) formula into symmetric hyperbolic weights.
46: 
47: ---
48: 
```

```text
48: 
49: # 2. Involution in log coordinates
50: 
51: Bombieri's algebraic involution is
52: 
53: \[
54: f^*(x)=x^{-1}f(1/x).
```

```text
132: f^*(n)=n^{-1/2}F(-\log n).
133: \]
134: 
135: Therefore Bombieri's prime-side term becomes
136: 
137: \[
138: -\sum_{n=1}^{\infty}
```

```text
144: 
145: ---
146: 
147: # 5. Multiplicative convolution becomes additive convolution
148: 
149: Let \(h=f*g\), where
150: 
```

```text
203: 
204: \[
205: \boxed{
206: \text{multiplicative convolution becomes additive convolution.}
207: }
208: \]
209: 
```

```text
209: 
210: ---
211: 
212: # 6. Positivity convolution in log coordinates
213: 
214: For the Hermitian positivity adjoint, log coordinates convert the reflected-conjugate operation into
215: 
```

```text
217: G^*_{\mathrm{pos}}(u)=\overline{G(-u)}.
218: \]
219: 
220: Thus the positivity convolution becomes
221: 
222: \[
223: F*F^*_{\mathrm{pos}}.
```

### weil_reconstruction/sources/extractions/PHASE_8F_BOMBIERI_THEOREM_EXTRACTION.md

score: 5

```text
1: # Phase 8F — Bombieri Theorem 1 and Theorem 2 Extraction
2: 
3: ## Purpose
4: 
```

```text
2: 
3: ## Purpose
4: 
5: Phase 8E locked only high-level structural facts from Bombieri and Suzuki.
6: 
7: Phase 8F extracts the first exact theorem-level objects from Bombieri's Section 3.
8: 
```

```text
4: 
5: Phase 8E locked only high-level structural facts from Bombieri and Suzuki.
6: 
7: Phase 8F extracts the first exact theorem-level objects from Bombieri's Section 3.
8: 
9: This is not a proof of RH.
10: 
```

```text
8: 
9: This is not a proof of RH.
10: 
11: This is not a new Weil criterion.
12: 
13: This is a reconstruction of known classical source material.
14: 
```

```text
16: 
17: # 1. Source
18: 
19: Enrico Bombieri, **Remarks on Weil's quadratic functional in the theory of prime numbers, I**, Rend. Mat. Acc. Lincei, Serie 9, Vol. 11, 183-233, 2000.
20: 
21: Relevant section:
22: 
```

```text
26: 
27: # 2. Extracted setup
28: 
29: Bombieri considers test functions
30: 
31: \[
32: f(x)\in C_0^\infty((0,\infty))
```

```text
32: f(x)\in C_0^\infty((0,\infty))
33: \]
34: 
35: that are multiplicative convolutions of a function \(g\) and its transpose conjugate \(g^*\).
36: 
37: The multiplicative convolution is written schematically as
38: 
```

```text
34: 
35: that are multiplicative convolutions of a function \(g\) and its transpose conjugate \(g^*\).
36: 
37: The multiplicative convolution is written schematically as
38: 
39: \[
40: f(x)
```

### weil_reconstruction/symbolic/PHASE_8I_INVOLUTION_CONVOLUTION_AUDIT.md

score: 5

```text
1: # Phase 8I — Involution and Convolution Identity Audit
2: 
3: ## Purpose
4: 
```

```text
2: 
3: ## Purpose
4: 
5: Phase 8H locked Bombieri's full linear functional
6: 
7: \[
8: T[f].
```

```text
5: Phase 8H locked Bombieri's full linear functional
6: 
7: \[
8: T[f].
9: \]
10: 
11: Phase 8I audits the symbolic identities surrounding the involution
```

```text
14: f^*(x)=x^{-1}f(1/x)
15: \]
16: 
17: and multiplicative convolution.
18: 
19: This phase does not prove RH.
20: 
```

```text
18: 
19: This phase does not prove RH.
20: 
21: This phase does not create a new Weil criterion.
22: 
23: This phase does not implement finite-rank Weil matrices.
24: 
```

```text
20: 
21: This phase does not create a new Weil criterion.
22: 
23: This phase does not implement finite-rank Weil matrices.
24: 
25: ---
26: 
```

```text
26: 
27: # 1. Current locked convention
28: 
29: From the Phase 8H extraction, the project currently records Bombieri's involution as
30: 
31: \[
32: f^*(x)=x^{-1}f(1/x).
```

```text
38: f(s)=\int_0^\infty f(x)x^{s-1}\,dx.
39: \]
40: 
41: The multiplicative convolution is
42: 
43: \[
44: (f*g)(x)
```

### horizontal_defect/theorems/PHASE_7F_QUADRATIC_LI_FILTER_POSITIVITY.md

score: 4

```text
208: 
209: ---
210: 
211: # 5. General quadratic form version
212: 
213: Let
214: 
```

```text
218: (\Delta_1(u,\theta),\ldots,\Delta_N(u,\theta))^T.
219: \]
220: 
221: For any positive semidefinite matrix
222: 
223: \[
224: A\succeq0,
```

```text
224: A\succeq0,
225: \]
226: 
227: the quadratic form
228: 
229: \[
230: Q_A(u,\theta)
```

```text
234: 
235: is nonnegative.
236: 
237: If \(A\) is positive definite and the vector \(\Delta(u,\theta)\) is never zero for \(u\ne0\), then \(Q_A\) is strictly positive.
238: 
239: The case \(N=2\) with \(A=I\) already gives strict phase-uniform positivity.
240: 
```

```text
266: \Delta_m\Delta_n.
267: \]
268: 
269: Such terms do not automatically appear as a standard Weil/Guinand zero-side expression.
270: 
271: Therefore the next serious problem is:
272: 
```

```text
272: 
273: \[
274: \boxed{
275: \text{Can the quadratic Li-filter lift be represented, bounded, or approximated by Weil-positive machinery?}
276: }
277: \]
278: 
```

### original_results/finite_bombieri_stability/contribution_branch/bombieri_weil_template/SPECIALIZATION_TEMPLATE_LOCK.md

score: 4

```text
3: ## Infinite form
4: 
5: \[
6: Q_W:\mathcal D\to\mathbb R
7: \]
8: 
9: is the infinite Weil/Bombieri-style quadratic form.
```

```text
6: Q_W:\mathcal D\to\mathbb R
7: \]
8: 
9: is the infinite Weil/Bombieri-style quadratic form.
10: 
11: ## Finite forms
12: 
```

```text
23: ## Required convergence
24: 
25: \[
26: Q_N(P_Nf)\to Q_W(f).
27: \]
28: 
29: ## Quantitative target
```

```text
29: ## Quantitative target
30: 
31: \[
32: |Q_N(P_Nf)-Q_W(f)|\leq \varepsilon_N(f)\to0.
33: \]
34: 
35: ## Current status
```

```text
34: 
35: ## Current status
36: 
37: BOMBIIERI_WEIL_SPECIALIZATION_TEMPLATE
38: 
39: CONVERGENCE_THEOREM_MISSING
40: 
```

### original_results/finite_bombieri_stability/contribution_branch/classical_definition_extraction/PHASE_10AO_CLASSICAL_DEFINITION_EXTRACTION_LEDGER.md

score: 4

```text
50: | Toy finite matrices | \(M_N\) | PROJECT DEFINITION | defined in Phase 10AM |
51: | Toy approximation maps | \(P_N\) | PROJECT DEFINITION | defined abstractly in Phase 10AM |
52: | Toy error term | \(E_N(f)\) | PROJECT DEFINITION | defined in Phase 10AM |
53: | True Weil/Bombieri test domain | \(\mathcal D_W\) | MISSING | must be imported |
54: | True Weil/Bombieri form | \(Q_W\) | MISSING | must be imported |
55: | RH positivity relation | RH \(\leftrightarrow Q_W\geq0\) | MISSING | must be imported |
56: | Classical finite spaces | \(V_N^{W}\) | MISSING | must be imported |
```

```text
51: | Toy approximation maps | \(P_N\) | PROJECT DEFINITION | defined abstractly in Phase 10AM |
52: | Toy error term | \(E_N(f)\) | PROJECT DEFINITION | defined in Phase 10AM |
53: | True Weil/Bombieri test domain | \(\mathcal D_W\) | MISSING | must be imported |
54: | True Weil/Bombieri form | \(Q_W\) | MISSING | must be imported |
55: | RH positivity relation | RH \(\leftrightarrow Q_W\geq0\) | MISSING | must be imported |
56: | Classical finite spaces | \(V_N^{W}\) | MISSING | must be imported |
57: | Classical finite matrices | \(M_N^{W}\) | PARTIAL PROJECT MODEL | modeled, not fully validated |
```

```text
52: | Toy error term | \(E_N(f)\) | PROJECT DEFINITION | defined in Phase 10AM |
53: | True Weil/Bombieri test domain | \(\mathcal D_W\) | MISSING | must be imported |
54: | True Weil/Bombieri form | \(Q_W\) | MISSING | must be imported |
55: | RH positivity relation | RH \(\leftrightarrow Q_W\geq0\) | MISSING | must be imported |
56: | Classical finite spaces | \(V_N^{W}\) | MISSING | must be imported |
57: | Classical finite matrices | \(M_N^{W}\) | PARTIAL PROJECT MODEL | modeled, not fully validated |
58: | Classical approximation maps | \(P_N^W\) | MISSING | must be imported or defined |
```

```text
56: | Classical finite spaces | \(V_N^{W}\) | MISSING | must be imported |
57: | Classical finite matrices | \(M_N^{W}\) | PARTIAL PROJECT MODEL | modeled, not fully validated |
58: | Classical approximation maps | \(P_N^W\) | MISSING | must be imported or defined |
59: | Convergence theorem | \(Q_N(P_Nf)\to Q_W(f)\) | MISSING | central missing bridge |
60: | Quantitative convergence rate | \(\varepsilon_N(f)\) | MISSING | central missing quantitative object |
61: 
62: ---
```

```text
194: 
195: ## Missing classical object 2
196: 
197: Exact infinite Weil/Bombieri form:
198: 
199: \[
200: Q_W.
```

```text
197: Exact infinite Weil/Bombieri form:
198: 
199: \[
200: Q_W.
201: \]
202: 
203: Status:
```

```text
215: \[
216: \text{RH}
217: \Longleftrightarrow
218: Q_W(f)\geq0
219: \quad
220: \forall f\in\mathcal D_W.
221: \]
```

```text
259: Convergence theorem:
260: 
261: \[
262: Q_N(P_N^Wf)\to Q_W(f).
263: \]
264: 
265: Status:
```

### original_results/finite_bombieri_stability/contribution_branch/final_professor_package/ONE_PAGE_SUMMARY.md

score: 4

```text
2: 
3: ## Project
4: 
5: A Conditional Finite-to-Infinite Transfer Framework for Certified Gram-Matrix Approximations in Weil/Bombieri-Style Models
6: 
7: ## Main idea
8: 
```

```text
6: 
7: ## Main idea
8: 
9: The project studies when finite certified matrix computations can be connected to an infinite Weil/Bombieri-style quadratic form.
10: 
11: ## Main conditional theorem
12: 
```

```text
50: 
51: \[
52: \sup_{f\in\mathcal F_R^{(m)}}
53: |Q_N^W(P_N^Wf)-Q_W(f)|
54: \leq
55: R^2m
56: \left(
```

## Scan conclusion

This scan identifies candidate local references, but does not by itself prove that the exact classical quadratic Weil positivity form has been imported.

## Exact audit strings

PHASE_12C_QUADRATIC_SOURCE_SCAN_COMPLETE

LOCAL_QUADRATIC_FORM_SCAN_PERFORMED

