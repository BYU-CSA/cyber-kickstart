Okay, let's get some properties here, fellas. 
On a given elliptic curve *E*, x(P) == x(Q) if and only if P == Q or P == (-)Q, so in negation on an elliptic curve, the x value will not change. Negation on the curve, therefore, is defined as (-) : (x : y : 1) -> (x : -y : 1)
The group law, (+), is harder to define, but we can do so with a series of equations:
- *x*<sub>(+)</sub> = *B*λ<sup>2</sup> - (*x*<sub>P</sub> + *x*<sub>Q</sub>) - *A*
- *y*<sub>(+)</sub> = (2*x*<sub>P</sub> + *x*<sub>Q</sub> + *A*)λ - Bλ<sup>3</sup> - *y*<sub>P</sub> = λ(*x*<sub>P</sub> - *x*<sub>(+)</sub>) - *y*<sub>P</sub>
- λ = (*y*<sub>Q</sub> - *y*<sub>P</sub>)/(*x*<sub>Q</sub> - *x*<sub>P</sub>) if *P* != *Q* or (-)*Q*
-    = (3*x*<sup>2</sup><sub>P</sub> + 2*Ax*<sub>P</sub> + 1)/(2*By*<sub>P</sub>) if *P* = *Q*
It's important to note as well that if *P* = (-)*Q*, then *P* (+) *Q* = *O*

### Montgomery Ladder
The Montgomery ladder tries to simplify the ability to take x(P) -> x(\[k]P) instead of going from P -> \[k]P
When we talk about points on a curve (x,y), we end up talking about them typically in terms of the projective plane coordinates (X : Y : Z), where x = X/Z and y = Y/Z, in other words (X : Y : Z) = (xZ : yZ : Z). We can then define the point at infinity as (0 : 1 : 0). This is the only point on *E*<sub>(a,b)</sub> where Z = 0
