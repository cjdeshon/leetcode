# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if head == None: return False
        
        #get middle
        p1 = p2 = head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        
        #reverse second half
        prev = None
        curr = p1
        while curr:
            nextTemp = curr.next
            curr.next = prev
            prev = curr 
            curr = nextTemp
        
        #calc max
        maxTwin = -9999
        curTwin = 0
        p1 = prev
        p2 = head
        while p1:
            currTwin = p1.val + p2.val
            maxTwin = max(maxTwin, currTwin)
            p1 = p1.next
            p2 = p2.next
            
        return maxTwin