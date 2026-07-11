# 5. Proof of the Main Theorem

## 5.1 Mean channel

We have

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

## 5.2 Primitive channel

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

## 5.3 Conclusion

Since

\[
R_{\mathrm{int}}
=
R_{\mathrm{mean}}
+
R_{\mathrm{prim}},
\]

we obtain

\[
\boxed{
R_{\mathrm{int}}(n;H,\eta)
=
O_{K,\eta}
\left(
\frac{\log H}{H^3}
\right).
}
\]

Multiplying by \(H^2\),

\[
H^2R_{\mathrm{int}}
=
O_{K,\eta}
\left(
\frac{\log H}{H}
\right).
\]

Therefore

\[
\boxed{
H^2R_{\mathrm{int}}\to0.
}
\]

This completes the proof of Theorem A.

No assumption of RH has been used.

