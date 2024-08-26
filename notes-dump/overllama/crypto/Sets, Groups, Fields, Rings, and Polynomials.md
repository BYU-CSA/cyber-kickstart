### Set Theory, Group Theory, Field Theory, and Ring Theory speed run
Sets are just collections of things with shared attributes of some kind. You can represent them all kinds of ways so most of the reading of math documentation is found in Set Theory
There are also operations that are important. Unions, subtractions, etc.

A group is a set where it has some operation where that operation is associative (order of operations doesn't matter when it's just the operation itself, i.e. parenthesis can move around and it won't affect output), has an identity element, and every element of the set has an inverse. So group is set + operation
The identity element will be unique, as will inverses by definition
  
A field is a set where addition, subtraction, multiplication, and division are defined. More specifically, it just matters that addition and multiplication be defined, then an additive inverse and multiplicative inverse must follow. These operations must comply with: associativity (order doesn't matter), commutativity (they can switch), identity elements (e) must exist for both operations such that a + e1 = a and a * e2 = a where e1 and e2 can be unique, there must be an additive and multiplicative inverse, and there must be distributivity of multiplication over addition. Those properties are also called the **field axioms**
A finite field is a field that contains a finite number of elements. Each operation of that field then results in another member of the field. The **order** of a finite field is its number of elements and is traditionally a prime number or a prime power.
  
A ring generalizes a field, or makes it so that multiplication and a multiplicative inverse are no longer necessary for its existence. Multiplication will still exist, since it's just a summation at heart, but it isn't required to carry with it inverses not commutation. Some rings are commutative, which gives them very different properties from other rings.
**Ring axioms**: it is an abelian group under addition (associative, commutative, there is an identity, and an inverse), it is a monoid under multiplication (associative and an identity), and multiplication is distributive with respect to addition
  
### Polynomials
A polynomial is an expression consisting of indeterminates (variables, just a symbol not standing for anything but itself) and coefficients. It involves just addition, subtraction, multiplication, and exponentiation to a nonnegative power.
  
A polynomial ring, then, is a polynomial where all coefficients fall into another ring (often a field).