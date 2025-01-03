# definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sameTree(self, p: TreeNode, q: TreeNode) -> bool: # type: ignore
        """
        Determines if two binary trees are the same.

        Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

        Args:
            p (TreeNode): The root node of the first binary tree.
            q (TreeNode): The root node of the second binary tree.

        Returns:
            bool: True if the two binary trees are the same, False otherwise.

        Implementation Details:
        - The function uses a recursive approach to compare the two trees.
        - Base Cases:
            - If both nodes (p and q) are None, the trees are identical up to this point, so return True.
            - If one of the nodes is None and the other is not, the trees are not identical, so return False.
            - If the values of the current nodes (p.val and q.val) are not equal, the trees are not identical, so return False.
        - Recursive Case:
            - Recursively check the left subtree of both trees.
            - Recursively check the right subtree of both trees.
            - Both subtrees must be identical for the trees to be considered the same.

        Edge Cases:
        - Both trees are empty (p and q are both None).
        - One tree is empty, and the other is not.
        - Trees with different structures but the same node values.

        Asymptotic Analysis:
        - Time Complexity: O(N), where N is the number of nodes in the smaller tree. Each node is visited once.
        - Space Complexity: O(H), where H is the height of the tree. This space is used by the call stack during recursion. In the worst case (unbalanced tree), the height can be O(N).
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            # If the values of the current nodes are not equal, the trees are not identical
            return False
        return (self.sameTree(p.left.q.left) 
                and self.sameTree(p.right, q.right))