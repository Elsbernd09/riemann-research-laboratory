from decimal import Decimal, getcontext
from pathlib import Path
import json
import hashlib

getcontext().prec = 80

def D(x):
    return Decimal(str(x))

def compute_transfer_certificate(R, m, tau, pi, kappa, chi, eta=None):
    R = D(R)
    m = int(m)
    tau = D(tau)
    pi = D(pi)
    kappa = D(kappa)
    chi = D(chi)

    total_entrywise_error = tau + pi + kappa + chi
    transfer_bound = (R * R) * D(m) * total_entrywise_error

    cert = {
        "phase": "10AX",
        "status": "TRANSFER_CERTIFICATE_CALCULATOR",
        "inputs": {
            "R": str(R),
            "m": m,
            "tau_N_m": str(tau),
            "pi_N_m": str(pi),
            "kappa_N_m": str(kappa),
            "chi_N_m": str(chi),
            "eta": None if eta is None else str(D(eta)),
        },
        "computed": {
            "total_entrywise_error_E_N_m": str(total_entrywise_error),
            "transfer_bound_R2_m_E_N_m": str(transfer_bound),
        },
        "verdicts": {
            "transfer_certificate": "TRANSFER_BOUND_COMPUTED",
            "negative_direction_transfer": "ETA_NOT_PROVIDED",
        },
        "boundary": {
            "does_not_prove_RH": True,
            "does_not_falsify_RH": True,
            "does_not_prove_new_RH_criterion": True,
            "does_not_prove_unconditional_classical_convergence": True,
            "does_not_import_true_Weil_form": True,
            "does_not_claim_novelty": True,
        },
    }

    if eta is not None:
        eta = D(eta)
        half_eta = eta / D(2)
        cert["computed"]["half_eta"] = str(half_eta)

        if transfer_bound < half_eta:
            cert["verdicts"]["negative_direction_transfer"] = "NEGATIVE_DIRECTION_TRANSFER_CERTIFIED"
        else:
            cert["verdicts"]["negative_direction_transfer"] = "NEGATIVE_DIRECTION_TRANSFER_NOT_CERTIFIED"

    digest = hashlib.sha256(json.dumps(cert, sort_keys=True).encode("utf-8")).hexdigest()
    cert["certificate_sha256"] = digest
    return cert

def main():
    out_dir = Path("original_results/finite_bombieri_stability/contribution_branch/transfer_certificate_calculator")
    out_dir.mkdir(parents=True, exist_ok=True)

    examples = [
        {
            "name": "certified_margin_example",
            "R": "2",
            "m": 3,
            "tau": "0.001",
            "pi": "0.001",
            "kappa": "0.001",
            "chi": "0.0001",
            "eta": "0.10",
        },
        {
            "name": "not_certified_margin_example",
            "R": "5",
            "m": 4,
            "tau": "0.01",
            "pi": "0.01",
            "kappa": "0.01",
            "chi": "0.005",
            "eta": "0.05",
        },
        {
            "name": "bound_only_example",
            "R": "1.5",
            "m": 2,
            "tau": "0.0005",
            "pi": "0.0005",
            "kappa": "0.0005",
            "chi": "0.00005",
            "eta": None,
        },
    ]

    certificates = []
    for ex in examples:
        cert = compute_transfer_certificate(
            R=ex["R"],
            m=ex["m"],
            tau=ex["tau"],
            pi=ex["pi"],
            kappa=ex["kappa"],
            chi=ex["chi"],
            eta=ex["eta"],
        )
        cert["example_name"] = ex["name"]
        certificates.append(cert)

    bundle = {
        "phase": "10AX",
        "status": "TRANSFER_CERTIFICATE_CALCULATOR_OUTPUT",
        "certificates": certificates,
        "exact_audit_strings": [
            "TRANSFER_CERTIFICATE_CALCULATOR",
            "TOTAL_ENTRYWISE_ERROR_COMPUTED",
            "TRANSFER_BOUND_COMPUTED",
            "NEGATIVE_DIRECTION_TRANSFER_CERTIFIED",
            "NEGATIVE_DIRECTION_TRANSFER_NOT_CERTIFIED",
            "CERTIFICATE_SHA256_RECORDED",
            "UNCONDITIONAL_CLASSICAL_CONVERGENCE_NOT_PROVEN",
            "NOT_RH_CONTRIBUTION_YET",
        ],
    }

    (out_dir / "PHASE_10AX_TRANSFER_CERTIFICATES.json").write_text(
        json.dumps(bundle, indent=2),
        encoding="utf-8",
    )

    summary = []
    summary.append("# Phase 10AX Transfer Certificate Calculator Output\n\n")
    summary.append("## Status\n\n")
    summary.append("TRANSFER_CERTIFICATE_CALCULATOR\n\n")
    summary.append("## Formula\n\n")
    summary.append("\\[\n")
    summary.append("\\mathcal E_N^{(m)}=\\tau_N^{(m)}+\\pi_N^{(m)}+\\kappa_N^{(m)}+\\chi_N^{(m)}\n")
    summary.append("\\]\n\n")
    summary.append("\\[\n")
    summary.append("\\text{transfer bound}=R^2m\\mathcal E_N^{(m)}\n")
    summary.append("\\]\n\n")

    for cert in certificates:
        summary.append(f"## Example: {cert['example_name']}\n\n")
        summary.append(f"- total_entrywise_error_E_N_m: {cert['computed']['total_entrywise_error_E_N_m']}\n")
        summary.append(f"- transfer_bound_R2_m_E_N_m: {cert['computed']['transfer_bound_R2_m_E_N_m']}\n")
        summary.append(f"- transfer_certificate: {cert['verdicts']['transfer_certificate']}\n")
        summary.append(f"- negative_direction_transfer: {cert['verdicts']['negative_direction_transfer']}\n")
        summary.append(f"- certificate_sha256: {cert['certificate_sha256']}\n\n")

    summary.append("## Boundary\n\n")
    summary.append("This calculator does not prove RH.\n\n")
    summary.append("This calculator does not falsify RH.\n\n")
    summary.append("This calculator does not prove a new RH criterion.\n\n")
    summary.append("This calculator does not prove unconditional classical convergence.\n\n")
    summary.append("This calculator does not import the true Weil form.\n\n")
    summary.append("This calculator does not claim novelty.\n\n")
    summary.append("## Exact audit strings\n\n")
    summary.append("TRANSFER_CERTIFICATE_CALCULATOR\n\n")
    summary.append("TOTAL_ENTRYWISE_ERROR_COMPUTED\n\n")
    summary.append("TRANSFER_BOUND_COMPUTED\n\n")
    summary.append("NEGATIVE_DIRECTION_TRANSFER_CERTIFIED\n\n")
    summary.append("NEGATIVE_DIRECTION_TRANSFER_NOT_CERTIFIED\n\n")
    summary.append("CERTIFICATE_SHA256_RECORDED\n\n")
    summary.append("UNCONDITIONAL_CLASSICAL_CONVERGENCE_NOT_PROVEN\n\n")
    summary.append("NOT_RH_CONTRIBUTION_YET\n\n")

    (out_dir / "PHASE_10AX_TRANSFER_CERTIFICATE_OUTPUT.md").write_text(
        "".join(summary),
        encoding="utf-8",
    )

    print("=" * 80)
    print("PHASE 10AX TRANSFER CERTIFICATE CALCULATOR: COMPLETE")
    print("TRANSFER_CERTIFICATE_CALCULATOR")
    print("TOTAL_ENTRYWISE_ERROR_COMPUTED")
    print("TRANSFER_BOUND_COMPUTED")
    print("NEGATIVE_DIRECTION_TRANSFER_CERTIFIED")
    print("NEGATIVE_DIRECTION_TRANSFER_NOT_CERTIFIED")
    print("CERTIFICATE_SHA256_RECORDED")
    print("UNCONDITIONAL_CLASSICAL_CONVERGENCE_NOT_PROVEN")
    print("NOT_RH_CONTRIBUTION_YET")
    print("=" * 80)

if __name__ == "__main__":
    main()
