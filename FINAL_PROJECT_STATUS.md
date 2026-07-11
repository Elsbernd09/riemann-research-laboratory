# Final Project Status

## Project

Riemann Research Laboratory

## Current paper title

**Matched-Scale Li Susceptibility and Centered-Primitive Transfer of Zero-Counting Discrepancy**

## Current status

The project has reached a clean stopping point.

A coherent research manuscript exists.

A mentor review package exists.

The project is ready for serious mentor/professor review.

It is not ready for submission.

Originality remains under active prior-art review.

---

# Main theorem

The central theorem proves, unconditionally, that

\[
R_{\mathrm{int}}(n;H,\eta)
=
O_{K,\eta}
\left(
\frac{\log H}{H^3}
\right)
\]

uniformly for

\[
n/H\in K\Subset(0,\infty).
\]

Consequently,

\[
H^2R_{\mathrm{int}}(n;H,\eta)\to0.
\]

No assumption of the Riemann Hypothesis is used.

---

# RH refinement

Under RH, the same method gives

\[
R_{\mathrm{int}}(n;H,\eta)
=
O_{K,\eta}
\left(
\frac{\log H}
{H^3(\log\log H)^2}
\right).
\]

This is a refinement, not the source of the main theorem.

---

# What the project does not claim

The project does not prove RH.

The project does not make progress toward proving RH.

The project does not exclude off-critical zeros.

The project does not introduce a new Li criterion.

The project does not introduce a new Weil positivity criterion.

The project does not claim novelty.

The project does not treat numerical experiments as proof.

---

# Core paper files

Read these first:

- `paper/latex/main.tex`
- `paper/MENTOR_REVIEW_NOTE.md`
- `paper/PROJECT_SUMMARY_FOR_READER.md`
- `paper/WHAT_TO_REVIEW_FIRST.md`
- `paper/SUBMISSION_CHECKLIST.md`
- `paper/REFEREE_RESPONSE_DRAFT.md`

---

# Core proof dependencies

The main theorem depends on:

1. classical Riemann-von Mangoldt zero counting;
2. classical \(S_1(t)=O(\log t)\);
3. the matched-scale Li susceptibility profile;
4. the corrected second-derivative profile

\[
K_{\mathrm{Li}}^{(2)}(q)
=
2q^4\cos q
+
24q^3\sin q
-
72q^2\cos q
-
48q\sin q;
\]

5. the centered primitive

\[
F(t)=\int_H^t(E(s)-\overline E)ds;
\]

6. the exact transfer identity

\[
R_{\mathrm{int}}
=
-\overline E(\chi_n(B)-\chi_n(H))
+
\int_H^B F(t)\chi_n''(t)dt.
\]

---

# Important failed or abandoned branches

The project deliberately abandoned:

- reverse RH sensitivity through scalar \(N(T)\);
- naive Hardy/Parseval energy;
- broad positive horizontal-defect extraction;
- fixed linear Li-filter positivity;
- signed Weil-rank hunting;
- treating PCA as a theorem;
- claiming numerical experiments prove asymptotics.

These are recorded in the research ledger for honesty and audit history.

---

# Next serious step

Show the manuscript to a mathematically mature reader and ask them to review:

1. whether the \(S_1(t)=O(\log t)\) input is normalized correctly;
2. whether the ordinary integration-by-parts step is valid;
3. whether the matched-scale derivative hierarchy is correct;
4. whether the theorem is already known in another form;
5. whether the result should be framed as a short specialization rather than a major new theorem.

