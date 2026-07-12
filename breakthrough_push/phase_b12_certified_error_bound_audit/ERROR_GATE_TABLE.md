# Error Gate Table

| Gate | Status | Certification impact |
|---|---|---|
| Quadrature error | HARD_BUT_POSSIBLE | Needs interval quadrature or derivative bounds |
| Convolution error | NEEDS_NEW_THEOREM_OR_IMPLEMENTATION | Nested integral certification required |
| Archimedean singularity | BLOCKS_CERTIFICATION | Must handle removable singularity rigorously |
| Floating-point rounding | EASY_TO_CERTIFY | Use outward-rounded intervals or rationals |
| Basis smoothness | BLOCKS_TRUE_WEIL_CERTIFICATION | Replace triangular toy basis with \(C_c^\infty\) basis |
| Pole constraints | REQUIRES_SOURCE_REVIEW | Exact admissibility must be validated |
| Source normalization | REQUIRES_REVIEW | Must use one locked normalization |

Exact strings:

ERROR_GATES_AUDITED

QUADRATURE_ERROR_HARD_BUT_POSSIBLE

CONVOLUTION_ERROR_NEEDS_NEW_THEOREM_OR_IMPLEMENTATION

ARCHIMEDEAN_SINGULARITY_BLOCKS_CERTIFICATION

ROUNDING_ERROR_EASY_TO_CERTIFY

TOY_BASIS_BLOCKS_TRUE_WEIL_CERTIFICATION

POLE_CONSTRAINTS_REQUIRE_SOURCE_REVIEW

SOURCE_NORMALIZATION_REQUIRES_REVIEW

INTERVAL_CANDIDATE_NOT_CERTIFIED

BREAKTHROUGH_NOT_ACHIEVED
