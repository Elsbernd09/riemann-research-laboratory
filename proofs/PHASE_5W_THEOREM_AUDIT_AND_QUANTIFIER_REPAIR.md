# Phase 5W — Unconditional Li-Response Theorem Audit and Quantifier Repair

## Status

MAIN PHASE 5V THEOREM SURVIVES ADVERSARIAL AUDIT.

ONE NORMALIZED-SHARE CONSEQUENCE REQUIRES A QUANTIFIER REPAIR.

## Objective

Audit the Phase 5V unconditional global Li-response suppression theorem at the level of:

1. classical dependencies;
2. zero-counting conventions;
3. ordinary versus Stieltjes integration;
4. compact-uniform matched-scale estimates;
5. endpoint and atom hypotheses;
6. normalized-share conclusions;
7. current prior-art disposition.

---

# 1. Classical zero-counting convention

Let

\[
N(T)
\]

count the nontrivial zeros

\[
\rho=\beta+i\gamma
\]

with

\[
0<\gamma\le T,
\]

counted with multiplicity.

Define

\[
M(T)
=
\frac{T}{2\pi}
\log\frac{T}{2\pi e}
+
\frac78.
\]

Equivalently,

\[
M(T)
=
\frac{T}{2\pi}
\log\frac{T}{2\pi}
-
\frac{T}{2\pi}
+
\frac78.
\]

The classical Riemann-von Mangoldt formula gives

\[
N(T)
=
M(T)
+
S(T)
+
R(T),
\]

where

\[
R(T)=O(1/T).
\]

Thus, with

\[
E(T)=N(T)-M(T),
\]

we have

\[
\boxed{
E(T)=S(T)+R(T).
}
\]

Different standard choices for the value of \(S(T)\) at zero ordinates affect only point values.

The Phase 5V theorem uses ordinary integrals of \(E\).

Therefore changing values on the discrete set of zero ordinates does not affect the ordinary integral identities.

This convention-independence does not apply to Stieltjes atom terms.

---

# 2. Classical antiderivative input

Define

\[
S_1(T)
=
C+\int_0^T S(t)\,dt.
\]

The classical unconditional estimate is

\[
\boxed{
S_1(T)=O(\log T).
}
\]

Under the Riemann Hypothesis,

\[
\boxed{
S_1(T)
=
O
\left(
\frac{\log T}
{(\log\log T)^2}
\right).
}
\]

These are classical inputs.

They are not project results.

---

# 3. Fixed relative window

Fix

\[
\eta>0
\]

and set

\[
B=(1+\eta)H.
\]

Then

\[
B-H=\eta H.
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

The integrated Riemann-von Mangoldt remainder satisfies

\[
\int_H^B |R(t)|\,dt
=
O_\eta(1)
\]

because

\[
R(t)=O(1/t).
\]

---

# 4. Window-mean discrepancy audit

Define

\[
\overline E
=
\frac1{B-H}
\int_H^B E(t)\,dt.
\]

Using

\[
E=S+R,
\]

we obtain

\[
\int_H^B E(t)\,dt
=
S_1(B)-S_1(H)
+
O_\eta(1).
\]

Unconditionally,

\[
S_1(B)-S_1(H)
=
O_\eta(\log H).
\]

Therefore

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

The implied constant may depend on \(\eta\).

No RH assumption is used.

---

# 5. Centered primitive audit

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
\int_{t_0}^t E(s)\,ds.
\]

The exact secant identity is

\[
\boxed{
F(t)
=
A(t)-A(H)
-
\frac{t-H}{B-H}
\left(
A(B)-A(H)
\right).
}
\]

Since

\[
A(t)
=
S_1(t)
+
\int_{t_0}^t R(s)\,ds
+
C_0,
\]

the additive constant cancels.

On the fixed relative window,

\[
\sup_{H\le t\le B}
|S_1(t)|
=
O_\eta(\log H),
\]

while all integrated remainder increments are

\[
O_\eta(1).
\]

Hence

\[
\boxed{
\|F\|_{\infty,[H,B]}
=
O_\eta(\log H).
}
\]

No RH assumption is used.

---

# 6. Matched-scale compactness audit

Fix

\[
K=[c_-,c_+]
\Subset
(0,\infty).
\]

Suppose

\[
\frac nH\in K.
\]

For

\[
t=Hu,
\qquad
1\le u\le1+\eta,
\]

we have

\[
q=\frac nt
=
\frac{n/H}{u}.
\]

Therefore

\[
q
\in
K_\eta
:=
\left[
\frac{c_-}{1+\eta},
c_+
\right].
\]

The interval

\[
K_\eta
\]

is compact and contained in

\[
(0,\infty).
\]

Thus every compact-uniform matched-scale kernel estimate from the repaired derivative analysis may be applied uniformly across the full relative window.

---

# 7. Susceptibility endpoint scale

The matched-scale expansion is

\[
t^2\chi_n(t)
=
\Psi_{Li}(n/t)
+
O_{K_\eta}(t^{-2}).
\]

Since

\[
\Psi_{Li}
\]

is bounded on the compact interval

\[
K_\eta,
\]

we obtain

\[
\chi_n(t)
=
O_{K,\eta}(H^{-2})
\]

uniformly on

\[
[H,B].
\]

Hence

\[
\boxed{
|\chi_n(B)-\chi_n(H)|
=
O_{K,\eta}(H^{-2}).
}
\]

No subtraction asymptotic is needed.

The uniform pointwise bound is sufficient.

---

# 8. Second-derivative scale audit

The corrected direct second-derivative asymptotic is

\[
t^4\chi_n''(t)
=
K_{Li}^{(2)}(n/t)
+
O_{K_\eta}(t^{-2}),
\]

where

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

Compactness of

\[
K_\eta
\]

gives

\[
\chi_n''(t)
=
O_{K,\eta}(H^{-4})
\]

uniformly on the window.

Since the window length is

\[
\eta H,
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

This is the precise derivative scale needed by the centered-primitive transfer.

---

# 9. Exact transfer identity

Define

\[
R_{\mathrm{int}}(n;H,\eta)
=
-
\int_H^B
E(t)\chi_n'(t)\,dt.
\]

Write

\[
E(t)=\overline E+F'(t)
\]

almost everywhere.

Then

\[
\begin{aligned}
R_{\mathrm{int}}
&=
-\overline E
\int_H^B
\chi_n'(t)\,dt
-
\int_H^B
F'(t)\chi_n'(t)\,dt
\\
&=
-\overline E
\left(
\chi_n(B)-\chi_n(H)
\right)
+
\int_H^B
F(t)\chi_n''(t)\,dt,
\end{aligned}
\]

because

\[
F(H)=F(B)=0.
\]

Thus

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

The identity is an ordinary integration-by-parts identity.

No Stieltjes atom term appears in this identity.

---

# 10. Main unconditional theorem audit

The mean channel satisfies

\[
\left|
\overline E
\left(
\chi_n(B)-\chi_n(H)
\right)
\right|
=
O_\eta
\left(
\frac{\log H}{H}
\right)
O_{K,\eta}(H^{-2}).
\]

Therefore

\[
R_{\mathrm{mean}}
=
O_{K,\eta}
\left(
\frac{\log H}{H^3}
\right).
\]

For the primitive channel,

\[
\left|
\int_H^B
F(t)\chi_n''(t)\,dt
\right|
\le
\|F\|_\infty
\int_H^B
|\chi_n''(t)|dt.
\]

Hence

\[
R_{\mathrm{prim}}
=
O_\eta(\log H)
O_{K,\eta}(H^{-3})
=
O_{K,\eta}
\left(
\frac{\log H}{H^3}
\right).
\]

Combining the two channels gives

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

uniformly for positive integers \(n\) satisfying

\[
n/H\in K.
\]

The proof is unconditional.

Therefore

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

The main Phase 5V theorem survives the audit.

---

# 11. Atom-channel quantifier failure

The Phase 5V normalized-share discussion used the susceptibility nondegeneracy condition

\[
|\Psi_{Li}(n/H)|
\ge
\delta
>
0.
\]

This condition implies

\[
|\chi_n(H)|
\gg
H^{-2}.
\]

However, the Stieltjes atom component is

\[
R_{\mathrm{atom}}
=
\chi_n(H)\Delta N(H).
\]

The kernel lower bound alone does not imply

\[
|R_{\mathrm{atom}}|
\gg
H^{-2}.
\]

If

\[
H
\]

is not a zero ordinate, then

\[
\Delta N(H)=0
\]

and therefore

\[
R_{\mathrm{atom}}=0.
\]

Thus susceptibility nondegeneracy and atom existence are logically distinct hypotheses.

The original informal Phase 5V atom-share wording was overbroad.

---

# 12. Correct atom-share theorem

Suppose along a matched-scale sequence:

\[
\frac nH\in K,
\]

\[
|\Psi_{Li}(n/H)|
\ge
\delta
>
0,
\]

and

\[
\Delta N(H)
=
m_H
\ge
m_0
>
0.
\]

For the classical zero-counting function, \(m_H\) is the multiplicity of the zero ordinate at \(H\).

The susceptibility expansion gives, for sufficiently large \(H\),

\[
|\chi_n(H)|
\ge
\frac{\delta}{2}H^{-2}.
\]

Therefore

\[
|R_{\mathrm{atom}}|
=
m_H|\chi_n(H)|
\ge
\frac{m_0\delta}{2}H^{-2}.
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

Hence

\[
\boxed{
\frac{|R_{\mathrm{int}}|}
{
|R_{\mathrm{atom}}|
+
|R_{\mathrm{end}}|
+
|R_{\mathrm{int}}|
}
\to0.
}
\]

No lower bound on the endpoint channel is needed because the denominator is already bounded below by the atom channel.

This conclusion is unconditional.

---

# 13. Abstract competing-channel consequence

More generally, suppose a normalized response decomposition contains the interior channel

\[
R_{\mathrm{int}}
\]

and at least one competing channel

\[
R_{\mathrm{comp}}
\]

satisfying

\[
|R_{\mathrm{comp}}|
\ge
cH^{-2}
\]

for some fixed

\[
c>0
\]

along the sequence.

Then

\[
R_{\mathrm{int}}
=
O
\left(
\frac{\log H}{H^3}
\right)
\]

implies

\[
\boxed{
\frac{|R_{\mathrm{int}}|}
{
|R_{\mathrm{comp}}|
+
|R_{\mathrm{int}}|
}
=
O
\left(
\frac{\log H}{H}
\right)
\to0.
}
\]

This is the correct general normalized-share consequence.

The theorem requires a competing-channel lower bound.

Kernel nondegeneracy alone does not manufacture an atom.

---

# 14. RH-conditional refinement audit

Under RH,

\[
S_1(T)
=
O
\left(
\frac{\log T}
{(\log\log T)^2}
\right).
\]

Repeating the argument gives

\[
\overline E
=
O_\eta
\left(
\frac{\log H}
{H(\log\log H)^2}
\right)
\]

and

\[
\|F\|_\infty
=
O_\eta
\left(
\frac{\log H}
{(\log\log H)^2}
\right).
\]

Therefore

\[
\boxed{
R_{\mathrm{int}}
=
O_{K,\eta}
\left(
\frac{\log H}
{H^3(\log\log H)^2}
\right).
}
\]

The Phase 5O-A conditional result survives as a logarithmic sharpening.

---

# 15. Current prior-art disposition

The following are classical:

1. Riemann-von Mangoldt zero counting;
2. the argument term \(S(T)\);
3. the first primitive \(S_1(T)\);
4. the unconditional estimate \(S_1(T)=O(\log T)\);
5. the RH-conditional \(S_1\) estimate;
6. integration by parts;
7. the Li kernel and its Guinand-Weil explicit-formula embedding.

The current uploaded-corpus audit did not identify a source stating the exact combined theorem

\[
R_{\mathrm{int}}(n;H,\eta)
=
O_{K,\eta}
\left(
\frac{\log H}{H^3}
\right)
\]

for the matched-scale Li zero-coordinate susceptibility and centered zero-counting discrepancy response.

Required wording:

"No subsuming source identified in the current uploaded-corpus audit."

This is not a novelty claim.

A complete current-public-literature novelty determination is not made here.

---

# 16. Final audit disposition

Main Phase 5V theorem:

SURVIVES.

Uniformity in \(n/H\in K\):

SURVIVES.

Ordinary-integral convention handling:

SURVIVES.

RH-conditional sharpening:

SURVIVES.

Original Phase 5V informal atom-share inference from kernel nondegeneracy alone:

REJECTED AS OVERBROAD.

Corrected atom-share theorem with explicit atom multiplicity hypothesis:

PROVED.

Abstract competing-channel share theorem:

PROVED.

RH consequence:

NONE.

