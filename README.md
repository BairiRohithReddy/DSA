---

# Algorithms and Data Structures

### My notes on concepts covering algorithms and data structures, as well as solved Leetcode problems.

<p align="center">
    <a href="#introduction-to-data-structures">Introduction to Data Structures</a> •
    <a href="#trees">Trees</a> •
    <a href="#graphs">Graphs</a> •
    <a href="#introduction-to-algorithms">Introduction to Algorithms</a> •
    <a href="#sorting-algorithms">Sorting Algorithms</a> •
    <a href="#search-algorithms">Search Algorithms</a> •
    <a href="#greedy-algorithms">Greedy Algorithms</a> •
    <a href="#dynamic-programming">Dynamic Programming</a> •
    <a href="#other-algorithms">Other Algorithms</a> •
    <a href="#leetcode-explanation">Leetcode Explanation</a>
</p>

---

## Introduction to Data Structures
<p align="center">
    <a href="#basics">Basics</a> •
    <a href="#stacks">Stacks</a> •
    <a href="#queues">Queues</a> •
    <a href="#linked-list">Linked List</a> •
    <a href="#hash-tables">Hash Tables</a> •
    <a href="#heaps">Heaps</a>
</p>

### [Basics](#basics)
- Data structures are essential for organizing and manipulating data efficiently.
- Common data structures include **arrays**, **linked lists**, **stacks**, **queues**, **hash tables**, **heaps**, **trees**, and **graphs**.

### [Stacks](#stacks)
- Stacks follow the **Last In, First Out (LIFO)** principle. Operations include push, pop, and peek.
- Common applications: Undo functionality, expression evaluation, depth-first search.

### [Queues](#queues)
- Queues follow the **First In, First Out (FIFO)** principle. Operations include enqueue and dequeue.
- Common applications: Breadth-first search, handling asynchronous data (like message queues).

### [Linked List](#linked-list)
- A linked list is a linear collection where each element points to the next one. It can be singly or doubly linked.
- Common operations: Insertion, deletion, traversal.

---

## Introduction to Algorithms
<p align="center">
    <a href="#sorting-algorithms">Sorting Algorithms</a> •
    <a href="#search-algorithms">Search Algorithms</a> •
    <a href="#greedy-algorithms">Greedy Algorithms</a> •
    <a href="#dynamic-programming">Dynamic Programming</a>
</p>

### [Sorting Algorithms](#sorting-algorithms)
- Algorithms used to arrange data in a specific order (ascending/descending).
- Examples: **Bubble Sort**, **Quick Sort**, **Merge Sort**.

### [Search Algorithms](#search-algorithms)
- Algorithms used to locate a specific element within a data structure.
- Examples: **Binary Search**, **Breadth-First Search**, **Depth-First Search**.

### [Greedy Algorithms](#greedy-algorithms)
- Algorithms that make the locally optimal choice at each step with the hope of finding the global optimum.
- Examples: **Kruskal's Algorithm**, **Prim's Algorithm**.

### [Dynamic Programming](#dynamic-programming)
- A method for solving problems by breaking them down into simpler subproblems and storing the solutions to subproblems to avoid redundant work.
- Examples: **Knapsack Problem**, **Fibonacci Sequence**.

---

## Leetcode Explanation
<p align="center">
    <a href="#easy-problems">Easy Problems</a> •
    <a href="#medium-problems">Medium Problems</a> •
    <a href="#hard-problems">Hard Problems</a>
</p>

### [Easy Problems](#easy-problems)

- **Happy Number (LC-202)**  
    - Problem: Determine if a number is a happy number.  
    - Solution: Check if the sum of the squares of the digits eventually leads to 1 or loops.  
    - [File: `happy_numberLC(202).py`](./happy_numberLC(202).py)

- **Add Digits (LC-258)**  
    - Problem: Given a number, repeatedly add its digits until a single-digit result is obtained.  
    - Solution: Use the formula for the digital root, i.e., n % 9.  
    - [File: `addDigitsLC(258).py`](./addDigitsLC(258).py)

### [Medium Problems](#medium-problems)

- **Cycle in a Linked List (LC-141)**  
    - Problem: Detect if a linked list has a cycle.  
    - Solution: Use Floyd’s Tortoise and Hare algorithm to detect a cycle.  
    - [File: `LC(141).py`](./LC(141).py)

### [Hard Problems](#hard-problems)

---

## Additional Information

### [Single Linked List Implementation](#single-linked-list-implementation)
- A basic implementation of a singly linked list in Python that includes operations like insertion at head, insertion at tail, and deletion.
- [File: `singlelinkedlist.py`](./singlelinkedlist.py)

### [Square Root of x (LC-69)](#square-root-of-x)
- Problem: Compute the square root of a non-negative integer `x` without using the `sqrt` function.
- Solution: Use binary search to find the square root.  
- [File: `sqrt(x).py`](./sqrt(x).py)

---
