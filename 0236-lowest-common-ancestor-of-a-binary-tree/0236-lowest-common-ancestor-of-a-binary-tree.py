# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    
        #recursive approach
        def recurse_tree(current_node: TreeNode)-> bool:
            
            #if reached the end of a branch, return False
            if not current_node:
                return False
            
            #Left recursion
            left = recurse_tree(current_node.left)
            
            #Right recusion
            right = recurse_tree(current_node.right)
        
            #check for p or q
            mid = current_node == p or current_node == q
            
            #if any two of three flags left, right or mid become True
            if mid + left + right >= 2:
                self.ans = current_node
                
            #Return true if any flag is true
            return mid or left or right
        
        recurse_tree(root)
        return self.ans