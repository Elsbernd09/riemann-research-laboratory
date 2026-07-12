from pathlib import Path

base = Path("breakthrough_push/phase_b5_primary_paper_extraction")

files = [
    base / "PHASE_B5_PRIMARY_PAPER_EXTRACTION_PACK.md",
    base / "templates/EXTRACTION_TEMPLATE.md",
    base / "extractions/WEIL_EXTRACTION.md",
    base / "extractions/BOMBIERI_LAGARIAS_EXTRACTION.md",
    base / "extractions/CONNES_EXTRACTION.md",
    base / "extractions/FINITE_GALERKIN_EXTRACTION.md",
    base / "extractions/SUZUKI_EXTRACTION.md",
    base / "extractions/BURNOL_YOSHIDA_EXTRACTION.md",
    base / "PRIMARY_EXTRACTION_STATUS.md",
    base / "NEXT_PHASE_B6_BOMBIERI_LAGARIAS_EXTRACTION.md",
]

required = [
    "PHASE_B5_PRIMARY_PAPER_EXTRACTION_PACK_COMPLETE",
    "PRIMARY_EXTRACTION_FRAMEWORK_CREATED",
    "WEIL_EXTRACTION_TEMPLATE_CREATED",
    "BOMBIERI_LAGARIAS_EXTRACTION_TEMPLATE_CREATED",
    "CONNES_EXTRACTION_TEMPLATE_CREATED",
    "FINITE_GALERKIN_EXTRACTION_TEMPLATE_CREATED",
    "SUZUKI_EXTRACTION_TEMPLATE_CREATED",
    "BURNOL_YOSHIDA_EXTRACTION_TEMPLATE_CREATED",
    "BREAKTHROUGH_NOT_ACHIEVED",
    "READY_FOR_PHASE_B6_BOMBIERI_LAGARIAS_EXTRACTION",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a breakthrough",
    "This phase does not prove novelty",
    "This phase does not complete the literature review",
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

print("=" * 80)
print("PHASE B5 PRIMARY PAPER EXTRACTION PACK AUDIT: PASS")
print("PRIMARY EXTRACTION FRAMEWORK: CREATED")
print("WEIL TEMPLATE: CREATED")
print("BOMBIERI-LAGARIAS TEMPLATE: CREATED")
print("CONNES TEMPLATE: CREATED")
print("FINITE GALERKIN TEMPLATE: CREATED")
print("SUZUKI TEMPLATE: CREATED")
print("BURNOL/YOSHIDA TEMPLATE: CREATED")
print("BREAKTHROUGH: NOT ACHIEVED")
print("READY FOR B6: BOMBIERI-LAGARIAS EXTRACTION")
print("=" * 80)
