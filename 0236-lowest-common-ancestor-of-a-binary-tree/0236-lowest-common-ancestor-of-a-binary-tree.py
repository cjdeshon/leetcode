# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def __init__(self):
    #     self.ans = None
    
    #Traversed Flags
    BOTH_PENDING = 2
    LEFT_DONE = 1
    BOTH_DONE = 0
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #stack approach
    
        stack = [(root,Solution.BOTH_PENDING)]
        
        one_node_found = False
        LCA_index = -1
        
        while stack:
            parent_node, parent_state = stack[-1]
            
            #if parent_state not equal to BOTH_DONE, do not pop
            if parent_state != Solution.BOTH_DONE:
                
                #if both child traversals are pending
                if parent_state == Solution.BOTH_PENDING:
                    
                    #check if current parent_node is either p or q
                    if parent_node == p or parent_node == q:
                        
                        if one_node_found:
                            return stack[LCA_index][0]
                        else:
                            one_node_found = True
                            #save current top index of stack for LCA
                            LCA_index = len(stack) - 1
                    #if both pending, traverse left first
                    child_node = parent_node.left
                else:
                    child_node = parent_node.right
                    
                #update node state at top of stack after visiting child
                stack.pop()
                stack.append((parent_node, parent_state - 1))
                
                #add child node to stack for traversal
                if child_node:
                    stack.append((child_node, Solution.BOTH_PENDING))
                    
            else:
                #parent_state of node is both done
                if one_node_found and LCA_index == len(stack) - 1:
                    LCA_index -= 1
                stack.pop()
                
        return None
                
    
#         #recursive approach
#         def recurse_tree(current_node: TreeNode)-> bool:
            
#             #if reached the end of a branch, return False
#             if not current_node:
#                 return False
            
#             #Left recursion
#             left = recurse_tree(current_node.left)
            
#             #Right recusion
#             right = recurse_tree(current_node.right)
        
#             #check for p or q
#             mid = current_node == p or current_node == q
            
#             #if any two of three flags left, right or mid become True
#             if mid + left + right >= 2:
#                 self.ans = current_node
                
#             #Return true if any flag is true
#             return mid or left or right
        
#         recurse_tree(root)
#         return self.ans