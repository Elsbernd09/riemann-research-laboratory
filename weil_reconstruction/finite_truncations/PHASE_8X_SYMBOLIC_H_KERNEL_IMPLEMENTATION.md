# Phase 8X — Symbolic H-Kernel Implementation with Sanity Checks Only

## Purpose

Phase 8W created the implementation audit plan for the source-extracted \(H\)-kernel.

Phase 8X implements only scalar symbolic kernel functions:

\[
K,\quad K_t,\quad K^*,\quad H.
\]

This phase does not assemble matrices.

This phase does not compute eigenvalues.

This phase does not use zeta zeros.

This phase does not prove RH.

This phase does not claim novelty.

---

# 1. Implemented functions

The file

\[
\texttt{weil\_reconstruction/finite\_truncations/h\_kernel\_symbolic.py}
\]

implements:

\[
K(z)=\frac{\sin z}{z},
\]

with stable limiting value

\[
K(0)=1.
\]

It also implements:

\[
K_t(z)=K(tz),
\]

\[
K^*(x,y;t),
\]

and

\[
H(x,y;t)=\frac{2tK^*(x,y;t)}{1/4+y^2}.
\]

---

# 2. Sanity checks

The script

\[
\texttt{scripts/run\_phase8x\_h\_kernel\_sanity.py}
\]

checks:

1. \(K(0)=1\);
2. \(K(-z)=K(z)\);
3. \(K_t(-z)=K_t(z)\);
4. \(K^*\) is finite on deterministic synthetic samples;
5. \(H\) is finite on deterministic synthetic samples;
6. no matrices are assembled;
7. no eigenvalues are computed;
8. no zeta zeros are used.

---

# 3. Output

The sanity output is written to:

\[
\texttt{weil\_reconstruction/finite\_truncations/PHASE\_8X\_SANITY\_OUTPUT.txt}
\]

---

# 4. Current permission status

## Allowed now

Symbolic scalar evaluation of \(K,K_t,K^*,H\).

## Still denied

Matrix assembly.

Eigenvalue computation.

Zeta-zero experiments.

Bombieri-Weil numerical verification claims.

RH claims.

Novelty claims.

---

# 5. Boundary

This is a source-derived scalar kernel implementation.

It is not a matrix implementation.

It is not a numerical verification of Theorem 8.

It is not an RH result.

