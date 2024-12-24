# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #iterative
        while root is not None and root.val != val:
            root = root.left if val < root.val else root.right
        return root

        # # recursive
        # if root is None or val == root.val:
        #     return root

        # if val < root.val:
        #     return self.searchBST(root.left, val)
        
        # else:
        #     return self.searchBST(root.right, val)
            
            
            