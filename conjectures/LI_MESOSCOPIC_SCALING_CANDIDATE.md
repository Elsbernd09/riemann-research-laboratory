# Li Mesoscopic Susceptibility Scaling Candidate

## Status

CANDIDATE PROJECT PROPOSITION

Not yet PROVED IN PROJECT.

Not asserted to be original.

---

## Statement

Let

\[
f_n(z)
=
1-
\left(
1-\frac1z
\right)^n
\]

for integers \(n\ge1\).

For \(\gamma>0\), define

\[
\rho_\gamma
=
\frac12+i\gamma
\]

and

\[
\chi_n^{\mathrm{Li}}(\gamma)
=
2\Re f_n''(\rho_\gamma).
\]

Suppose

\[
\gamma_j\to\infty
\]

and \(n_j\) is a sequence of positive integers satisfying

\[
\frac{n_j}{\gamma_j}\to c
\]

for some fixed \(c>0\).

Then the candidate proposition is

\[
\boxed{
\gamma_j^2
\chi_{n_j}^{\mathrm{Li}}(\gamma_j)
\to
-2c
\left(
c\cos c+2\sin c
\right).
}
\]

Define the candidate profile

\[
\Psi_{\mathrm{Li}}(c)
=
-2c
\left(
c\cos c+2\sin c
\right).
\]

---

## Why this matters to the project

The scaling \(n\asymp\gamma\) is the regime in which the Li-kernel phase

\[
n\theta_\gamma
\]

remains order one because

\[
\theta_\gamma\sim\gamma^{-1}.
\]

This suggests that the natural diagnostic index scale for local quadratic response at height \(\gamma\) may be proportional to \(\gamma\).

This interpretation is project-level and has not been established as novel or as useful for RH itself.

---

## Required adversarial tests

1. independent symbolic differentiation;
2. direct finite-difference convergence to the exact susceptibility;
3. numerical scaling collapse for several values of \(c\);
4. analysis of \(c\to0\);
5. analysis of large \(c\);
6. study of zeros and sign changes of \(\Psi_{\mathrm{Li}}\);
7. prior-art audit;
8. determine whether the result is a trivial repackaging of known Li-coefficient zero contribution asymptotics.
