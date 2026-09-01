# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def rotate(head):
            if not head or head.next is None:
                return head
            
            second_last=head
            last=None
            while second_last.next.next is not None:
                second_last=second_last.next
            
            last=second_last.next
            last.next=head
            second_last.next=None
        
            return last
        
        if not head or head.next is None:
            return head
        
        count=0
        cur=head
        while cur:
            count+=1
            cur=cur.next
        
        k=k%count
        
        while k>0:
            head=rotate(head)
            k-=1
        
        return head
        
        