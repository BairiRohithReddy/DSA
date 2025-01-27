class Solution:
    # using a helper function
    def isMirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val ==right.val
                and self.isMirror(left.left==self.isMirror(right.right))
                and self.isMirror(left.right==self.isMirror(right.left)))
        
    def isSymmetric(self, root: TreeNode) -> bool:  #type:ignore
        if not root:
            return True
        return self.isMirror(root.left, root.right)
'''

intution:
# here we are using a helper function to check if the left and right subtrees are mirror images of each other.
# if both left and right are None, then they are mirror images.
# if one of them is None, then they are not mirror images.
# if the values of left and right are not equal, then they are not mirror images.
# if the values of left and right are equal, then we check if the left subtree of left is mirror image of the right subtree of right and vice versa.
# we are using recursion to check if the left and right subtrees are mirror images of each other.
# time complexity: O(n)
# space complexity: O(n)

'''
#using queue

def isSymmetric(self, root: TreeNode) -> bool: #type:ignore
        if not root:
            return True
        queue = [root.left, root.right]
        while queue:
            left = queue.popleft()
            right = queue.popleft()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True
    