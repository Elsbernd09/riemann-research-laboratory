# Bombieri–Lagarias Convention Extraction Table

| Object | Bombieri–Lagarias convention | Project convention | Status |
|---|---|---|---|
| Mellin transform | \(f(s)=\int_0^\infty f(x)x^{s-1}dx\) | \(\widehat f(s)=\int_0^\infty f(x)x^{s-1}dx\) | Match |
| Involution | \(\widetilde f(x)=x^{-1}f(1/x)\) | \(f^*(x)=x^{-1}\overline{f(1/x)}\) | Compatible after conjugation |
| Convolution | \((f\vee g)(x)=\int_0^\infty f(xy)g(y)dy/y\) | \((f*g)(x)=\int_0^\infty f(y)g(x/y)dy/y\) | Equivalent with convention tracking |
| Spectral product | \(M(f\vee\bar f)(s)=f(s)f(1-s)\) | \(\widehat{f*f^*}(s)=\widehat f(s)\overline{\widehat f(1-\bar s)}\) | Compatible |
| Critical-line positivity | real positive on \(\Re(s)=1/2\) | \(|\widehat f(1/2+it)|^2\) | Match |
| Explicit formula constant | \((\log\pi+\gamma)f(1)\) | earlier project sometimes used \((\log4\pi+\gamma)f(1)\) | Correction needed |
| Pole constraints | implicit through pole/integral terms | \(\widehat g(0)=\widehat g(1)=0\) | Needs further validation |

