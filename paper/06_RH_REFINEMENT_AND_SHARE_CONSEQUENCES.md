# 6. RH Refinement and Normalized-Share Consequences

## 6.1 RH refinement

Assume RH.

The classical sharper bound

\[
S_1(t)
=
O
\left(
\frac{\log t}
{(\log\log t)^2}
\right)
\]

gives

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

The kernel bounds are unchanged.

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

The RH assumption sharpens the logarithmic factor.

It is not responsible for the base suppression phenomenon.

---

## 6.2 Abstract normalized-share consequence

Suppose a competing response channel satisfies

\[
|R_{\mathrm{comp}}|
\ge
cH^{-2}
\]

for some fixed

\[
c>0.
\]

Then

\[
\frac{|R_{\mathrm{int}}|}
{
|R_{\mathrm{comp}}|
+
|R_{\mathrm{int}}|
}
\le
\frac{
C\log H/H^3
}{
c/H^2
}.
\]

Thus

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

---

## 6.3 Atom-channel specialization

The Stieltjes atom channel is

\[
R_{\mathrm{atom}}
=
\chi_n(H)\Delta N(H).
\]

Suppose

\[
|\Psi_{Li}(n/H)|
\ge
\delta>0
\]

and

\[
\Delta N(H)
=
m_H
\ge
m_0>0.
\]

Then, for sufficiently large \(H\),

\[
|\chi_n(H)|
\ge
\frac{\delta}{2}H^{-2}.
\]

Hence

\[
|R_{\mathrm{atom}}|
\ge
\frac{m_0\delta}{2}
H^{-2}.
\]

Therefore the normalized interior share tends to zero.

The atom-existence hypothesis is essential.

Kernel nondegeneracy alone does not imply

\[
\Delta N(H)>0.
\]

