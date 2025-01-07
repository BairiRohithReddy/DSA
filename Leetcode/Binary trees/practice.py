# binary trees representation in python
# binary trees can be constructed using linkedlists where the left of a node points to its left child and its right points to its right child.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)        
        else:
            self._recursive_insert(self.root, value)
    
    def _recursive_insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = TreeNode(value)
            else:
                self._recursive_insert(current_node.left, value)
        elif value >= current_node.value:
            # when the given value is equal to the current_node
            # adding this node to the right of the current node
            if current_node.right is None:
                current_node.right = TreeNode(value)
            else:
                self._recursive_insert(current_node.right, value)
    
    def pre_order_traversal(self, root):
        #pre_order-traversal (root left right)
        if root is None:
            return
        print(root.value)
        self.pre_order_traversal(root.left)
        self.pre_order_traversal(root.right)
        
    def post_order_traversal(self, root):
        # post_order-traversal (left right root)
        if root is None:
            return
        self.post_order_traversal(root.left)
        self.post_order_traversal(root.right)
        print(root.value)
    
    def in_order_traversal(self, root):
        # in_order-traversal (left root right)
        if root is None:
            return
        self.in_order_traversal(root.left)
        print(root.value)
        self.in_order_traversal(root.right)
        
    def search(self, root, value):
        pass
    
    def delete(self, root, value):
        pass
        