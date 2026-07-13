# Next Phase X9 — Primitive Interval Bump Bounds

## Goal

Create rigorous interval bounds for:

\[
\psi,\quad \psi',\quad \psi''
\]

on subintervals of \((-1,1)\).

## Why

X8 reduced derivative certification to primitive bump bounds.

## Required

1. interval arithmetic class;
2. interval operations for addition, multiplication, division, exponential;
3. interval enclosure for \(1-u^2\);
4. interval enclosure for \(\psi(u)=\exp(-1/(1-u^2))\);
5. interval enclosure for \(\psi'(u)\);
6. interval enclosure for \(\psi''(u)\);
7. proof-oriented outward rounding warning.

## Honest status target

The next phase may still be conservative unless true outward rounding is implemented.
