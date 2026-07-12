from pathlib import Path
import re

ROOT = Path(".")
OUT = Path("original_results/finite_bombieri_stability/level4_candidate/true_weil_form_import")
OUT.mkdir(parents=True, exist_ok=True)

patterns = [
    "T[f]",
    "T[f^*]",
    "sum_\\rho",
    "sum\\_rho",
    "Bombieri",
    "Weil",
    "explicit formula",
    "f^*(x)",
    "Mellin",
    "quadratic form",
    "positivity",
]

hits = []
for path in ROOT.rglob("*"):
    if path.is_file() and path.suffix.lower() in {".md", ".txt", ".py", ".lean"}:
        try:
            text = path.read_text(encoding="utf-8")
        except Exception:
            continue
        lowered = text.lower()
        score = sum(1 for p in patterns if p.lower().replace("\\", "") in lowered.replace("\\", ""))
        if score:
            snippets = []
            lines = text.splitlines()
            for idx, line in enumerate(lines, start=1):
                low = line.lower()
                if any(p.lower().replace("\\", "") in low.replace("\\", "") for p in patterns):
                    start = max(1, idx - 2)
                    end = min(len(lines), idx + 2)
                    snippets.append({
                        "line": idx,
                        "excerpt": "\n".join(f"{j}: {lines[j-1]}" for j in range(start, end + 1))
                    })
                    if len(snippets) >= 5:
                        break
            hits.append({
                "path": str(path),
                "score": score,
                "snippets": snippets,
            })

hits.sort(key=lambda x: (-x["score"], x["path"]))

report = []
report.append("# Phase 12B Source Scan Report\n\n")
report.append("## Purpose\n\n")
report.append("Search local project files for previously extracted Bombieri/Weil source objects.\n\n")
report.append("## Top hits\n\n")

for hit in hits[:20]:
    report.append(f"### {hit['path']}\n\n")
    report.append(f"score: {hit['score']}\n\n")
    for s in hit["snippets"]:
        report.append("```text\n")
        report.append(s["excerpt"])
        report.append("\n```\n\n")

if not hits:
    report.append("No relevant local source hits found.\n\n")

report.append("## Exact audit strings\n\n")
report.append("PHASE_12B_SOURCE_SCAN_COMPLETE\n\n")
report.append("LOCAL_SOURCE_SCAN_PERFORMED\n\n")

(OUT / "PHASE_12B_SOURCE_SCAN_REPORT.md").write_text("".join(report), encoding="utf-8")

print("=" * 80)
print("PHASE 12B SOURCE SCAN COMPLETE")
print("LOCAL_SOURCE_SCAN_PERFORMED")
print(f"hits_found={len(hits)}")
print("=" * 80)
