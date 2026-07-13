# Next Phase X10 — Log-Bump Interval Derivative Bounds

## Goal

Propagate primitive interval bounds for:

\[
\psi,\quad \psi',\quad \psi''
\]

to log-bumps:

\[
\phi(x)=\psi((\log x-c)/w).
\]

## Required formulas

\[
\phi'(x)=\psi'(u)\frac{1}{wx}
\]

\[
\phi''(x)=\psi''(u)\frac{1}{w^2x^2}-\psi'(u)\frac{1}{wx^2}
\]

where:

\[
u=(\log x-c)/w.
\]

## Next blocker

Interval enclosure of \(\log(x)\) over \(x\)-intervals.
