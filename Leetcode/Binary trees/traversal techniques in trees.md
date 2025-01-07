### Traversal Techniques in Trees *(BFS/ DFS)*

BFS --> Breadth First Search
DFS --> Depth First Search

- There are basically three types of Depth first search techniques they are as follows:

- DFS travels depth wise
    **1. Inorder Traversal (left Root Right)**: 
      - Here it means go to the extreme left subtree and apply the logic and then go to the extreme right subtree and apply the logic.
        Consider the example:
                       1
                    /    \ 
                   2      3
                  / \   /  \
                 4   5 6    7

        here the inorder traversal will give [4,2,5,1,6,3,7]
    **2. Pre-Order Traversal (Root Left Right)**:
      - Similarly here we start with root then the extreme left subtree (root, left, right) and then extreme right subtree (root, left, right)
      So for the same example above the pre-order traversal will be [1,2,4,5,3,6,7] 

    **3. Post-Order Traversal (Left Right Root)**:
       - Similarly here we start with left subtree then right subtree and then root.
       For the above example the post-order traversal will be [4,5,2,6,7,3,1]

**tip**: remember the naming convention based on the position of the root, in pre-order the root is first, in post order root is last and in inorder root is between left and right. also the right always follows left.


**BFS Breadth First Search**:
- BFS travels level wise

**Level-Order Traversal:**
   - Consider the below example:
   here the level order traversal will give [1,2,3,4,5,6,7]
            Example:
                       1
                    /     \ 
                   2       3
                  / \    /   \
                 4   5  6     7

    - for the first level we get 1
    - for the second level we get 2,3
    - for the third level we get 4,5,6,7

    > Inorder to print a level order traversal of a binary tree we need a queue data structure which will store the data level by level.
    > The queue will initially have root of the tree (1)
    > and inorder to store the values level by level we will use a list of list [[]].
    > Now check if the left of the root exists, if it exists then put it in the queue, and then check if right exists, if it does then put this right element in the queue.
    > Once both left and right are done, place the root in the list of lists, [[1]]
    > In the next iteration we take out 2 from the queue, and check if left of 2 exists then add this to the queue, similarly if right exists add it to the queue. Now do the same with 3 which is next after 2 in the queue.
    > once both 2 and 3 are checked for left and right and their elements are added to the queue, add 2 and 3 to the list of lists, [[1],[2,3]].
    > Repeat the same for 4,5,6,7 but here there are no left or right elements for these elements so we do not add anything to the queue but we add these values to the list of lists to store the level wise values.[[1],[2,3],[4,5,6,7]]. And once we checked for every value the queue will now be empty.
    > And we now have level wise values of the binary tree in the form of list of lists. 

**Iterative Pre-Order Traversal:**
> Preorder traversal is (Root Left Right)
> Here we can use stack to store the values of our binary tree, first we store the root and then pop it out after first iteration, then we store right and left of the root (as stack is First In Last Out), after second iteration we get left and then right element. 

**Iterative In-Order Traversal:**
> In-Order Traversal (Left Root Right)
>

**Iterative Post-Order Traversal:**
> Post-Order Traversal (Left Right Root)
> Here instead of a single stack we use 2 stacks
> In the first stack we will first push the first root, and then move it to second stack, then we check if the element has left and right elements, then we add them to the stack 1, now after second iteration we push the top of the stack 1 to stack 2 and check if left and right exists for this element if they do we add them to the stack 1
**to-do** code implementation of iterative pre-order traversal and level order traversal

Iterative traversal methods for binary trees are essential algorithms in computer science, offering efficient ways to visit all nodes without using recursion. Let's explore the iterative implementations of pre-order, in-order, and post-order traversals, with a focus on the post-order traversal using two stacks as shown in the image.

## Iterative Pre-Order Traversal (Root, Left, Right)

The pre-order traversal visits the root first, then the left subtree, and finally the right subtree. Here's how it works iteratively:

1. Create an empty stack and push the root node onto it.
2. While the stack is not empty:
   - Pop a node from the stack and process it (add to result).
   - If the node has a right child, push it onto the stack.
   - If the node has a left child, push it onto the stack.
3. Repeat step 2 until the stack is empty.

Example using the tree from the image:
```python
def iterative_preorder(root):
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result

# Result: [1, 2, 4, 5, 3, 6, 7, 8]
```

## Iterative In-Order Traversal (Left, Root, Right)

The in-order traversal visits the left subtree, then the root, and finally the right subtree:

1. Create an empty stack and set current to the root node.
2. While current is not None or the stack is not empty:
   - If current is not None:
     - Push current onto the stack.
     - Move to the left child (current = current.left).
   - Else:
     - Pop a node from the stack and process it.
     - Move to the right child (current = node.right).
3. Repeat step 2 until all nodes are processed.

Example using the tree from the image:
```python
def iterative_inorder(root):
    result = []
    stack = []
    current = root
    
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        result.append(current.val)
        current = current.right
    
    return result

# Result: [4, 2, 5, 1, 8, 7, 6, 3]
```

## Iterative Post-Order Traversal (Left, Right, Root)

The post-order traversal visits the left subtree, then the right subtree, and finally the root. The image shows a two-stack approach:

1. Create two stacks: stack1 and stack2.
2. Push the root onto stack1.
3. While stack1 is not empty:
   - Pop a node from stack1 and push it onto stack2.
   - If the node has a left child, push it onto stack1.
   - If the node has a right child, push it onto stack1.
4. After stack1 is empty, pop and process all nodes from stack2.

Example using the tree from the image:
```python
def iterative_postorder(root):
    if not root:
        return []
    
    result = []
    stack1 = [root]
    stack2 = []
    
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    
    while stack2:
        result.append(stack2.pop().val)
    
    return result

# Result: [4, 5, 2, 8, 7, 6, 3, 1]
```

The image [![iterative_post_order traversal example](<Iterative Post-order Traversal.jpg>)] illustrates this process, showing the contents of stack1 and stack2 at each step. The final result in stack2 represents the post-order traversal of the tree.

This two-stack method efficiently achieves post-order traversal without the need for complex node marking or parent pointers, making it a popular choice for iterative implementations.
