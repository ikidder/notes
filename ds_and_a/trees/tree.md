# tree
An abstract data type that stores element in a heirarchy. Each non-empty tree has a root node, which has no parent. Every other node in the tree has one parent and zero or more child nodes.

## terms
**root** - the one node without a parent  
**siblings** - two or more nodes that have the same parent  
**leaves** - (also called external nodes) - a node without any children  
**internal nodes** - a node with one or more children  
**edge** - an edge is a pair of nodes (u,v) s.t. u is a parent of v  
**path** - a sequence of nodes s.t. any two consective nodes forms an edge. 
**ordered** - a tree is ordered iff there is a linear order among the children of each node  

## Common use cases for trees:
* directory structure
* python Exception class inheritance

## Computing Depth of a node
the depth of a node n is the number of ancestors of n, excluding n itself.
```python

```
