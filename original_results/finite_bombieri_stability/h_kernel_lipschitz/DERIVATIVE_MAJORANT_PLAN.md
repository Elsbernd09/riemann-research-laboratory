# Derivative Majorant Plan

## Kernel pieces

The branch separates the kernel into pieces:

1. sinc-like core \(K_t(z)=\sin(tz)/(tz)\);
2. shifted \(K_t\)-terms;
3. products of shifted \(K_t\)-terms;
4. rational factor \((1/4+y^2)^{-1}\);
5. scalar prefactor \(2t\).

## Required derivative bounds

We need bounds for:

\[
K_t(z),
\]

\[
K_t'(z),
\]

\[
\frac{1}{1/4+y^2},
\]

and

\[
\frac{d}{dy}\frac{1}{1/4+y^2}.
\]

## Majorants

Use majorants:

\[
A_0(U,t)\geq\sup |K_t|,
\]

\[
A_1(U,t)\geq\sup |K_t'|,
\]

\[
B_0(U)\geq\sup |(1/4+y^2)^{-1}|,
\]

\[
B_1(U)\geq\sup \left|\frac{d}{dy}(1/4+y^2)^{-1}\right|.
\]

## Next phase

The next phase should write symbolic formulas for:

\[
\partial_x H(x,y;t)
\]

and

\[
\partial_y H(x,y;t)
\]

in majorant form, without pretending to solve RH or verify zeta zeros.

## Boundary

This plan does not prove RH.

This plan does not falsify RH.

This plan does not use zeta zeros.

This plan does not claim novelty.

