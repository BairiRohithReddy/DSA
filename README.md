## About This Repository

This repository contains my personal work on algorithms, data structures, and LeetCode problems. While the code implementations are my own original work, I've utilized Large Language Models (LLMs) in the following ways:

1. To explain and refine my approach to problems
2. To assist in documenting the solutions
3. To help structure and format the explanations

This methodology allows me to leverage AI as a learning and documentation tool while ensuring that the problem-solving and coding remain my own work. My goal is to create a comprehensive resource that reflects my learning journey while benefiting from AI-assisted explanation and documentation.

I want to be clear that while the documentation and explanations have been enhanced with the help of LLMs, the code solutions are my own implementations. This approach combines personal effort with AI assistance to create a more robust and well-documented learning resource.

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


- **Happy Number (LC-202)**  
    - Problem: Determine if a number is a happy number.  
    - Solution: Check if the sum of the squares of the digits eventually leads to 1 or loops.  
    - [File: `happy_numberLC(202).py`](./happy_numberLC(202).py)

- **Add Digits (LC-258)**  
    - Problem: Given a number, repeatedly add its digits until a single-digit result is obtained.  
    - Solution: Use the formula for the digital root, i.e., `n % 9`.  
    - [File: `addDigitsLC(258).py`](./addDigitsLC(258).py)


- **Cycle in a Linked List (LC-141)**  
    - Problem: Detect if a linked list has a cycle.  
    - Solution: Use Floyd’s Tortoise and Hare algorithm to detect a cycle.  
    - [File: `LC(141).py`](./LC(141).py)

- **Remove Nth Node From End of List (LC-19)**  
    - Problem: Remove the nth node from the end of the list.  
    - Solution: Use two pointers to determine the position of the node to be removed.  
    - [File: `LC(19).py`](./LC(19).py)

- **Merge Two Sorted Lists (LC-21)**  
    - Problem: Merge two sorted linked lists into one sorted list.  
    - Solution: Use a dummy node to build the merged list by comparing nodes.  
    - [File: `LC(21).py`](./LC(21).py)

- **Middle of the Linked List (LC-876)**  
    - Problem: Find the middle node of a linked list.  
    - Solution: Use two pointers to find the middle by moving one pointer two steps at a time and the other one step at a time.  
    - [File: `LC(876).py`](./LC(876).py)


- **Square Root of x (LC-69)**  
    - Problem: Compute the square root of a non-negative integer `x` without using the `sqrt` function.  
    - Solution: Use binary search to find the square root.  
    - [File: `sqrt(x).py`](./sqrt(x).py)

---

### [Single Linked List Implementation](#single-linked-list-implementation)
- A basic implementation of a singly linked list in Python that includes operations like insertion at head, insertion at tail, and deletion.
- [File: `singlelinkedlist.py`](./singlelinkedlist.py)

---  
