# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        reordered = self.reorder(head)

        dummy = ListNode(0, reordered)
        prev = dummy
        while n > 1:
            prev = prev.next
            n -= 1
        # prev now sits on the node BEFORE the target
        prev.next = prev.next.next

        return self.reorder(dummy.next)
        
        
    def reorder(self, head):
        prev, cur = None , head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev