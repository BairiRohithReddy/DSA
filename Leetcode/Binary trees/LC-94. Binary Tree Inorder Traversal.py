# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]: #type:ignore
        """
        Perform an inorder traversal of a binary tree.

        Inorder traversal visits nodes in the order: left subtree, root, right subtree.

        Args:
        root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
        List[int]: A list of node values in inorder traversal order.

        Approach 1: Recursive
        ---------------------
        Idea:
        - Use a helper function to recursively traverse the tree.
        - Follow the inorder pattern: left subtree, current node, right subtree.
        - Append node values to a result list during traversal.

        Time Complexity: O(n), where n is the number of nodes in the tree.
        - Each node is visited exactly once.

        Space Complexity: O(h), where h is the height of the tree.
        - In the worst case (skewed tree), this can be O(n).
        - The space is used by the call stack during recursion.

        Pros: Simple and intuitive implementation.
        Cons: Can lead to stack overflow for very deep trees.

        Implementation:
        """
        result = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)
        inorder(root)
        return result

        """
        Approach 2: Iterative
        ---------------------
        Idea:
        - Use a stack to simulate the recursive process.
        - Traverse to the leftmost node, pushing all nodes along the way onto the stack.
        - Pop nodes from the stack, process them, and move to their right subtrees.

        Time Complexity: O(n), where n is the number of nodes in the tree.
        - Each node is pushed and popped once.

        Space Complexity: O(h), where h is the height of the tree.
        - In the worst case (skewed tree), this can be O(n).
        - The space is used by the stack.

        Pros: Avoids potential stack overflow issues of recursion.
        Cons: Slightly more complex implementation.

        Implementation:
        """
        # Uncomment and indent the following code to use the iterative approach
        # result = []
        # stack = []
        # current = root
        # while current or stack:
        #     while current:
        #         stack.append(current)
        #         current = current.left
        #     current = stack.pop()
        #     result.append(current.val)
        #     current = current.right
        # return result

