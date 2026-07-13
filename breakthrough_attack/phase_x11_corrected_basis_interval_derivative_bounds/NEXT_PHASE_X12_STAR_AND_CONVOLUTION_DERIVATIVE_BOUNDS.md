# Next Phase X12 — Star and Convolution Derivative Bounds

## Goal

Use corrected-basis bounds to bound:

\[
\Phi^*,\quad (\Phi^*)',\quad (\Phi^*)''
\]

and then:

\[
F=\Phi*\Phi^*,
\qquad
F''.
\]

## Target

Create an interval upper bound for:

\[
\|F''\|_\infty.
\]

## Main formula

\[
(\Phi^*)''(x)
=
2x^{-3}\Phi(1/x)
+
4x^{-4}\Phi'(1/x)
+
x^{-5}\Phi''(1/x).
\]

Then:

\[
\|F''\|_\infty
\le
\frac12
\|\Phi\|_\infty
\|(\Phi^*)''\|_\infty
(L^{-2}-U^{-2}).
\]
