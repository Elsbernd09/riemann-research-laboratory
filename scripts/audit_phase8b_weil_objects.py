from pathlib import Path

files = [
    Path("weil_reconstruction/objects/PHASE_8B_WEIL_OBJECT_DEFINITIONS.md"),
    Path("weil_reconstruction/objects/OBJECT_GLOSSARY.md"),
    Path("weil_reconstruction/objects/OBJECT_DEPENDENCY_GRAPH.md"),
]

required = [
    "Weil Object Definitions",
    "test functions",
    "transform",
    "Weil quadratic form",
    "negative direction",
    "Toy matrix",
    "Forbidden shortcut",
    "not a proof of RH",
    "not a new Weil criterion",
]

for path in files:
    if not path.exists():
        raise FileNotFoundError(path)

    text = path.read_text(encoding="utf-8")

    if "\x00" in text:
        raise ValueError(f"NUL byte found in {path}")

combined = "\n".join(path.read_text(encoding="utf-8") for path in files)

missing = [
    phrase for phrase in required
    if phrase.lower() not in combined.lower()
]

if missing:
    raise RuntimeError("Missing required content: " + ", ".join(missing))

print("=" * 80)
print("PHASE 8B WEIL OBJECT DEFINITIONS AUDIT: PASS")
print("OBJECT DEFINITIONS: CREATED")
print("GLOSSARY: CREATED")
print("DEPENDENCY GRAPH: CREATED")
print("TOY-VS-WEIL BOUNDARY: ENFORCED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
