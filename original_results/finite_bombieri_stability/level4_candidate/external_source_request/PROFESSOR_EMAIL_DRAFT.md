# Professor Email Draft

Subject: Question about the exact Weil positivity quadratic form in Bombieri’s formulation

Dear Professor,

I am working through a finite-dimensional Bombieri/Weil-style positivity framework related to the Riemann Hypothesis. I want to be very clear that I am not claiming a proof or breakthrough. I am trying to correctly identify the classical objects before going further.

I have reconstructed the following explicit-formula functional:

\[
T[f]
=
\int_0^\infty f(x)\,dx
+
\int_0^\infty f^*(x)\,dx
-
\sum_{n=1}^{\infty}\Lambda(n)\{f(n)+f^*(n)\}
-
(\log 4\pi+\gamma_E)f(1)
-
\int_1^\infty
\left(
f(x)+f^*(x)-\frac{2f(1)}{x}
\right)
\frac{x\,dx}{x^2-1},
\]

with

\[
f^*(x)=x^{-1}f(1/x).
\]

I have seen this connected to a zero-side expression of the form

\[
T[f]=\sum_\rho f(\rho).
\]

My question is:

In the classical Weil positivity criterion, what exact function \(F_g\) is inserted into \(T\) to define the quadratic form

\[
Q_W(g)=T[F_g]?
\]

I want to avoid guessing the wrong convolution, involution, Mellin-transform, or sign convention.

Could you point me to the exact definition of \(F_g\), the admissible test-function space, and the precise sign convention in the RH positivity theorem?

My current goal is modest: to understand whether a finite-dimensional approximation \(Q_N(P_Ng)\) can be shown to converge to the true \(Q_W(g)\) on a controlled finite test class. I am not claiming this has been achieved.

Thank you very much,

Michael Elsbernd

