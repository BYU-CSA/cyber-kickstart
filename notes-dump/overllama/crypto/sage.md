## Matrices

Definition: `A = matrix([[0,2,0,0],[3,0,0,0],[0,0,5,0],[0,0,0,7]])`
You can get the reduced form of a given matrix, `A`, by using `A.rref()`
Inverse matrix: `A*A**-1 == 1`, `A.inverse()`
Diagonal matrix: only diagonal has non-zero values. Matrix multiplication with diagonal matrices is commutative. `A**T == A` for all diagonal matrices.
You can augment a matrix `A` with a vector `b` using `A.augment(b)`, which just attaches `b` to `A`
Get an index of `A` using `A.row(0)` or `A.column(0)`
Transpose: `A.transpose()` / `A.T`
A minor is a version of a matrix denoted by `Mij` where the minor is the same as the original matrix but excluding row `i` and column `j`
`M.determinant() == det(M) == M.det()`
You can also augment and solve using `M.solve_right(r)`
## Vectors
Definition: `v = vector([0,1])`
You can subtract or add vectors
Norm: `v.norm() # square root of sum`
Dot product / inner product: `v.inner_product(v1)`
A vector space must be closed, commutative, associative, has a neutral element, and an inverse under addition, and has all of that except an inverse under multiplication
A basis for a vector space is a set of B vectors that is linearly independent and spans the space
If `|B| == n` for some n in NN, we define the dimension of B to be n
You can define permutations of some matrix in sage with:
```sage
sage: per=Permutation((1,3,2))
sage: per
[3, 1, 2]
sage: matrix(per)
[0 1 0]
[0 0 1]
[1 0 0]
sage: grelt=PermutationGroupElement([1,3,2])
sage: grelt.matrix()
[1 0 0]
[0 0 1]
[0 1 0]
```
As seen, it will switch the ordering if you input it as a tuple versus as a list, so keep that in mind
`matrix(per).inverse()==matrix(per).T`
## Lattices
You can construct a lattice using: `sage: M = matrix(ZZ, [[1,2], [-1,1]])` and then check for inclusion using `vector([-101,5]) in span(M)`. You can then `M.solve_left(vector([-101,5]))` to find how that point is constructed in form `-32*M[0] + 69*M[1]` for point `(-32, 69)`
## Factoring
When you're trying to factor using sagemath, it uses `pari` as it's default factoring package. If you want things to factor faster, just `addprimes`. Then `pari` will have access to the factors you want when it goes and therefore won't have to do as much work.
```sage
p = random_prime(1<<512)
p = random_prime(1<<512)
n = p*q
pari.addprimes(p)
n.factor()
```