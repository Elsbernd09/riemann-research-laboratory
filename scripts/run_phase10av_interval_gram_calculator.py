from decimal import Decimal, getcontext
from pathlib import Path
import json
import hashlib

getcontext().prec = 80

class Interval:
    def __init__(self, lower, upper):
        self.lower = Decimal(str(lower))
        self.upper = Decimal(str(upper))
        if self.lower > self.upper:
            raise ValueError("interval lower bound exceeds upper bound")

    @staticmethod
    def point(x):
        x = Decimal(str(x))
        return Interval(x, x)

    def midpoint(self):
        return (self.lower + self.upper) / Decimal(2)

    def radius(self):
        return (self.upper - self.lower) / Decimal(2)

    def __add__(self, other):
        return Interval(self.lower + other.lower, self.upper + other.upper)

    def __sub__(self, other):
        return Interval(self.lower - other.upper, self.upper - other.lower)

    def __mul__(self, other):
        products = [
            self.lower * other.lower,
            self.lower * other.upper,
            self.upper * other.lower,
            self.upper * other.upper,
        ]
        return Interval(min(products), max(products))

    def to_dict(self):
        return {
            "lower": str(self.lower),
            "upper": str(self.upper),
            "midpoint": str(self.midpoint()),
            "radius": str(self.radius()),
        }

def interval_dot(row, col):
    total = Interval.point(0)
    for a, b in zip(row, col):
        total = total + (a * b)
    return total

def build_toy_interval_gram_matrix():
    """
    Toy interval Gram calculator.

    Important boundary:
    This does NOT compute the true classical Weil/Bombieri Gram matrix.
    It only demonstrates the certified interval structure:
    lower, upper, midpoint, radius, and chi_N_m.
    """
    basis_vectors = [
        [Interval("0.9999999999", "1.0000000001"), Interval("0.1999999999", "0.2000000001")],
        [Interval("0.1999999999", "0.2000000001"), Interval("0.4999999999", "0.5000000001")],
        [Interval("-0.1000000001", "-0.0999999999"), Interval("0.2999999999", "0.3000000001")],
    ]

    m = len(basis_vectors)
    gram = []

    for i in range(m):
        row = []
        for j in range(m):
            entry = interval_dot(basis_vectors[i], basis_vectors[j])
            row.append(entry)
        gram.append(row)

    return gram

def certificate_for_gram(gram):
    radii = []
    entries = []

    for i, row in enumerate(gram):
        entry_row = []
        for j, interval in enumerate(row):
            radii.append(interval.radius())
            entry_row.append({
                "i": i,
                "j": j,
                **interval.to_dict()
            })
        entries.append(entry_row)

    chi = max(radii) if radii else Decimal(0)
    m = len(gram)
    matrix_level_bound = Decimal(m) * chi

    cert = {
        "phase": "10AV",
        "status": "INTERVAL_GRAM_ENTRY_CALCULATOR_PROTOTYPE",
        "boundary": {
            "does_not_compute_true_weil_gram_matrix": True,
            "does_not_prove_RH": True,
            "does_not_claim_novelty": True,
        },
        "m": m,
        "chi_N_m": str(chi),
        "matrix_level_bound_m_chi_N_m": str(matrix_level_bound),
        "entries": entries,
    }

    digest = hashlib.sha256(json.dumps(cert, sort_keys=True).encode("utf-8")).hexdigest()
    cert["certificate_sha256"] = digest
    return cert

def main():
    out_dir = Path("original_results/finite_bombieri_stability/contribution_branch/interval_calculator")
    out_dir.mkdir(parents=True, exist_ok=True)

    gram = build_toy_interval_gram_matrix()
    cert = certificate_for_gram(gram)

    (out_dir / "PHASE_10AV_INTERVAL_GRAM_CERTIFICATE.json").write_text(
        json.dumps(cert, indent=2),
        encoding="utf-8"
    )

    summary = []
    summary.append("# Phase 10AV Interval Gram-Entry Calculator Output\n")
    summary.append("## Status\n")
    summary.append("INTERVAL_GRAM_ENTRY_CALCULATOR_PROTOTYPE\n")
    summary.append("\n## Boundary\n")
    summary.append("This prototype does not compute the true classical Weil/Bombieri Gram matrix.\n")
    summary.append("This prototype does not prove RH.\n")
    summary.append("This prototype does not claim novelty.\n")
    summary.append("\n## Certificate\n")
    summary.append(f"- m: {cert['m']}\n")
    summary.append(f"- chi_N_m: {cert['chi_N_m']}\n")
    summary.append(f"- matrix_level_bound_m_chi_N_m: {cert['matrix_level_bound_m_chi_N_m']}\n")
    summary.append(f"- certificate_sha256: {cert['certificate_sha256']}\n")
    summary.append("\n## Exact audit strings\n")
    summary.append("INTERVAL_GRAM_ENTRY_CALCULATOR_PROTOTYPE\n")
    summary.append("CHI_N_M_COMPUTED\n")
    summary.append("MATRIX_LEVEL_BOUND_COMPUTED\n")
    summary.append("CERTIFICATE_SHA256_RECORDED\n")
    summary.append("TRUE_WEIL_GRAM_NOT_COMPUTED\n")
    summary.append("NOT_RH_CONTRIBUTION_YET\n")

    (out_dir / "PHASE_10AV_INTERVAL_GRAM_CALCULATOR_OUTPUT.md").write_text(
        "".join(summary),
        encoding="utf-8"
    )

    print("=" * 80)
    print("PHASE 10AV INTERVAL GRAM CALCULATOR: COMPLETE")
    print("INTERVAL_GRAM_ENTRY_CALCULATOR_PROTOTYPE")
    print("CHI_N_M_COMPUTED:", cert["chi_N_m"])
    print("MATRIX_LEVEL_BOUND_COMPUTED:", cert["matrix_level_bound_m_chi_N_m"])
    print("CERTIFICATE_SHA256_RECORDED:", cert["certificate_sha256"])
    print("TRUE_WEIL_GRAM_NOT_COMPUTED")
    print("NOT_RH_CONTRIBUTION_YET")
    print("=" * 80)

if __name__ == "__main__":
    main()
