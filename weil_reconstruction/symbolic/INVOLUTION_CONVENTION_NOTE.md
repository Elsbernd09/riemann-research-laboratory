# Involution Convention Note

## Current recorded convention

\[
f^*(x)=x^{-1}f(1/x).
\]

Under the Mellin transform convention

\[
f(s)=\int_0^\infty f(x)x^{s-1}dx,
\]

this gives

\[
f^*(s)=f(1-s).
\]

## Positivity caution

For real-valued functions, the non-conjugated and conjugated conventions can appear similar.

For complex-valued functions, they differ.

Before any finite-rank positivity computation, the project must source-lock whether Bombieri's star operation includes complex conjugation, transpose, or both in each context.

## Current status

Non-conjugated Mellin identity:

LOCKED ALGEBRAICALLY.

Complex positivity convention:

UNLOCKED.

Finite-rank positivity implementation:

BLOCKED.

