# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        prev=None
        slow=head
        fast=head
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=None

        left = self.sortList(head)
        right = self.sortList(slow)

        return self.merge(left, right)
    
    def merge(self, left, right):
        dummy = ListNode()
        cur=dummy
        while left and right:
            if left.val<=right.val:
                cur.next=left
                left=left.next
            else:
                cur.next=right
                right=right.next

            cur=cur.next
            
        if left:
            cur.next=left
        if right:
            cur.next=right
        
        return dummy.next