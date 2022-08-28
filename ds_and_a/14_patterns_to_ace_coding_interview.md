# 14 patterns
https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed

## Sliding window
Following are some ways you can identify that the given problem might require a sliding window:
* The problem input is a linear data structure such as a linked list, array, or string
* You’re asked to find the longest/shortest substring, subarray, or a desired value

Common problems you use the sliding window pattern with:
* Maximum sum subarray of size ‘K’ (easy)
* Longest substring with ‘K’ distinct characters (medium)
* String anagrams (hard)

## Two pointers
Two Pointers is a pattern where two pointers iterate through the data structure in tandem until one or both of the pointers hit a certain condition.Two Pointers is often useful when searching pairs in a sorted array or linked list; for example, when you have to compare each element of an array to its other elements.

Ways to identify when to use the Two Pointer method:
* It will feature problems where you deal with sorted arrays (or Linked Lists) and need to find a set of elements that fulfill certain constraints
* The set of elements in the array is a pair, a triplet, or even a subarray

Here are some problems that feature the Two Pointer pattern:
* Squaring a sorted array (easy)
* Triplets that sum to zero (medium)
* Comparing strings that contain backspaces (medium)

## Fast and Slow pointers
The Fast and Slow pointer approach, also known as the Hare & Tortoise algorithm, is a pointer algorithm that uses two pointers which move through the array (or sequence/linked list) at different speeds. This approach is quite useful when dealing with cyclic linked lists or arrays.

How do you identify when to use the Fast and Slow pattern?
* The problem will deal with a loop in a linked list or array
* When you need to know the position of a certain element or the overall length of the linked list.

Problems featuring the fast and slow pointers pattern:
* Linked List Cycle (easy)
* Palindrome Linked List (medium)
* Cycle in a Circular Array (hard)

## Merge Intervals
The Merge Intervals pattern is an efficient technique to deal with overlapping intervals. In a lot of problems involving intervals, you either need to find overlapping intervals or merge intervals if they overlap. The pattern works like this:

Given two intervals (‘a’ and ‘b’), there will be six different ways the two intervals can relate to each other:
1. a and b do not overlap
2. a and b overlap, b ends after a
3. a completely overlaps b
4. a and b overlap, a ends after b
5. b completely overlaps a
6. a and b do not overlap

How do you identify when to use the Merge Intervals pattern?
* If you’re asked to produce a list with only mutually exclusive intervals
* If you hear the term “overlapping intervals”.

Merge interval problem patterns:
* Intervals Intersection (medium)
* Maximum CPU Load (hard)

## Cyclic sort
This pattern describes an interesting approach to deal with problems involving arrays containing numbers in a given range. The Cyclic Sort pattern iterates over the array one number at a time, and if the current number you are iterating is not at the correct index, you swap it with the number at its correct index.

How do I identify this pattern?
* They will be problems involving a sorted array with numbers in a given range
* If the problem asks you to find the missing/duplicate/smallest number in an sorted/rotated array

* Problems featuring cyclic sort pattern:
* Find the Missing Number (easy)
* Find the Smallest Missing Positive Number (medium)

## In-place reversal of linked list
This pattern reverses one node at a time starting with one variable (current) pointing to the head of the linked list, and one variable (previous) will point to the previous node that you have processed. 

How do I identify when to use this pattern:
* If you’re asked to reverse a linked list without using extra memory

Problems featuring in-place reversal of linked list pattern:
* Reverse a Sub-list (medium)
* Reverse every K-element Sub-list (medium)

## BFS
This pattern is based on the Breadth First Search (BFS) technique to traverse a tree and uses a queue to keep track of all the nodes of a level before jumping onto the next level. Any problem involving the traversal of a tree in a level-by-level order can be efficiently solved using this approach.

The Tree BFS pattern works by pushing the root node to the queue and then continually iterating until the queue is empty. For each iteration, we remove the node at the head of the queue and “visit” that node. After removing each node from the queue, we also insert all of its children into the queue.

How to identify the Tree BFS pattern:
* If you’re asked to traverse a tree in a level-by-level fashion (or level order traversal)

Problems featuring Tree BFS pattern:
* Binary Tree Level Order Traversal (easy)
* Zigzag Traversal (medium)

## DFS
Tree DFS is based on the Depth First Search (DFS) technique to traverse a tree.
You can use recursion (or a stack for the iterative approach) to keep track of all the previous (parent) nodes while traversing.

The Tree DFS pattern works by starting at the root of the tree, if the node is not a leaf you need to do three things: Decide whether to process the current node now (pre-order), or between processing two children (in-order) or after processing both children (post-order). Make two recursive calls for both the children of the current node to process them.

How to identify the Tree DFS pattern:
* If you’re asked to traverse a tree with in-order, preorder, or postorder DFS
* If the problem requires searching for something where the node is closer to a leaf

Problems featuring Tree DFS pattern:
* Sum of Path Numbers (medium)
* All Paths for a Sum (medium)

## Two Heaps
In many problems, we are given a set of elements such that we can divide them into two parts. To solve the problem, we are interested in knowing the smallest element in one part and the biggest element in the other part. 
This pattern uses two heaps; A Min Heap to find the smallest element and a Max Heap to find the biggest element. At any time, the median of the current list of numbers can be calculated from the top element of the two heaps.

Ways to identify the Two Heaps pattern:
* Useful in situations like Priority Queue, Scheduling
* If the problem states that you need to find the smallest/largest/median elements of a set
* Sometimes, useful in problems featuring a binary tree data structure

Problems featuring
* Find the Median of a Number Stream (medium)

## Subsets
A huge number of coding interview problems involve dealing with Permutations and Combinations of a given set of elements. The pattern Subsets describes an efficient Breadth First Search (BFS) approach to handle all these problems.  
The pattern looks like this:
```
Given a set of [1, 5, 3]
Start with an empty set: [[]]
Add the first number (1) to all the existing subsets to create new subsets: [[], [1]];
Add the second number (5) to all the existing subsets: [[], [1], [5], [1,5]];
Add the third number (3) to all the existing subsets: [[], [1], [5], [1,5], [3], [1,3], [5,3], [1,5,3]].
```

How to identify the Subsets pattern:
* Problems where you need to find the combinations or permutations of a given set

Problems featuring Subsets pattern:
* Subsets With Duplicates (easy)
* String Permutations by changing case (medium)

## Modified binary search
Whenever you are given a sorted array, linked list, or matrix, and are asked to find a certain element, the best algorithm you can use is the Binary Search. This pattern describes an efficient way to handle all problems involving Binary Search.

The patterns looks like this for an ascending order set:
```
Find the middle of start and end. An easy way to find the middle would be: middle = (start + end) / 2. But this has a good chance of producing an integer overflow so it’s recommended that you represent the middle as: middle = start + (end — start) / 2
If the key is equal to the number at index middle then return middle
If ‘key’ isn’t equal to the index middle:
  if key < arr[middle], reduce your search to end = middle — 1
  if key > arr[middle], reduce your search to end = middle + 1
```

Problems featuring the Modified Binary Search pattern:
* Order-agnostic Binary Search (easy)
* Search in a Sorted Infinite Array (medium)

## Top k elements
Use a Heap

How to identify the Top ‘K’ Elements pattern:
* If you’re asked to find the top/smallest/frequent ‘K’ elements of a given set
* If you’re asked to sort an array to find an exact element

Problems featuring Top ‘K’ Elements pattern:
* Top ‘K’ Numbers (easy)
* Top ‘K’ Frequent Numbers (medium)

## K-way merge
Use a Heap.

Whenever you’re given ‘K’ sorted arrays, you can use a Heap to efficiently perform a sorted traversal of all the elements of all arrays. You can push the smallest element of each array in a Min Heap to get the overall minimum. After getting the overall minimum, push the next element from the same array to the heap. Then, repeat this process to make a sorted traversal of all elements.

The pattern looks like this:
* Insert the first element of each array in a Min Heap.
* After this, take out the smallest (top) element from the heap and add it to the merged list.
* After removing the smallest element from the heap, insert the next element of the same list into the heap.
* Repeat steps 2 and 3 to populate the merged list in sorted order.

How to identify the K-way Merge pattern:
* The problem will feature sorted arrays, lists, or a matrix
* If the problem asks you to merge sorted lists, find the smallest element in a sorted list.

Problems featuring the K-way Merge pattern:
Merge K Sorted Lists (medium)
K Pairs with Largest Sums (Hard)

## Topological sort
Topological Sort is used to find a linear ordering of elements that have dependencies on each other. For example, if event ‘B’ is dependent on event ‘A’, ‘A’ comes before ‘B’ in topological ordering.

1. Initialization
    1. Store the graph in adjacency lists by using a HashMap
    1. To find all sources, use a HashMap to keep the count of in-degrees. Build the graph and find in-degrees of all vertices.
2. Build the graph from the input and populate the in-degrees HashMap.
3. Find all sources
    1. All vertices with ‘0’ in-degrees will be sources and are stored in a Queue.
4. Sort
    1. For each source, do the following things:
        1. Add it to the sorted list.
        2. Get all of its children from the graph.
        3. Decrement the in-degree of each child by 1.
        4. If a child’s in-degree becomes ‘0’, add it to the sources Queue.
    2. Repeat (a), until the source Queue is empty.

How to identify the Topological Sort pattern:
* The problem will deal with graphs that have no directed cycles
* If you’re asked to update all objects in a sorted order
* If you have a class of objects that follow a particular order

Problems featuring the Topological Sort pattern:
* Task scheduling (medium)
* Minimum height of a tree (hard)