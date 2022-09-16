# itertools

https://docs.python.org/3/library/itertools.html

from itertools import *

# Infinite Iterators

### count(start, [step])
```python
count(10)
10, 11, 12, 13, 14, ...
```

### cycle(iterable)
```python
cycle('ABC')
A B C A B C A ...
```

### repeat(elem, [times])
```python
repeat('a', 3)
'a' 'a' 'a'

repeat('b')
'b' 'b' 'b' 'b' ...
```

# Iterators terminating on the shortest input sequence

## accumulate(iterable, [func])
```python
accumulate([1,2,3,4,5])
1 3 6 10 15
```

### chain(i0, i1, i2, ...)
```python
chain('ABC', 'DEF')
A B C D E F
```

### chain.from_iterable(iterable)
```python
chain.from_iterable(['ABC', 'DEF'])
A B C D E F
```

### pairwise(iterable)
```python
pairwise('ABCDEFG')
AB BC CD DE EF FG
```

# Combinatoric Iterators

### product(i0, i1, i2, [repeat=1])

cartesian product. equivalent to nested for loops
```python
product('ABCD', repeat=2)
AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
```

### permutations(p, [r])

r-length tuples, all possible orderings, no repeated elements
```python
permutations('ABCD', 2)
AB AC AD BA BC BD CA CB CD DA DB DC
```

### combinations(p, r)
r-length tuples, in sorted order, no repeated elements
```python
combinations('ABCD', 2)
AB AC AD BC BD CD
```

### combinations_with_replacement(p,r)
r-length tuples, in sorted order, with repeated elements
```python
combinations_with_replacement('ABCD', 2)
AA AB AC AD BB BC BD CC CD DD
```