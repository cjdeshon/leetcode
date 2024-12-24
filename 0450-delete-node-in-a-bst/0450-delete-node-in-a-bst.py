# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def successor(self, root: TreeNode) -> int:
            root = root.right
            while root.left:
                root = root.left
            return root.val

    def predecessor(self, root: TreeNode) -> int:
        root = root.left
        while root.right:
            root = root.right
        return root.val
        
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        #recursive
        if not root:
            return None

        #delete right
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        #delete left
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        #delete current
        else:
            #leaf
            if not (root.left or root.right):
                root = None
            #right child
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            #left child
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)

        return root
        
        def inorder(root: Optional[TreeNode]) -> List:
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        

        