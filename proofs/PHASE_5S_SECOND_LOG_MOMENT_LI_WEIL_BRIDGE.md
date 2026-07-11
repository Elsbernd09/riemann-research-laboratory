# Phase 5S — Second Log-Moment Li Test Function and Weil Bridge

## Status

EXACT MELLIN BRIDGE PROVED.

FINITE SIGNED WEIL-RANK QUESTION OPEN.

## Prior-art correction

The Li individual-zero kernel

\[
f_n(s)
=
1-\left(1-\frac1s\right)^n
\]

is already explicitly embedded into Guinand-Weil explicit-formula machinery in the classical Li literature.

Bombieri-Lagarias derive arithmetic formulas for Li coefficients through the Guinand-Weil explicit formula.

Later treatments record the corresponding inverse-Mellin test function explicitly.

Therefore no originality claim is permitted for embedding the Li kernel itself into the explicit formula.

---

# 1. Classical Li test transform

Define

\[
f_n(s)
=
1-\left(1-\frac1s\right)^n.
\]

The classical inverse-Mellin test function may be written in logarithmic coordinates as

\[
G_n(y)
=
e^{-y/2}
\sum_{\ell=1}^n
\binom n\ell
\frac{(-1)^{\ell-1}y^{\ell-1}}
{(\ell-1)!},
\qquad
y>0,
\]

with

\[
G_n(y)=0
\]

for

\[
y<0.
\]

Under the standard Mellin/logarithmic transform convention,

\[
\boxed{
f_n(s)
=
\int_{-\infty}^{\infty}
G_n(y)
e^{-(s-1/2)y}
\,dy.
}
\]

Equivalently, in the multiplicative variable

\[
x=e^{-y},
\]

there is a test function \(g_n(x)\) satisfying

\[
\boxed{
f_n(s)
=
\int_0^\infty
g_n(x)x^{s-1}\,dx.
}
\]

This is classical Li/Guinand-Weil machinery.

---

# 2. Mellin differentiation identity

Let

\[
\mathcal M[g](s)
=
\int_0^\infty
g(x)x^{s-1}\,dx.
\]

Whenever differentiation under the integral is justified,

\[
\frac{d}{ds}
\mathcal M[g](s)
=
\int_0^\infty
g(x)x^{s-1}\log x\,dx.
\]

Differentiating again,

\[
\boxed{
\frac{d^2}{ds^2}
\mathcal M[g](s)
=
\int_0^\infty
g(x)x^{s-1}
(\log x)^2
\,dx.
}
\]

Thus if

\[
f_n=\mathcal M[g_n],
\]

then

\[
\boxed{
f_n''(s)
=
\mathcal M[
(\log x)^2g_n(x)
](s).
}
\]

---

# 3. Logarithmic-coordinate form

Under

\[
x=e^{-y},
\]

we have

\[
\log x=-y.
\]

Therefore

\[
(\log x)^2=y^2.
\]

Consequently,

\[
\boxed{
f_n''(s)
=
\int_{-\infty}^{\infty}
y^2G_n(y)
e^{-(s-1/2)y}
\,dy.
}
\]

Define the second log-moment Li test function

\[
\boxed{
G_n^{(2)}(y)
=
y^2G_n(y).
}
\]

Then

\[
\boxed{
f_n''(s)
=
\mathcal L_{\mathrm{bilateral}}
[
G_n^{(2)}
](s-1/2)
}
\]

in the corresponding logarithmic Mellin convention.

---

# 4. Li susceptibility spectral representation

The project Li susceptibility is

\[
\chi_n^{Li}(\gamma)
=
2\Re
f_n''
\left(
\frac12+i\gamma
\right).
\]

Substituting the exact transformed test function gives

\[
\boxed{
\chi_n^{Li}(\gamma)
=
2\Re
\int_{-\infty}^{\infty}
G_n^{(2)}(y)e^{-i\gamma y}\,dy.
}
\]

Because

\[
G_n^{(2)}(y)=0
\]

for

\[
y<0,
\]

this is equivalently

\[
\boxed{
\chi_n^{Li}(\gamma)
=
2
\int_0^\infty
y^2G_n(y)
\cos(\gamma y)
\,dy.
}
\]

Thus the Li susceptibility is the cosine response of the second log-moment deformation of the classical Li test function.

---

# 5. Exact polynomial form

For

\[
y>0,
\]

\[
G_n^{(2)}(y)
=
e^{-y/2}
\sum_{\ell=1}^n
\binom n\ell
\frac{(-1)^{\ell-1}y^{\ell+1}}
{(\ell-1)!}.
\]

Therefore the susceptibility test family is explicitly finite-dimensional at each fixed \(n\):

\[
\boxed{
G_n^{(2)}
\in
e^{-y/2}
\operatorname{span}
\{
y^2,y^3,\ldots,y^{n+1}
\}
\mathbf 1_{y>0}.
}
\]

This finite polynomial-exponential structure is inherited directly from the classical Li test function.

---

# 6. Prior-art boundary

The following are classical or directly subsumed by prior art:

1. the Li kernel

\[
1-(1-1/s)^n;
\]

2. its zero-side summation in the Li coefficients;

3. its Guinand-Weil explicit-formula arithmetic interpretation;

4. its inverse-Mellin test-function realization.

The project does not claim originality for these items.

The project-specific object is the horizontal zero-coordinate susceptibility

\[
2\Re f_n''(1/2+i\gamma)
\]

and its matched-scale response analysis.

The exact Mellin identity shows that this susceptibility corresponds to the second logarithmic moment weighting of the classical Li test family.

No subsuming source for the full susceptibility/matched-scale specialization has been identified in the current audit.

This is not a novelty claim.

---

# 7. Weil quadratic-form question

The Weil quadratic form is built from Hermitian convolution structures.

The test function

\[
G_n^{(2)}(y)
=
y^2G_n(y)
\]

is not automatically a convolution square and is not automatically of positive type.

Therefore classical Weil positivity does not directly imply a sign for

\[
\chi_n^{Li}(\gamma).
\]

This is consistent with the exact sign-changing matched-scale profile

\[
\Psi_{Li}(c).
\]

The next structural question is whether

\[
G_n^{(2)}
\]

admits a finite signed convolution-square decomposition of the form

\[
G_n^{(2)}
=
\sum_{j=1}^r
\sigma_j
u_{n,j}
*
\widetilde u_{n,j},
\qquad
\sigma_j\in\{-1,+1\},
\]

with finite \(r\), or an equivalent finite-rank representation in the Fourier-side Weil quadratic form.

A uniformly controlled rank or signature would provide a direct structural bridge between Li susceptibility and Weil energy geometry.

No such decomposition is proved in this phase.

---

# 8. Restrictions

This phase does not prove RH.

The Li kernel's explicit-formula embedding is classical.

The second-log-moment Mellin bridge is elementary Mellin differentiation.

No positivity result is obtained.

No finite signed Weil-rank result is yet proved.

No originality claim is made for classical Li or Weil machinery.

