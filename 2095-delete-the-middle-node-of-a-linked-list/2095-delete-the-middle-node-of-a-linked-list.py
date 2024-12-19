# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        
        count = 0
        p1 = head
        p2 = head.next.next
        
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        
        p1.next = p1.next.next
        return head
        