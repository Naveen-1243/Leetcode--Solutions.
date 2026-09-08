# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy=ListNode(0,head)
        prev=dummy
        for _ in range(left-1):
            prev=prev.next
        
        first=prev.next
        
        second=first
        for _ in range(right-left):
            second=second.next
        
        after=second.next

        cur=first
        x=after
        while cur != after:
            nxt=cur.next
            cur.next=x
            x=cur
            cur=nxt
        prev.next=second
        return dummy.next