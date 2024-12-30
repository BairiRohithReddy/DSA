# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]: #type:ignore
        """
        Inverts a binary tree.

        This function takes the root of a binary tree and inverts it,
        swapping left and right children for each node recursively.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            Optional[TreeNode]: The root of the inverted binary tree.

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree (due to recursion stack).
        """

        def invertbintree(root):
            """
            Helper function to recursively invert the binary tree.

            Args:
                root (Optional[TreeNode]): The current node being processed.

            Returns:
                Optional[TreeNode]: The current node after inversion.
            """
            # Base case: if the node is None, return None (handles leaf nodes)
            if not root:
                return None

            # Swap the left and right children
            root.left, root.right = root.right, root.left

            # Recursively invert the left and right subtrees
            invertbintree(root.left)
            invertbintree(root.right)

            # Return the current node (now inverted)
            return root

        # Call the helper function with the root node
        return invertbintree(root)

'''
## Explanation of Edge Cases

1. **Empty Tree**: The base case `if not root: return None` handles the situation where the input tree is empty or when we reach a leaf node's child (which is None).

2. **Single Node Tree**: This case is implicitly handled. For a single node, the function will swap its None children and return the node unchanged.

3. **Unbalanced Tree**: The algorithm works correctly for unbalanced trees as it processes each node individually, regardless of the tree's structure.

## Asymptotic Analysis

### Time Complexity: O(n)
- The function visits each node in the tree exactly once.
- At each node, it performs a constant-time operation (swapping children).
- Therefore, the total time complexity is O(n), where n is the number of nodes in the tree.
- Note: While it's true that we're swapping n-1 nodes (excluding the root), in Big O notation, we simplify this to O(n) as constants are dropped.

### Space Complexity: O(h)
- The space complexity is determined by the maximum depth of the recursion stack.
- In the worst case (a completely unbalanced tree), this could be O(n).
- In a balanced tree, it would be O(log n).
- Generally, we express this as O(h), where h is the height of the tree.
- No additional data structures are used, so the extra space is solely due to the recursion stack.

This implementation efficiently inverts the binary tree with a clean, recursive approach, handling all edge cases and maintaining optimal time and space complexity for the problem.

'''