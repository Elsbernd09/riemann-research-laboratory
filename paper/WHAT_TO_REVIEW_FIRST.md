# What to Review First

For a mathematically serious reviewer, read in this order:

## 1. Main theorem statement

File:

`paper/latex/main.tex`

Search for:

Unconditional global Li-response suppression

Check:

- Are the quantifiers correct?
- Is \(K\Subset(0,\infty)\) enough?
- Is the theorem clearly unconditional?

## 2. Kernel derivative hierarchy

Search for:

Second derivative profile

Check the formula:

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

This is the corrected profile.

The earlier incorrect version is intentionally excluded from the manuscript.

## 3. Centered primitive

Search for:

Centered discrepancy primitive

Check:

\[
F(t)
=
\int_H^t(E(s)-\overline E)ds.
\]

Confirm that:

\[
\|F\|_\infty=O_\eta(\log H)
\]

follows from classical \(S_1(t)=O(\log t)\).

## 4. Integration by parts

Search for:

ordinary absolutely-continuous

Check the identity:

\[
R_{\mathrm{int}}
=
-\overline E(\chi_n(B)-\chi_n(H))
+
\int_H^B F(t)\chi_n''(t)dt.
\]

The proof uses ordinary integration by parts, not Stieltjes integration.

## 5. Proof of main theorem

Search for:

Proof of the main theorem

Check the two bounds:

\[
R_{\mathrm{mean}}
=
O_{K,\eta}
\left(
\frac{\log H}{H^3}
\right)
\]

and

\[
R_{\mathrm{prim}}
=
O_{K,\eta}
\left(
\frac{\log H}{H^3}
\right).
\]

## 6. Scope restriction

Search for:

Horizontal blindness and scope

Check that the paper does not claim the theorem implies RH.

## 7. Prior-art boundary

Search for:

Relation to classical Li and Weil machinery

Check that the paper correctly treats Li, Guinand-Weil, and Weil positivity as classical prior art.

