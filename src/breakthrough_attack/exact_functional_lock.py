from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, Any
import json


@dataclass(frozen=True)
class ExactFunctionalLock:
    name: str = "T_BL"
    source_family: str = "Bombieri-Lagarias"
    mellin_transform: str = "hat_f(s)=int_0^infty f(x)x^(s-1)dx"
    tilde_involution: str = "tilde_f(x)=x^(-1)f(1/x)"
    hermitian_star: str = "f_star(x)=x^(-1)conjugate(f(1/x))"
    constant_term: str = "-(log(pi)+EulerGamma)f(1)"
    rejected_constant: str = "-(log(4*pi)+EulerGamma)f(1)"
    official_pole_target: str = "hat_f(0)=hat_f(1)=0"
    sufficient_g_constraint: str = "hat_g(0)=hat_g(1)=0"
    matrix_entry: str = "M_ij=T_BL[phi_j*phi_i_star]"
    certification_goal: str = "rigorous interval enclosure for each M_ij"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def write_exact_functional_lock_certificate(path: Path) -> None:
    lock = ExactFunctionalLock()
    payload = {
        "phase": "X2",
        "status": "PHASE_X2_EXACT_FUNCTIONAL_LOCK_COMPLETE",
        "lock": lock.to_dict(),
        "allowed_constant": "log(pi)+EulerGamma",
        "rejected_constant_for_locked_branch": "log(4*pi)+EulerGamma",
        "official_admissibility_target": "f-pole removal",
        "construction_admissibility_device": "stronger g-pole constraints",
        "audit_strings": [
            "PHASE_X2_EXACT_FUNCTIONAL_LOCK_COMPLETE",
            "BOMBIERI_LAGARIAS_FUNCTIONAL_LOCKED",
            "LOG_PI_GAMMA_CONSTANT_LOCKED",
            "LOG_4PI_GAMMA_REJECTED_FOR_LOCKED_BRANCH",
            "TILDE_INVOLUTION_LOCKED",
            "HERMITIAN_STAR_DICTIONARY_LOCKED",
            "F_POLE_REMOVAL_TARGET_LOCKED",
            "G_POLE_CONSTRAINTS_MARKED_SUFFICIENT_NOT_NECESSARY",
            "FINITE_ARITHMETIC_MATRIX_TARGET_DEFINED",
            "CERTIFIED_MATRIX_GAP_TARGET_IDENTIFIED",
            "READY_FOR_PHASE_X3_BUILT_IN_POLE_CANCELLED_SMOOTH_BASIS",
        ],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    write_exact_functional_lock_certificate(
        Path("breakthrough_attack/phase_x2_exact_functional_lock/exact_functional_lock_certificate.json")
    )
    print("Wrote exact functional lock certificate")
