# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        queue = deque( [root,])
        rightside = []
        
        while queue:
            level_length = len(queue)
            
            for i in range(level_length):
                node = queue.popleft()

                #if rightmost
                if i == level_length-1:
                    rightside.append(node.val)

                #add child nodes 
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return rightside
        
        
        
#         if root is None:
#             return []
        
#         next_level = deque([root,])
#         rightside = []
        
#         while next_level:
#             #prep for next level
#             curr_level = next_level
#             next_level = deque()
            
#             while curr_level:
#                 node = curr_level.popleft()
                
#                 #add children
#                 if node.left:
#                     next_level.append(node.left)
#                 if node.right:
#                     next_level.append(node.right)
                    
#             #current level finished add next level rightmost element
#             rightside.append(node.val)
            
#         return rightside