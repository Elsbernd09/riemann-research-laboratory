# Next Phase X3 — Built-In Pole-Cancelled Smooth Basis

## Goal

Build smooth compactly supported basis functions \(\phi_j\) satisfying:

\[
\widehat \phi_j(0)=0,
\qquad
\widehat \phi_j(1)=0.
\]

## Strategy

Start with raw smooth bumps \(b_j\), then subtract two correction bumps \(u_0,u_1\):

\[
\phi_j=b_j-\alpha_j u_0-\beta_j u_1.
\]

Choose \(\alpha_j,\beta_j\) by solving:

\[
\widehat \phi_j(0)=0,
\qquad
\widehat \phi_j(1)=0.
\]

## Result

Every finite combination:

\[
g_a=\sum_j a_j\phi_j
\]

automatically satisfies:

\[
\widehat g_a(0)=0,
\qquad
\widehat g_a(1)=0.
\]

Thus \(f_a=g_a*g_a^*\) satisfies the locked \(f\)-pole cancellation target.

