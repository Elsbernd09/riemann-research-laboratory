# Exact Li-Kernel Susceptibility Derivation

## Phase 1A

This document derives the signed quadratic susceptibility of the individual Li zero kernel.

---

# 1. Kernel

For integer \(n\ge1\), define

\[
f_n(z)
=
1-
\left(
1-\frac1z
\right)^n,
\qquad
z\ne0.
\]

This is the individual zero kernel appearing in a zero-side representation associated with the Li coefficients.

The project does not yet make any claim about commuting synthetic perturbation with an infinite zero summation.

The present calculation concerns the individual kernel only.

---

# 2. First derivative

Let

\[
g(z)
=
1-\frac1z.
\]

Then

\[
g'(z)=z^{-2}.
\]

Therefore

\[
f_n'(z)
=
-n g(z)^{n-1}z^{-2}.
\]

---

# 3. Second derivative

Differentiate again:

\[
f_n''(z)
=
-n
\left[
(n-1)g(z)^{n-2}z^{-4}
-
2g(z)^{n-1}z^{-3}
\right].
\]

Hence

\[
f_n''(z)
=
2n g(z)^{n-1}z^{-3}
-
n(n-1)g(z)^{n-2}z^{-4}.
\]

Factoring gives

\[
f_n''(z)
=
n g(z)^{n-2}z^{-4}
\left[
2g(z)z-(n-1)
\right].
\]

Since

\[
g(z)z=z-1,
\]

we obtain

\[
\boxed{
f_n''(z)
=
n
\left(
1-\frac1z
\right)^{n-2}
\frac{2z-n-1}{z^4}.
}
\]

---

# 4. Critical-line baseline

Let

\[
\rho_\gamma
=
\frac12+i\gamma,
\qquad
\gamma>0.
\]

Then

\[
2\rho_\gamma-n-1
=
-n+2i\gamma.
\]

Also,

\[
\left|
1-\frac1{\rho_\gamma}
\right|
=
1.
\]

Define

\[
\theta_\gamma
=
2\arctan\left(\frac1{2\gamma}\right).
\]

Then

\[
1-\frac1{\rho_\gamma}
=
e^{i\theta_\gamma}.
\]

Let

\[
r_\gamma^2
=
\gamma^2+\frac14.
\]

Writing

\[
\rho_\gamma=r_\gamma e^{i\phi_\gamma},
\]

one has

\[
\theta_\gamma=\pi-2\phi_\gamma.
\]

Therefore

\[
\rho_\gamma^{-4}
=
r_\gamma^{-4}e^{2i\theta_\gamma}.
\]

Substitution yields

\[
\boxed{
f_n''(\rho_\gamma)
=
\frac{n}
{\left(\gamma^2+\frac14\right)^2}
(-n+2i\gamma)
e^{in\theta_\gamma}.
}
\]

---

# 5. Exact quadratic susceptibility

For the conjugation-compatible Li kernel,

\[
\chi_n^{\mathrm{Li}}(\gamma)
=
2\Re f_n''(\rho_\gamma).
\]

Since

\[
\Re
\left[
(-n+2i\gamma)e^{in\theta_\gamma}
\right]
=
-n\cos(n\theta_\gamma)
-
2\gamma\sin(n\theta_\gamma),
\]

we obtain

\[
\boxed{
\chi_n^{\mathrm{Li}}(\gamma)
=
-
\frac{
2n
}{
\left(\gamma^2+\frac14\right)^2
}
\left[
n\cos(n\theta_\gamma)
+
2\gamma\sin(n\theta_\gamma)
\right],
}
\]

where

\[
\boxed{
\theta_\gamma
=
2\arctan\left(\frac1{2\gamma}\right).
}
\]

Equivalently,

\[
\boxed{
\chi_n^{\mathrm{Li}}(\gamma)
=
-
\frac{
2n
}{
\left(\gamma^2+\frac14\right)^2
}
\left[
n\cos\left(
2n\arctan\frac1{2\gamma}
\right)
+
2\gamma\sin\left(
2n\arctan\frac1{2\gamma}
\right)
\right].
}
\]

---

# 6. Exact magnitude bound

By Cauchy-Schwarz,

\[
\left|
n\cos x+2\gamma\sin x
\right|
\le
\sqrt{n^2+4\gamma^2}.
\]

Therefore

\[
\boxed{
\left|
\chi_n^{\mathrm{Li}}(\gamma)
\right|
\le
\frac{
2n\sqrt{n^2+4\gamma^2}
}{
\left(\gamma^2+\frac14\right)^2
}.
}
\]

---

# 7. Fixed-n large-height asymptotic

For large \(\gamma\),

\[
\theta_\gamma
=
\frac1\gamma
-
\frac1{12\gamma^3}
+
O(\gamma^{-5}).
\]

For fixed \(n\),

\[
\cos(n\theta_\gamma)
=
1-\frac{n^2}{2\gamma^2}
+
O_n(\gamma^{-4}),
\]

and

\[
\sin(n\theta_\gamma)
=
\frac n\gamma
+
O_n(\gamma^{-3}).
\]

Hence

\[
n\cos(n\theta_\gamma)
+
2\gamma\sin(n\theta_\gamma)
=
3n+O_n(\gamma^{-2}).
\]

Since

\[
\left(\gamma^2+\frac14\right)^2
=
\gamma^4
\left(
1+O(\gamma^{-2})
\right),
\]

it follows that

\[
\boxed{
\chi_n^{\mathrm{Li}}(\gamma)
=
-\frac{6n^2}{\gamma^4}
+
O_n(\gamma^{-6}).
}
\]

---

# 8. Mesoscopic scaling candidate

Suppose

\[
\gamma\to\infty
\]

through positive real values and \(n=n(\gamma)\) is integer-valued with

\[
\frac{n}{\gamma}\to c
\]

for some fixed

\[
c>0.
\]

Since

\[
\gamma\theta_\gamma\to1,
\]

one has

\[
n\theta_\gamma
=
\frac n\gamma
\left(
\gamma\theta_\gamma
\right)
\to c.
\]

Also,

\[
\frac n\gamma\to c
\]

and

\[
\frac{
\left(\gamma^2+\frac14\right)^2
}{
\gamma^4
}
\to1.
\]

Therefore the exact susceptibility formula suggests

\[
\boxed{
\gamma^2
\chi_n^{\mathrm{Li}}(\gamma)
\to
-2c
\left(
c\cos c+2\sin c
\right).
}
\]

Define

\[
\Psi_{\mathrm{Li}}(c)
=
-2c
\left(
c\cos c+2\sin c
\right).
\]

This is a candidate mesoscopic susceptibility profile.

---

# 9. Claim status

The exact derivative identity and susceptibility formula have been manually derived and adversarially checked algebraically.

The mesoscopic scaling statement is a candidate project proposition.

No originality claim is made.

A symbolic and independent numerical identity check must be completed before promotion to PROVED IN PROJECT.

A current literature audit is also required before discussing novelty.
