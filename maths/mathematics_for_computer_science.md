# Mathematics for Computer Science

https://courses.csail.mit.edu/6.042/spring17/mcs.pdf
https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/video_galleries/video-lectures/

Note: how to enter math symbols on a mac. Icon at the top right that looks like a window. Click Show Emojis and symbols. 
Click Icon at top right of that window to expand and show the search bar. 

# Proofs - Chapter 1

**Proposition** a statement that is either true or false.
Examples of propositions:
* 2 + 3 = 5
* 1 + 1 = 3 (does not need to be true to be a proposition)
Examples of statements that are not propositions:
* Wherefore art thou Romeo
* Give me an A!
* It's 5 o'clock. (if truth varies according to circumstances, it can't be a proposition)

**Mathematical Proof** a mathematical proof of a proposition is a chain ofr logical deductions leading to the proposition from a base set of axioms.

**Predicate** a proposition whose truth depends on the value of one or more variables. Predicates are denoted by capital `P`. `P(n)` is a predicate that is either true or false, depending on the value of `n`.
Example:
predicate -> "n is a perfect square"
true proposition -> "n is a perfect square, and n = 4"
false proposition -> "n is a perfect square, and n = 5"

**Axiomatic Method** - Invented by Euclid for geometry. A sequence of logical deductions from axioms that concludes with the proposition.

**Axiom** - a proposition that is accepted as true. e.g. there is a straight line between two points.

**Theorem** - an important true proposition

**Corollary** - a proposition that follows in just a few logical steps from a theorem

**Lemma** - a preliminary proposition useful for proving other propositions

**Antecedents** - propositions in a proof before the consequent

**Conclusion/Consequent** - the last proposition in a proof

**Sound** - about inference rules. If assigning True to all the antecedents of an inference rule _must_ make the consequent true, then the rule is sound.

## Inference rules 
also called logical deductions, are used to prove new propositions using previous true propositions.  
∧ - and  
∨ - or  
-> - implies  
|- - therefore  
for codepoints, see: https://en.wikipedia.org/wiki/List_of_logic_symbols  
* **modus ponens** ((p -> q) ∧ p) |- q 
* **modus tolens** ((p -> q) ∧ -q) |- -p
* **hypothetical syllogism** ((p -> q) ∧ (q -> r) |- (p -> r)
* **disjunctive syllogism** ((p ∨ q) ∧ -p) |- q

for more, see https://en.wikipedia.org/wiki/Propositional_calculus#Basic_and_derived_argument_forms

## Patterns of Proofs

### Proving an Implication
An implication is a proposition of the form p -> q. (if p then q)
methods:
1. assume p, and show that q follows
2. assume -q, and show that -p follows. 
    * this is proving the contrapositive. p -> q is logically equivalent to its contrapositive -q -> -p

### Proving an "if and only if"
iff means logically equivalent  
example: two triangles have the same side lengths iff two side lengths and the angles between them are the same.
methods:
1. (p iff q) means ((p -> q) ∧ (q -> p)). Prove the iff by proving both implications.
2. construct a chain of iff's. Prove that p is equivalent to some statement(s) that is equivalent to q.

### Proof by Cases
methods:
1. breaking a complicated proof into cases and proving each case separately is common.

### Proof by Contradiction
show that if a proposition were flase, then some false fact would be true. 


**Sidenote** - Goldbach's Conjecture 
Every event integer greater than 2 is the sum of two primes. Known to hold for all numbers up to 10^18.

# The Well Ordering Principle - Chapter 2

_Every nonempty set of nonnegative integers has a smallest element_.

One of the most important proof rules in discrete maths.

See text for well ordering proof template

**Prime Factorization Theorem** Every positive integer greater than one can be factored as a product of primes.
(this can be proved by the Well Ordering Principle)

**Well Ordered Sets** - a set of real numbers is well ordered when each of its nonempty subsets has a minimum element. 

**theorem** For any nonnegative integer n, the set of integers greater than or equal to -n is well ordered.

**Lower and Upper Bounds** of a set - just the min and max element

# Logical Formulas - Chapter 3

can test the equavalence of two propositions by comparing their truth tables. if the truth tables are the same, then they are equivalent


## Quantifiers
∀ - for all
∃ - there exists at least one
∃! - there exists exactly one

The order of quantifiers is significant. Consider "Every American has a dream". This is ambiguous because the order of quantifiers is unclear. Define the predicate H(a,d) to be "American a has dream d". The sentence could mean `∃d ∈ D ∀a ∈ A. H(a,d)`, meaning that there is a single dream that every American shares. Or it could mean `∀a ∈ A ∃d ∈ D. H(a,d)`, meaning every American has a personal dream.


## DeMorgan's Laws
* -(P ∨ Q) <-> -P ∧ -Q  ... not (A or B) = (not A) and (not B) ;  
* -(P ∧ Q) <-> -P ∨ -Q  ... not (A and B) = (not A) or (not B) 


# Mathematical Data Types Chapter 4

## Sets
A set is a bunch of objects, which could be numbers, points, or other sets. 

Write a set with curly braces: A = {red, blue, yellow} or B = {1,2,3,4,...}

The order of elements is not significant. The sets {x,y} and {y,x} are the same set.

### Popular sets
∅ - empty set
ℕ - nonnegative integers
ℤ - integers
Q - rational numbers
R - real numbers
C - complex numbers

### Comparing and Combining Sets
`S ⊆ T` set S is a subset of T. Meaning that every element of S is also an element of T. Note that S could equal T.  
`S ⊂ T` set S is a _strict_ subset of T. Every element of S is also an element of T. The sets can't be equal here.  
(Think of it like <= and <.)
`A ∪ B` the union of A and B. includes the elements apprearing in A or B or both.  
`A ∩ B` the intersection of A and B. includes the elements appearing in both A and B.  
`--A` (supposed to be a long bar over capital A. can't find the symbol.) this is the complement of A.
includes all the elements of D (whatever the Domain is) that are not in A.
`pow(A)` power set. the set of all subsets of A. B ∊ pow(A) iff B ⊆ A.  
    * pow({1,2}) = {∅, {1}, {2}, {1,2}}
    * if A has n elements, then there are 2^n sets in pow(A). 

### Set builder notation
`A ::= { n ∊ ℕ | n is a prime and n == 4k + 1 for some integer k }`  
`D ::= { L ∊ books | L is cited in this text }`

### Proving set equality
two sets are defined as equal if they have exactly the same elements. That is,
`X = Y` means that `∀z, z ∊ X iff z ∊ Y`

**Distributive Law of Sets**  
`A ∩ (B ∪ C) == (A ∩ B) ∪ (A ∩ C)`

### Sequences
containers, like sets. But, unlike sets, sequences:
* allow duplicate elements
* elements have a specified order
* empty sequence symbol: ()

### Cartesian product
a Cartesian product of sets S1 x S2 . . . Sn is a new set consisting of all sequences where the first component is drawn from S1, the second from S2, etc. Length two sequences are called pairs. For example, ℕ x {a,b} is the set of all pairs whose first element is a nonnegative integer and whose second element is an a or b.  

`ℕ x {a,b} == { (0,a), (0,b), (1,a), (1,b) (2,a), (2,b) . . . } ` 

A product of n copies of a set S is denoted S^n.  
`{0,1}^3 == { (0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1) }`

### Functions

A function assigns an element of one set, called the **domain**, to an element of another set, called the **codomain**.  
Notation for f is a function with domain A and codomain B: `f : A -> B`

The familiar notation `f(a) == b` means b is the value of f at argument a.

A function can also be defined by a procedure for computing the value at any element of the domain. For example,
if f(a) is the length of a left to right search of the bits until a 1 appears:
```
f(0010) == 3
f(100) == 1
f(0000) is undefined
```

### Function Composition 
For funtions `f : A -> B` and `g : B -> C`, the composition `g ∘ f` is definted to be the cuntaion from A to C:
`(g ∘ f)(x) ::== g(f(x))`

### Binary relations
Binary relations define relations between two objects.    
A binary relation `R` consists of a set `A`, called the domain of `R`, a set `B` called the codomain of `R`, and a
subset of `A x B` called the **graph** of `R`.

### Classes of functions 
nice pictures at: https://en.wikipedia.org/wiki/Bijection,_injection_and_surjection
* **injection** - The function is injective, or one-to-one, if each element of the codomain is mapped to by at most one element of the domain, or equivalently, if distinct elements of the domain map to distinct elements in the codomain. An injective function is also called an injection
* **surjective** - The function is surjective, or onto, if each element of the codomain is mapped to by at least one element of the domain. That is, the image and the codomain of the function are equal. A surjective function is a surjection.
* **bijectiv** - The function is bijective (one-to-one and onto, one-to-one correspondence, or invertible) if each element of the codomain is mapped to by exactly one element of the domain. That is, the function is both injective and surjective. A bijective function is also called a bijection.

### Cardinality
cardinality is the size of a set

If `A` is a finite set, the cardinality `|A|` of `A` is the number of elements in `A`.

### Number of subsets of a finite set
`|A| == n implies |pow(A)|==2^n`

# Induction Chapter 5

induction is a defining characteristic of discrete -- as opposed to continuous -- mathematics.

## Ordinary Induction

```
Let P be a predicate on nonnegative integers. if
* P(0) is true, and
* P(n) implies P(n+1) for all nonnegatives integers n
then
* P(m) is true for all nonnegative integers m
```



