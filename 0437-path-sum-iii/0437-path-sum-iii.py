# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def preorder(node: TreeNode, curr_sum) -> None:
            nonlocal count
            if not node: return
            
            #update current sum
            curr_sum += node.val
            
            #check if target found
            if curr_sum == k:
                count += 1
                
            #check if subtree target found
            count += h[curr_sum -k]
            
            #add current sum to hashmap
            h[curr_sum] += 1
            
            #process children
            preorder(node.left, curr_sum)
            preorder(node.right, curr_sum)
            
            #remove curr_sum from hashmap to avoid parallel processing
            h[curr_sum] -= 1
            
        count, k = 0, targetSum
        h = defaultdict(int)
        preorder(root,0)
        return count