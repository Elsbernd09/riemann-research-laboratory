from pathlib import Path
import json

from src.breakthrough_attack.outward_rounding_interval_audit import (
    build_interval_audit_report,
    write_interval_audit_report,
)

files = [
    Path("breakthrough_attack/phase_x20_outward_rounding_and_interval_audit/PHASE_X20_OUTWARD_ROUNDING_AND_INTERVAL_AUDIT.md"),
    Path("breakthrough_attack/phase_x20_outward_rounding_and_interval_audit/INTERVAL_AUDIT_STATUS.md"),
    Path("breakthrough_attack/phase_x20_outward_rounding_and_interval_audit/NEXT_PHASE_X21_TWO_BY_TWO_MATRIX_CERTIFICATE_CANDIDATE.md"),
    Path("src/breakthrough_attack/outward_rounding_interval_audit.py"),
]

required = [
    "PHASE_X20_OUTWARD_ROUNDING_AND_INTERVAL_AUDIT_COMPLETE",
    "SOURCE_NORMALIZATION_PASS_PROVISIONAL",
    "FINITE_PRIME_CUTOFF_PASS_STRUCTURAL",
    "COEFFICIENT_SOLVE_PARTIAL_PASS",
    "INTERVAL_ARITHMETIC_PARTIAL_PASS",
    "CENTRAL_AND_TILDE_INTEGRALS_PARTIAL_PASS",
    "PRIME_SIDE_PARTIAL_PASS",
    "CONSTANT_TERM_PARTIAL_PASS",
    "ARCHIMEDEAN_TERM_PARTIAL_PASS",
    "FULL_M00_ASSEMBLED_BUT_NOT_FULLY_CERTIFIED",
    "NO_BREAKTHROUGH_YET",
    "READY_FOR_PHASE_X21_TWO_BY_TWO_MATRIX_CERTIFICATE_CANDIDATE",
    "Theorem X20.1",
    "Theorem X20.2",
    "This phase does not prove RH",
    "This phase does not prove a breakthrough",
    "This phase does not establish novelty",
    "This phase does not compute a fully certified arithmetic entry",
]

for path in files:
    if not path.exists():
        raise FileNotFoundError(path)
    text = path.read_text(encoding="utf-8")
    if "\x00" in text:
        raise ValueError(f"NUL byte found in {path}")

combined = "\n".join(path.read_text(encoding="utf-8") for path in files)
missing = [phrase for phrase in required if phrase.lower() not in combined.lower()]
if missing:
    raise RuntimeError("Missing required content: " + ", ".join(missing))

report = build_interval_audit_report()
assert report.overall_status == "PHASE_X20_OUTWARD_ROUNDING_AND_INTERVAL_AUDIT_COMPLETE"
assert report.breakthrough_status == "NO_BREAKTHROUGH_YET"
assert report.certified_arithmetic_entry is False
assert len(report.gates) >= 10
assert any(g.status == "ASSEMBLED_BUT_NOT_FULLY_CERTIFIED" for g in report.gates)
assert any("certified pointwise convolution" in g.blocker for g in report.gates)

out = Path("breakthrough_attack/phase_x20_outward_rounding_and_interval_audit/outward_rounding_interval_audit_report.json")
write_interval_audit_report(out)
saved = json.loads(out.read_text(encoding="utf-8"))
assert saved["status"] == "PHASE_X20_OUTWARD_ROUNDING_AND_INTERVAL_AUDIT_COMPLETE"
assert saved["report"]["breakthrough_status"] == "NO_BREAKTHROUGH_YET"
assert saved["report"]["certified_arithmetic_entry"] is False

print("=" * 80)
print("PHASE X20 OUTWARD ROUNDING AND INTERVAL AUDIT: PASS")
print("SOURCE NORMALIZATION: PASS PROVISIONAL")
print("FINITE PRIME CUTOFF: PASS STRUCTURAL")
print("COEFFICIENT SOLVE: PARTIAL PASS")
print("INTERVAL ARITHMETIC: PARTIAL PASS")
print("CENTRAL/TILDE/PRIME/CONSTANT/ARCHIMEDEAN: PARTIAL PASS")
print("FULL M00: ASSEMBLED BUT NOT FULLY CERTIFIED")
print("BREAKTHROUGH STATUS: NO BREAKTHROUGH YET")
print("NEXT: TWO-BY-TWO MATRIX CERTIFICATE CANDIDATE")
print("=" * 80)
