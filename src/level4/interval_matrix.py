from __future__ import annotations

from dataclasses import dataclass
from typing import List, Sequence, Dict, Any
import json
from pathlib import Path


@dataclass(frozen=True)
class Interval:
    """Closed real interval [lo, hi]."""

    lo: float
    hi: float

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise ValueError(f"Invalid interval with lo > hi: [{self.lo}, {self.hi}]")

    def __add__(self, other: "Interval") -> "Interval":
        return Interval(self.lo + other.lo, self.hi + other.hi)

    def __sub__(self, other: "Interval") -> "Interval":
        return Interval(self.lo - other.hi, self.hi - other.lo)

    def __mul__(self, other: "Interval") -> "Interval":
        candidates = [
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        ]
        return Interval(min(candidates), max(candidates))

    def scale(self, scalar: float) -> "Interval":
        values = [scalar * self.lo, scalar * self.hi]
        return Interval(min(values), max(values))

    def contains_zero(self) -> bool:
        return self.lo <= 0.0 <= self.hi

    def strictly_negative(self) -> bool:
        return self.hi < 0.0

    def to_dict(self) -> Dict[str, float]:
        return {"lo": self.lo, "hi": self.hi}


class IntervalMatrix:
    """Real interval matrix skeleton for certified arithmetic matrix experiments."""

    def __init__(self, entries: List[List[Interval]]) -> None:
        if not entries:
            raise ValueError("Matrix must be nonempty")
        n = len(entries)
        if any(len(row) != n for row in entries):
            raise ValueError("Only square matrices are supported")
        self.entries = entries
        self.n = n

    def hermitian_residual(self) -> List[List[Interval]]:
        """Real skeleton residual R_ij = M_ij - M_ji."""
        residual: List[List[Interval]] = []
        for i in range(self.n):
            row: List[Interval] = []
            for j in range(self.n):
                row.append(self.entries[i][j] - self.entries[j][i])
            residual.append(row)
        return residual

    def residual_contains_zero(self) -> bool:
        return all(
            self.hermitian_residual()[i][j].contains_zero()
            for i in range(self.n)
            for j in range(self.n)
        )

    def residual_exact_zero(self) -> bool:
        """
        Certify exact real symmetry at the interval-entry level.

        Important: interval subtraction of the same non-point interval [a,b] - [a,b]
        produces [a-b, b-a], not [0,0], because dependency is lost.
        Therefore exact interval symmetry should be checked by comparing paired
        interval entries directly.
        """
        return all(
            self.entries[i][j].lo == self.entries[j][i].lo
            and self.entries[i][j].hi == self.entries[j][i].hi
            for i in range(self.n)
            for j in range(self.n)
        )

    def rayleigh_interval(self, vector: Sequence[float]) -> Interval:
        if len(vector) != self.n:
            raise ValueError(f"Vector length {len(vector)} does not match matrix size {self.n}")
        total = Interval(0.0, 0.0)
        for i in range(self.n):
            for j in range(self.n):
                coeff = vector[i] * vector[j]
                total = total + self.entries[i][j].scale(coeff)
        return total

    def negative_direction_certificate(self, vector: Sequence[float]) -> Dict[str, Any]:
        rq = self.rayleigh_interval(vector)
        verdict = "CERTIFIED_NEGATIVE_DIRECTION" if rq.strictly_negative() else "NOT_CERTIFIED_NEGATIVE"
        return {
            "verdict": verdict,
            "rayleigh_interval": rq.to_dict(),
            "vector": list(vector),
            "hermitian_residual_contains_zero": self.residual_contains_zero(),
            "hermitian_residual_exact_zero": self.residual_exact_zero(),
        }

    def to_dict(self) -> Dict[str, Any]:
        return {
            "n": self.n,
            "entries": [[entry.to_dict() for entry in row] for row in self.entries],
        }


def build_placeholder_matrix() -> IntervalMatrix:
    """
    Placeholder interval matrix.

    This is not the true arithmetic matrix.
    It is a skeleton matrix chosen to exercise certificate logic.
    """
    return IntervalMatrix(
        [
            [Interval(-2.01, -1.99), Interval(0.49, 0.51)],
            [Interval(0.49, 0.51), Interval(0.99, 1.01)],
        ]
    )


def write_placeholder_certificate(output_path: Path) -> None:
    matrix = build_placeholder_matrix()
    vector = [1.0, 0.0]
    certificate = {
        "phase": "12V",
        "status": "PLACEHOLDER_INTERVAL_MATRIX_CERTIFICATE",
        "important_boundary": "TRUE_ARITHMETIC_ENTRIES_NOT_YET_COMPUTED",
        "matrix": matrix.to_dict(),
        "negative_direction": matrix.negative_direction_certificate(vector),
        "audit_strings": [
            "INTERVAL_MATRIX_IMPLEMENTATION_COMPLETE",
            "REAL_INTERVAL_CLASS_IMPLEMENTED",
            "INTERVAL_MATRIX_CLASS_IMPLEMENTED",
            "HERMITIAN_RESIDUAL_INTERVAL_IMPLEMENTED",
            "RAYLEIGH_INTERVAL_IMPLEMENTED",
            "NEGATIVE_DIRECTION_CERTIFICATE_LOGIC_IMPLEMENTED",
            "PLACEHOLDER_ENTRIES_ONLY",
            "TRUE_ARITHMETIC_ENTRIES_NOT_YET_COMPUTED",
            "ARITHMETIC_ONLY_CERTIFICATE_NOT_YET_COMPLETE",
        ],
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(certificate, indent=2), encoding="utf-8")


if __name__ == "__main__":
    out = Path("original_results/finite_bombieri_stability/level4_candidate/interval_matrix_implementation/placeholder_interval_certificate.json")
    write_placeholder_certificate(out)
    print(f"Wrote {out}")
