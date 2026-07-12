from pathlib import Path

ROOT = Path(".")
OUT = Path("original_results/finite_bombieri_stability/level4_candidate/quadratic_form_import")
OUT.mkdir(parents=True, exist_ok=True)

patterns = [
    "Q_W",
    "B_W",
    "quadratic form",
    "Hermitian form",
    "positive definite",
    "positive semidefinite",
    "Weil positivity",
    "positivity criterion",
    "RH iff",
    "Riemann hypothesis if and only if",
    "convolution",
    "autocorrelation",
    "F_g",
    "T[F",
    "T[f]",
    "Bombieri",
    "Weil",
]

hits = []
for path in ROOT.rglob("*"):
    if path.is_file() and path.suffix.lower() in {".md", ".txt", ".py", ".lean"}:
        try:
            text = path.read_text(encoding="utf-8")
        except Exception:
            continue

        normalized = text.lower().replace("\\", "")
        score = sum(1 for p in patterns if p.lower().replace("\\", "") in normalized)

        if score:
            snippets = []
            lines = text.splitlines()
            for idx, line in enumerate(lines, start=1):
                low = line.lower().replace("\\", "")
                if any(p.lower().replace("\\", "") in low for p in patterns):
                    start = max(1, idx - 3)
                    end = min(len(lines), idx + 3)
                    snippets.append(
                        {
                            "line": idx,
                            "excerpt": "\n".join(f"{j}: {lines[j-1]}" for j in range(start, end + 1)),
                        }
                    )
                    if len(snippets) >= 8:
                        break

            hits.append(
                {
                    "path": str(path),
                    "score": score,
                    "snippets": snippets,
                }
            )

hits.sort(key=lambda x: (-x["score"], x["path"]))

report = []
report.append("# Phase 12C Quadratic Form Source Scan Report\n\n")
report.append("## Purpose\n\n")
report.append("Search local project files for an exact imported Weil positivity quadratic form.\n\n")
report.append("## Search target\n\n")
report.append("\\[\nQ_W(g)=T[F_g]\n\\]\n\n")
report.append("or an equivalent source-grounded quadratic/Hermitian Weil positivity form.\n\n")
report.append("## Top hits\n\n")

for hit in hits[:30]:
    report.append(f"### {hit['path']}\n\n")
    report.append(f"score: {hit['score']}\n\n")
    for s in hit["snippets"]:
        report.append("```text\n")
        report.append(s["excerpt"])
        report.append("\n```\n\n")

if not hits:
    report.append("No relevant local source hits found.\n\n")

report.append("## Scan conclusion\n\n")
report.append("This scan identifies candidate local references, but does not by itself prove that the exact classical quadratic Weil positivity form has been imported.\n\n")
report.append("## Exact audit strings\n\n")
report.append("PHASE_12C_QUADRATIC_SOURCE_SCAN_COMPLETE\n\n")
report.append("LOCAL_QUADRATIC_FORM_SCAN_PERFORMED\n\n")

(OUT / "PHASE_12C_QUADRATIC_SOURCE_SCAN_REPORT.md").write_text("".join(report), encoding="utf-8")

print("=" * 80)
print("PHASE 12C QUADRATIC SOURCE SCAN COMPLETE")
print("LOCAL_QUADRATIC_FORM_SCAN_PERFORMED")
print(f"hits_found={len(hits)}")
print("=" * 80)
