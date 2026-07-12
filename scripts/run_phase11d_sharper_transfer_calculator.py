from decimal import Decimal, getcontext
from pathlib import Path
import json
import hashlib

getcontext().prec = 80

def D(x):
    return Decimal(str(x))

def compute_sharper_transfer_certificate(R, m, tau, pi, chi, eta=None):
    R = D(R)
    m = int(m)
    tau = D(tau)
    pi = D(pi)
    chi = D(chi)

    sharper_total_error = tau + pi + chi
    sharper_transfer_bound = (R * R) * D(m) * sharper_total_error

    cert = {
        "phase": "11D",
        "status": "SHARPER_TRANSFER_CERTIFICATE_CALCULATOR",
        "assumption": "KAPPA_ZERO_UNDER_EXTRACTED_KERNEL_ALIGNMENT",
        "inputs": {
            "R": str(R),
            "m": m,
            "tau_N_m": str(tau),
            "pi_N_m": str(pi),
            "chi_N_m": str(chi),
            "eta": None if eta is None else str(D(eta)),
        },
        "computed": {
            "sharper_total_error_tau_pi_chi": str(sharper_total_error),
            "sharper_transfer_bound_R2_m_tau_pi_chi": str(sharper_transfer_bound),
        },
        "verdicts": {
            "transfer_certificate": "SHARPER_TRANSFER_BOUND_COMPUTED",
            "negative_direction_transfer": "ETA_NOT_PROVIDED",
        },
        "boundary": {
            "does_not_prove_RH": True,
            "does_not_falsify_RH": True,
            "does_not_prove_new_RH_criterion": True,
            "does_not_prove_full_classical_validation": True,
            "does_not_prove_unconditional_classical_convergence": True,
            "does_not_claim_novelty": True,
        },
    }

    if eta is not None:
        eta = D(eta)
        half_eta = eta / D(2)
        cert["computed"]["half_eta"] = str(half_eta)

        if sharper_transfer_bound < half_eta:
            cert["verdicts"]["negative_direction_transfer"] = "SHARPER_NEGATIVE_DIRECTION_TRANSFER_CERTIFIED"
        else:
            cert["verdicts"]["negative_direction_transfer"] = "SHARPER_NEGATIVE_DIRECTION_TRANSFER_NOT_CERTIFIED"

    digest = hashlib.sha256(json.dumps(cert, sort_keys=True).encode("utf-8")).hexdigest()
    cert["certificate_sha256"] = digest
    return cert

def main():
    out_dir = Path("original_results/finite_bombieri_stability/breakthrough_attempt/sharper_calculator")
    out_dir.mkdir(parents=True, exist_ok=True)

    examples = [
        {
            "name": "sharper_certified_margin_example",
            "R": "2",
            "m": 3,
            "tau": "0.001",
            "pi": "0.001",
            "chi": "0.0001",
            "eta": "0.06",
        },
        {
            "name": "sharper_not_certified_margin_example",
            "R": "5",
            "m": 4,
            "tau": "0.01",
            "pi": "0.01",
            "chi": "0.005",
            "eta": "0.05",
        },
        {
            "name": "sharper_bound_only_example",
            "R": "1.5",
            "m": 2,
            "tau": "0.0005",
            "pi": "0.0005",
            "chi": "0.00005",
            "eta": None,
        },
    ]

    certificates = []
    for ex in examples:
        cert = compute_sharper_transfer_certificate(
            R=ex["R"],
            m=ex["m"],
            tau=ex["tau"],
            pi=ex["pi"],
            chi=ex["chi"],
            eta=ex["eta"],
        )
        cert["example_name"] = ex["name"]
        certificates.append(cert)

    bundle = {
        "phase": "11D",
        "status": "SHARPER_TRANSFER_CERTIFICATE_CALCULATOR_OUTPUT",
        "assumption": "KAPPA_ZERO_UNDER_EXTRACTED_KERNEL_ALIGNMENT",
        "certificates": certificates,
        "exact_audit_strings": [
            "SHARPER_TRANSFER_CERTIFICATE_CALCULATOR",
            "KAPPA_ZERO_UNDER_EXTRACTED_KERNEL_ALIGNMENT",
            "SHARPER_TOTAL_ERROR_COMPUTED",
            "SHARPER_TRANSFER_BOUND_COMPUTED",
            "SHARPER_NEGATIVE_DIRECTION_TRANSFER_CERTIFIED",
            "SHARPER_NEGATIVE_DIRECTION_TRANSFER_NOT_CERTIFIED",
            "CERTIFICATE_SHA256_RECORDED",
            "FULL_CLASSICAL_VALIDATION_NOT_PROVEN",
            "NOT_RH_CONTRIBUTION_YET",
        ],
    }

    (out_dir / "PHASE_11D_SHARPER_TRANSFER_CERTIFICATES.json").write_text(
        json.dumps(bundle, indent=2),
        encoding="utf-8",
    )

    summary = []
    summary.append("# Phase 11D Sharper Transfer Certificate Calculator Output\n\n")
    summary.append("## Status\n\n")
    summary.append("SHARPER_TRANSFER_CERTIFICATE_CALCULATOR\n\n")
    summary.append("## Assumption\n\n")
    summary.append("KAPPA_ZERO_UNDER_EXTRACTED_KERNEL_ALIGNMENT\n\n")
    summary.append("## Formula\n\n")
    summary.append("\\[\n")
    summary.append("\\mathcal E_{sharp,N}^{(m)}=\\tau_N^{(m)}+\\pi_N^{(m)}+\\chi_N^{(m)}\n")
    summary.append("\\]\n\n")
    summary.append("\\[\n")
    summary.append("\\text{sharper transfer bound}=R^2m\\mathcal E_{sharp,N}^{(m)}\n")
    summary.append("\\]\n\n")

    for cert in certificates:
        summary.append(f"## Example: {cert['example_name']}\n\n")
        summary.append(f"- sharper_total_error_tau_pi_chi: {cert['computed']['sharper_total_error_tau_pi_chi']}\n")
        summary.append(f"- sharper_transfer_bound_R2_m_tau_pi_chi: {cert['computed']['sharper_transfer_bound_R2_m_tau_pi_chi']}\n")
        summary.append(f"- transfer_certificate: {cert['verdicts']['transfer_certificate']}\n")
        summary.append(f"- negative_direction_transfer: {cert['verdicts']['negative_direction_transfer']}\n")
        summary.append(f"- certificate_sha256: {cert['certificate_sha256']}\n\n")

    summary.append("## Boundary\n\n")
    summary.append("This calculator does not prove RH.\n\n")
    summary.append("This calculator does not falsify RH.\n\n")
    summary.append("This calculator does not prove a new RH criterion.\n\n")
    summary.append("This calculator does not prove full classical validation.\n\n")
    summary.append("This calculator does not prove unconditional classical convergence.\n\n")
    summary.append("This calculator does not claim novelty.\n\n")
    summary.append("## Exact audit strings\n\n")
    summary.append("SHARPER_TRANSFER_CERTIFICATE_CALCULATOR\n\n")
    summary.append("KAPPA_ZERO_UNDER_EXTRACTED_KERNEL_ALIGNMENT\n\n")
    summary.append("SHARPER_TOTAL_ERROR_COMPUTED\n\n")
    summary.append("SHARPER_TRANSFER_BOUND_COMPUTED\n\n")
    summary.append("SHARPER_NEGATIVE_DIRECTION_TRANSFER_CERTIFIED\n\n")
    summary.append("SHARPER_NEGATIVE_DIRECTION_TRANSFER_NOT_CERTIFIED\n\n")
    summary.append("CERTIFICATE_SHA256_RECORDED\n\n")
    summary.append("FULL_CLASSICAL_VALIDATION_NOT_PROVEN\n\n")
    summary.append("NOT_RH_CONTRIBUTION_YET\n\n")

    (out_dir / "PHASE_11D_SHARPER_TRANSFER_CALCULATOR_OUTPUT.md").write_text(
        "".join(summary),
        encoding="utf-8",
    )

    print("=" * 80)
    print("PHASE 11D SHARPER TRANSFER CERTIFICATE CALCULATOR: COMPLETE")
    print("SHARPER_TRANSFER_CERTIFICATE_CALCULATOR")
    print("KAPPA_ZERO_UNDER_EXTRACTED_KERNEL_ALIGNMENT")
    print("SHARPER_TOTAL_ERROR_COMPUTED")
    print("SHARPER_TRANSFER_BOUND_COMPUTED")
    print("SHARPER_NEGATIVE_DIRECTION_TRANSFER_CERTIFIED")
    print("SHARPER_NEGATIVE_DIRECTION_TRANSFER_NOT_CERTIFIED")
    print("CERTIFICATE_SHA256_RECORDED")
    print("FULL_CLASSICAL_VALIDATION_NOT_PROVEN")
    print("NOT_RH_CONTRIBUTION_YET")
    print("=" * 80)

if __name__ == "__main__":
    main()
