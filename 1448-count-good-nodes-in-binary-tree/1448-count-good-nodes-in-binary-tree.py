# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #iterative approach
        st = [(root, float(-inf))]
        numGood = 0
        
        while st:
            node, prevMax = st.pop()
            
            if prevMax <= node.val:
                numGood += 1
            if node.left:
                st.append((node.left, max(node.val, prevMax)))
            if node.right:
                          st.append((node.right, max(node.val, prevMax)))
                          
        return numGood
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #recursive approach
#         def dfs(node, prevMax):
#             nonlocal numGood
#             if node:
#                 if node.left:
#                     if node.val <= node.left.val and node.left.val >= prevMax:
#                         print("numG updated at node val ", node.val)
#                         numGood += 1
#                         dfs(node.left, node.left.val)
#                     else:
#                         dfs(node.left, prevMax)
#                 if node.right:
#                     if node.val <= node.right.val and node.right.val >= prevMax:
#                         print("numG updated at node val ", node.val)
#                         numGood += 1
#                         dfs(node.right, node.right.val)
#                     else:
#                         dfs(node.right, prevMax)
#         numGood = 1
#         dfs(root, root.val)
            
#         return numGood