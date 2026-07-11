# Phase 5V — Unconditional Global Li-Response Suppression

## Status

PROVED IN PROJECT — UNCONDITIONAL THEOREM.

## Objective

Upgrade the Phase 5O response-transfer analysis by using the classical unconditional bound for the first antiderivative of the zero-counting argument term.

The result is an unconditional asymptotic suppression theorem for the interior zero-counting discrepancy response of the matched-scale Li susceptibility kernel.

---

# 1. Global zero-counting discrepancy

Let

\[
N(t)
\]

denote the classical counting function for nontrivial zeros of the Riemann zeta function, counted with multiplicity and with any standard synchronized endpoint convention.

Define

\[
M(t)
=
\frac{t}{2\pi}
\log\frac{t}{2\pi}
-
\frac{t}{2\pi}
+
\frac78.
\]

Define the global discrepancy

\[
E(t)
=
N(t)-M(t).
\]

The classical Riemann-von Mangoldt decomposition gives

\[
E(t)
=
S(t)+r(t),
\]

where

\[
r(t)=O(1/t).
\]

Only ordinary integrals of \(E\) occur below.

Therefore changes to point values of \(N\) or \(S\) at individual zero ordinates do not affect the argument.

---

# 2. Classical unconditional antiderivative input

Let

\[
S_1(t)
=
C+\int_0^tS(u)\,du.
\]

Use the classical unconditional bound

\[
\boxed{
S_1(t)=O(\log t).
}
\]

Fix

\[
\eta>0
\]

and define

\[
B=(1+\eta)H.
\]

For

\[
t\in[H,B],
\]

we have

\[
\log t
=
O_\eta(\log H).
\]

Therefore

\[
\sup_{H\le t\le B}
|S_1(t)|
=
O_\eta(\log H).
\]

---

# 3. Window-mean discrepancy

Define

\[
\overline E
=
\frac1{B-H}
\int_H^B E(s)\,ds.
\]

Since

\[
E=S+r,
\]

we have

\[
\int_H^B E(s)\,ds
=
S_1(B)-S_1(H)
+
\int_H^B r(s)\,ds.
\]

The unconditional \(S_1\) bound gives

\[
S_1(B)-S_1(H)
=
O_\eta(\log H).
\]

Also,

\[
\int_H^B|r(s)|\,ds
=
O_\eta(1),
\]

because

\[
r(s)=O(1/s)
\]

and

\[
\int_H^{(1+\eta)H}\frac{ds}{s}
=
\log(1+\eta).
\]

Since

\[
B-H=\eta H,
\]

we obtain

\[
\boxed{
\overline E
=
O_\eta
\left(
\frac{\log H}{H}
\right).
}
\]

---

# 4. Centered primitive

Define

\[
F(t)
=
\int_H^t
\left(
E(s)-\overline E
\right)ds.
\]

Then

\[
F(H)=F(B)=0.
\]

Let

\[
A(t)
=
\int_{t_0}^tE(s)\,ds
\]

for a fixed positive \(t_0\).

The exact secant-detrending identity gives

\[
F(t)
=
A(t)-A(H)
-
\frac{t-H}{B-H}
\left(
A(B)-A(H)
\right).
\]

Using

\[
E=S+r,
\]

the function \(A\) differs from \(S_1\) by an integrated \(O(1/t)\) remainder and an additive constant.

The additive constant cancels under secant detrending.

On the fixed relative window,

\[
\sup_{H\le t\le B}
|S_1(t)|
=
O_\eta(\log H),
\]

and the integrated remainder increments are

\[
O_\eta(1).
\]

Therefore

\[
\boxed{
\|F\|_{\infty,[H,B]}
=
O_\eta(\log H).
}
\]

This estimate is unconditional.

---

# 5. Matched-scale Li susceptibility

Let

\[
\chi_n(t)
=
\chi_n^{Li}(t).
\]

Fix a compact interval

\[
K=[c_-,c_+]
\subset
(0,\infty).
\]

Assume

\[
\frac nH\in K.
\]

For

\[
t\in[H,(1+\eta)H],
\]

the coordinate

\[
q=\frac nt
\]

lies in the compact interval

\[
K_\eta
=
\left[
\frac{c_-}{1+\eta},
c_+
\right].
\]

The project matched-scale susceptibility expansion gives

\[
t^2\chi_n(t)
=
\Psi_{Li}(q)
+
O_{K_\eta}(t^{-2}).
\]

Therefore

\[
\boxed{
\chi_n(t)
=
O_{K,\eta}(H^{-2})
}
\]

uniformly on the window.

Consequently,

\[
\boxed{
|\chi_n(B)-\chi_n(H)|
=
O_{K,\eta}(H^{-2}).
}
\]

---

# 6. Corrected second-derivative asymptotic

The repaired direct derivative argument gives

\[
t^4\chi_n''(t)
=
K_{Li}^{(2)}(q)
+
O_{K_\eta}(t^{-2}),
\]

where

\[
q=\frac nt
\]

and

\[
K_{Li}^{(2)}(q)
=
2q^4\cos q
+
24q^3\sin q
-
72q^2\cos q
-
48q\sin q.
\]

Thus

\[
\chi_n''(t)
=
O_{K,\eta}(H^{-4})
\]

uniformly for

\[
t\in[H,B].
\]

Because

\[
B-H=\eta H,
\]

we obtain

\[
\boxed{
\int_H^B
|\chi_n''(t)|dt
=
O_{K,\eta}(H^{-3}).
}
\]

More precisely, along matched-scale sequences

\[
\frac nH\to c>0,
\]

\[
H^3
\int_H^{(1+\eta)H}
|\chi_n''(t)|dt
\to
\int_1^{1+\eta}
u^{-4}
\left|
K_{Li}^{(2)}
\left(
\frac cu
\right)
\right|du.
\]

---

# 7. Exact centered-primitive transfer identity

Define the global interior discrepancy response

\[
R_{\mathrm{int}}(n;H,\eta)
=
-
\int_H^B
E(t)\chi_n'(t)\,dt.
\]

The Phase 5N integration-by-parts identity gives

\[
\boxed{
R_{\mathrm{int}}
=
-\overline E
\left(
\chi_n(B)-\chi_n(H)
\right)
+
\int_H^B
F(t)\chi_n''(t)\,dt.
}
\]

Define

\[
R_{\mathrm{mean}}
=
-\overline E
\left(
\chi_n(B)-\chi_n(H)
\right)
\]

and

\[
R_{\mathrm{prim}}
=
\int_H^B
F(t)\chi_n''(t)\,dt.
\]

Then

\[
R_{\mathrm{int}}
=
R_{\mathrm{mean}}
+
R_{\mathrm{prim}}.
\]

---

# 8. Unconditional mean-channel bound

From the preceding estimates,

\[
\overline E
=
O_\eta
\left(
\frac{\log H}{H}
\right)
\]

and

\[
|\chi_n(B)-\chi_n(H)|
=
O_{K,\eta}(H^{-2}).
\]

Therefore

\[
\boxed{
R_{\mathrm{mean}}
=
O_{K,\eta}
\left(
\frac{\log H}{H^3}
\right).
}
\]

---

# 9. Unconditional primitive-channel bound

We have

\[
\|F\|_\infty
=
O_\eta(\log H)
\]

and

\[
\int_H^B
|\chi_n''(t)|dt
=
O_{K,\eta}(H^{-3}).
\]

Hence

\[
\begin{aligned}
|R_{\mathrm{prim}}|
&\le
\|F\|_\infty
\int_H^B
|\chi_n''(t)|dt
\\
&=
O_{K,\eta}
\left(
\frac{\log H}{H^3}
\right).
\end{aligned}
\]

Thus

\[
\boxed{
R_{\mathrm{prim}}
=
O_{K,\eta}
\left(
\frac{\log H}{H^3}
\right).
}
\]

---

# 10. Unconditional global response theorem

Combining the mean and primitive channels gives:

## Theorem

Fix

\[
\eta>0
\]

and a compact interval

\[
K\Subset(0,\infty).
\]

Let

\[
B=(1+\eta)H.
\]

Uniformly over positive integers \(n\) satisfying

\[
\frac nH\in K,
\]

the global Li susceptibility interior discrepancy response satisfies

\[
\boxed{
R_{\mathrm{int}}(n;H,\eta)
=
O_{K,\eta}
\left(
\frac{\log H}{H^3}
\right)
}
\]

as

\[
H\to\infty.
\]

No assumption of the Riemann Hypothesis is used.

Consequently,

\[
\boxed{
H^2R_{\mathrm{int}}(n;H,\eta)
=
O_{K,\eta}
\left(
\frac{\log H}{H}
\right)
\to0.
}
\]

Thus the global interior discrepancy-response channel is asymptotically lower order than the natural matched-scale Li susceptibility scale

\[
H^{-2}.
\]

---

# 11. Nondegenerate normalized-share consequence

Suppose along a matched-scale sequence

\[
\frac nH\in K
\]

and

\[
|\Psi_{Li}(n/H)|
\ge
\delta
>
0.
\]

The susceptibility expansion gives

\[
\chi_n(H)
=
H^{-2}
\Psi_{Li}(n/H)
+
O_K(H^{-4}).
\]

Therefore, for sufficiently large \(H\),

\[
|\chi_n(H)|
\gg_{K,\delta}
H^{-2}.
\]

For a nonzero atom coefficient of fixed magnitude, the atom channel has natural scale

\[
H^{-2}.
\]

Meanwhile,

\[
R_{\mathrm{int}}
=
O_{K,\eta}
\left(
\frac{\log H}{H^3}
\right)
=
o(H^{-2}).
\]

Therefore any normalized component share whose denominator contains a uniformly nondegenerate competing \(H^{-2}\) channel satisfies

\[
\boxed{
i_{\mathrm{int}}\to0.
}
\]

The nondegeneracy assumption is essential.

No claim is made on Li blind-scale paths where

\[
\Psi_{Li}=0
\]

or on other paths where all competing channels simultaneously degenerate.

---

# 12. RH-conditional sharpening

Under RH, the classical estimate

\[
S_1(t)
=
O
\left(
\frac{\log t}
{(\log\log t)^2}
\right)
\]

improves the preceding antiderivative bounds to

\[
\|F\|_\infty
=
O_\eta
\left(
\frac{\log H}
{(\log\log H)^2}
\right)
\]

and

\[
\overline E
=
O_\eta
\left(
\frac{\log H}
{H(\log\log H)^2}
\right).
\]

Therefore the unconditional theorem sharpens conditionally to

\[
\boxed{
\mathrm{RH}
\Longrightarrow
R_{\mathrm{int}}
=
O_{K,\eta}
\left(
\frac{\log H}
{H^3(\log\log H)^2}
\right).
}
\]

The conditional theorem is therefore a logarithmic refinement of the unconditional response suppression theorem.

---

# 13. Interpretation of the finite component-share geometry

Phases 5J through 5N found a finite-data component-share cloud concentrated near

\[
i=0,
\]

with a principal direction almost equal to atom-endpoint exchange.

The unconditional theorem gives an asymptotic analytic mechanism consistent with this geometry:

\[
R_{\mathrm{int}}
=
o(H^{-2}).
\]

The theorem does not prove that every finite-height simplex point lies near the edge.

It does not establish a universal rate for the normalized share on degenerate paths.

It does show that, on nondegenerate matched-scale sequences, the interior response is asymptotically suppressed relative to the natural Li susceptibility scale without assuming RH.

---

# 14. Prior-art boundary

The following inputs are classical:

1. the Riemann-von Mangoldt formula;

2. the decomposition

\[
E=S+O(1/t);
\]

3. the first antiderivative \(S_1\);

4. the unconditional bound

\[
S_1(t)=O(\log t);
\]

5. the sharper conditional \(S_1\) bound under RH;

6. integration by parts as an analytic mechanism.

The project-specific specialization combines these inputs with:

1. the Li zero-coordinate susceptibility;

2. its matched-scale profile hierarchy;

3. the corrected direct second-derivative profile;

4. the centered-primitive Li response decomposition.

No subsuming source identified in the current audit for the full exact specialization and stated matched-scale response theorem.

This is not a novelty claim.

Originality remains under active prior-art review.

---

# 15. RH consequence

The unconditional theorem does not prove RH.

Indeed, Phase 5P proves that the scalar zero-counting discrepancy architecture is horizontally blind.

The theorem is compatible with RH failure.

Its significance is response asymptotics, not an RH criterion.

