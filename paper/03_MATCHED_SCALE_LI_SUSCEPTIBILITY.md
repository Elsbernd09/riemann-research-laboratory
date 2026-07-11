# 3. Matched-Scale Li Susceptibility

## 3.1 Definition

Define

\[
f_n(z)
=
1-
\left(
1-\frac1z
\right)^n.
\]

The Li susceptibility is

\[
\boxed{
\chi_n(\gamma)
=
2\Re
f_n''
\left(
\frac12+i\gamma
\right).
}
\]

The exact closed form is

\[
\chi_n(\gamma)
=
-
\frac{2n}
{
(\gamma^2+1/4)^2
}
\left[
n\cos(n\theta_\gamma)
+
2\gamma\sin(n\theta_\gamma)
\right],
\]

where

\[
\theta_\gamma
=
2\arctan
\left(
\frac1{2\gamma}
\right).
\]

---

## 3.2 Leading matched-scale profile

Let

\[
q=\frac n\gamma.
\]

Uniformly for \(q\) in compact positive sets,

\[
\boxed{
\gamma^2\chi_n(\gamma)
=
\Psi_{Li}(q)
+
O_K(\gamma^{-2}),
}
\]

where

\[
\boxed{
\Psi_{Li}(q)
=
-2q
\left(
q\cos q
+
2\sin q
\right).
}
\]

---

## 3.3 First derivative profile

Define

\[
\boxed{
J_{Li}(q)
=
2q^3\sin q
-
12q^2\cos q
-
12q\sin q.
}
\]

The repaired direct derivative argument gives

\[
\boxed{
\gamma^3\chi_n'(\gamma)
=
-J_{Li}(q)
+
O_K(\gamma^{-2}).
}
\]

This is obtained from the exact scaled analytic representation.

It is not obtained by differentiating a previously displayed big-O remainder.

---

## 3.4 Second derivative profile

Define

\[
\boxed{
K_{Li}^{(2)}(q)
=
3J_{Li}(q)
+
qJ_{Li}'(q).
}
\]

Since

\[
J_{Li}'(q)
=
2q^3\cos q
+
18q^2\sin q
-
36q\cos q
-
12\sin q,
\]

we obtain

\[
\boxed{
K_{Li}^{(2)}(q)
=
2q^4\cos q
+
24q^3\sin q
-
72q^2\cos q
-
48q\sin q.
}
\]

Uniformly for \(q\) in compact positive sets,

\[
\boxed{
\gamma^4\chi_n''(\gamma)
=
K_{Li}^{(2)}(q)
+
O_K(\gamma^{-2}).
}
\]

---

## 3.5 Relative-window derivative scale

Fix

\[
K=[c_-,c_+]
\Subset(0,\infty)
\]

and suppose

\[
n/H\in K.
\]

For

\[
t=Hu,
\qquad
1\le u\le1+\eta,
\]

the coordinate

\[
n/t
=
\frac{n/H}{u}
\]

lies in

\[
K_\eta
=
\left[
\frac{c_-}{1+\eta},
c_+
\right].
\]

Thus

\[
\chi_n(t)
=
O_{K,\eta}(H^{-2})
\]

and

\[
\chi_n''(t)
=
O_{K,\eta}(H^{-4})
\]

uniformly on the window.

Therefore

\[
\boxed{
|\chi_n(B)-\chi_n(H)|
=
O_{K,\eta}(H^{-2})
}
\]

and

\[
\boxed{
\int_H^B
|\chi_n''(t)|dt
=
O_{K,\eta}(H^{-3}).
}
\]

