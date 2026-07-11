# Submission Checklist

## Paper

Working title:

**Matched-Scale Li Susceptibility and Centered-Primitive Transfer of Zero-Counting Discrepancy**

Current status:

Research draft.

Not submitted.

Originality remains under active prior-art review.

---

## Main theorem

The paper proves the unconditional estimate

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

No assumption of the Riemann Hypothesis is used.

---

## RH refinement

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

This is a refinement, not the source of the main suppression mechanism.

---

## What the paper is

This paper is a matched-scale response-transfer theorem for the Li zero-coordinate susceptibility.

It combines:

1. classical \(S_1\)-control of the zero-counting argument term;
2. the project Li susceptibility derivative hierarchy;
3. a centered zero-counting discrepancy primitive;
4. an exact ordinary integration-by-parts transfer identity.

---

## What the paper is not

This paper is not a proof of RH.

It is not a new Li criterion.

It is not a new Weil positivity criterion.

It is not a claim that RH is nearly solved.

It is not a claim that off-critical zeros are excluded.

It is not a numerical proof.

It is not a novelty-certified publication.

---

## Classical dependencies to cite carefully

- Riemann-von Mangoldt zero counting formula.
- Classical \(S(t)\) and \(S_1(t)\) theory.
- Unconditional bound \(S_1(T)=O(\log T)\).
- RH-conditional bound \(S_1(T)=O(\log T/(\log\log T)^2)\).
- Li criterion and Li coefficients.
- Guinand-Weil explicit formula.
- Bombieri-Lagarias connection between Li coefficients and Guinand-Weil.
- Weil quadratic functional and Bombieri's analysis.

---

## Project-specific dependencies

- Exact Li susceptibility formula.
- Matched-scale profile \(\Psi_{\mathrm{Li}}\).
- First derivative profile \(J_{\mathrm{Li}}\).
- Corrected second derivative profile

\[
K_{\mathrm{Li}}^{(2)}(q)
=
2q^4\cos q
+
24q^3\sin q
-
72q^2\cos q
-
48q\sin q.
\]

- Relative-window bound

\[
\int_H^{(1+\eta)H}
|\chi_n''(t)|dt
=
O_{K,\eta}(H^{-3}).
\]

- Centered primitive \(F\).
- Exact transfer identity

\[
R_{\mathrm{int}}
=
-\overline E
\left(
\chi_n(B)-\chi_n(H)
\right)
+
\int_H^B
F(t)\chi_n''(t)dt.
\]

---

## Before sharing with a professor

Check:

- [ ] Every theorem has precise quantifiers.
- [ ] Every \(O\)-constant dependency is stated.
- [ ] The \(n/H\in K\Subset(0,\infty)\) condition is repeated wherever needed.
- [ ] No statement implies uniformity near \(n/H=0\).
- [ ] The corrected \(K_{\mathrm{Li}}^{(2)}\) profile appears everywhere.
- [ ] The failed original \(K_2\) profile does not appear in the manuscript.
- [ ] The integration-by-parts step explicitly uses absolutely continuous \(F\).
- [ ] Ordinary integrals are distinguished from Stieltjes atom terms.
- [ ] Atom-share conclusions include the explicit jump hypothesis \(\Delta N(H)>0\).
- [ ] Numerical results are labeled motivation/validation only.
- [ ] No RH-progress language appears.
- [ ] No novelty claim appears.

---

## Current recommendation

Do not submit anywhere yet.

First show the manuscript to a mathematically mature reader and ask them specifically:

1. Is the \(S_1\)-based centered-primitive bound stated correctly?
2. Is the integration-by-parts step valid with the staircase zero-counting function?
3. Is the matched-scale second derivative profile correct?
4. Is the theorem more than a straightforward corollary once the kernel estimate is known?
5. Is there known literature already containing this exact specialization?

