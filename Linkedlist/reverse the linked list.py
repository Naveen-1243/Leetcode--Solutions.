class Solution:
  def ReverseLinkedlist(self, head):
    if not head or not head.next:
      return head
    cur=head
    prev=None
    while cur:
      nxt=cur.next
      cur.next=prev
      prev=cur
      cur=nxt
    return prev

#difficulty : easy
#time complexity : O(n)
#space complexity : O(1)
