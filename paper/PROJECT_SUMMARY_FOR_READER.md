# Project Summary for Reader

## One-sentence summary

This project proves an unconditional matched-scale response estimate showing that the interior zero-counting discrepancy response through the Li susceptibility kernel is lower order than the natural \(H^{-2}\) susceptibility scale.

## Main theorem

Let

\[
E(t)=N(t)-M(t),
\]

where \(N(t)\) is the classical nontrivial-zero counting function and \(M(t)\) is the main Riemann-von Mangoldt term.

Let

\[
\chi_n^{Li}(\gamma)
=
2\Re f_n''\left(\frac12+i\gamma\right),
\]

where

\[
f_n(z)
=
1-\left(1-\frac1z\right)^n.
\]

Define

\[
R_{\mathrm{int}}(n;H,\eta)
=
-\int_H^{(1+\eta)H}
E(t)\chi_n'(t)\,dt.
\]

Then, for fixed \(\eta>0\) and compact \(K\Subset(0,\infty)\),

\[
R_{\mathrm{int}}(n;H,\eta)
=
O_{K,\eta}
\left(
\frac{\log H}{H^3}
\right)
\]

uniformly when

\[
n/H\in K.
\]

Therefore

\[
H^2R_{\mathrm{int}}(n;H,\eta)\to0.
\]

## Why the theorem is true

The proof is short after the kernel estimates are known.

Classically,

\[
E(t)=S(t)+O(1/t)
\]

and

\[
S_1(t)=O(\log t).
\]

On a fixed relative window

\[
[H,(1+\eta)H],
\]

this gives

\[
\overline E
=
O_\eta\left(\frac{\log H}{H}\right)
\]

and

\[
\|F\|_\infty
=
O_\eta(\log H),
\]

where

\[
F(t)=\int_H^t(E(s)-\overline E)\,ds.
\]

The Li susceptibility satisfies

\[
|\chi_n(B)-\chi_n(H)|
=
O_{K,\eta}(H^{-2})
\]

and

\[
\int_H^B|\chi_n''(t)|dt
=
O_{K,\eta}(H^{-3}).
\]

The exact identity

\[
R_{\mathrm{int}}
=
-\overline E(\chi_n(B)-\chi_n(H))
+
\int_H^B F(t)\chi_n''(t)dt
\]

then gives

\[
R_{\mathrm{int}}
=
O_{K,\eta}
\left(
\frac{\log H}{H^3}
\right).
\]

## What is classical

The following are classical:

- Riemann-von Mangoldt zero counting;
- \(S(t)\) and \(S_1(t)\);
- \(S_1(t)=O(\log t)\);
- the RH-conditional \(S_1\) refinement;
- Li's criterion;
- the Guinand-Weil explicit formula;
- the relation between Li coefficients and Guinand-Weil;
- Weil's quadratic positivity criterion.

## What is project-specific

The project-specific part is the matched-scale response specialization using

\[
\chi_n^{Li}(\gamma)
=
2\Re f_n''\left(\frac12+i\gamma\right)
\]

and the centered-primitive transfer identity.

The key kernel profile is

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

## What the project does not claim

The project does not prove RH.

The project does not give a new Li criterion.

The project does not give a new Weil positivity criterion.

The project does not exclude off-critical zeros.

The project does not claim novelty.

Originality remains under active prior-art review.

