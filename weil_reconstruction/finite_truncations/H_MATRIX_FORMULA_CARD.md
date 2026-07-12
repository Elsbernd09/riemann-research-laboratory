# H-Matrix Formula Card

## Base kernel

\[
K(x)=\frac{\sin x}{x}.
\]

Scaled notation:

\[
K_t(x)=K(tx).
\]

## Corrected kernel

\[
K^*(x,y;t)
=
K_t(x-y)
-
\frac{t}{\sinh t}
\left(\frac12+iy\right)
K_t\left(\frac i2-y\right)
K_t\left(\frac i2+x\right)
-
\frac{t}{\sinh t}
\left(\frac12-iy\right)
K_t\left(\frac i2+y\right)
K_t\left(\frac i2-x\right).
\]

## H kernel

\[
H(x,y;t)
=
\frac{2t\,K^*(x,y;t)}{\frac14+y^2}.
\]

Therefore,

\[
H(\gamma,\gamma';t)
=
\frac{2t\,K^*(\gamma,\gamma';t)}{\frac14+(\gamma')^2}.
\]

## Coefficient equation

\[
w_\gamma
=
\Lambda
\sum_{\gamma'\in\Gamma}
H(\gamma,\gamma';t)w_{\gamma'}.
\]

## Status

Formula-level source extraction: COMPLETE.

Implementation: BLOCKED.

Reason:

Theorem 8, exact finite matrix convention, and finite eigenvalue interpretation remain unlocked.

