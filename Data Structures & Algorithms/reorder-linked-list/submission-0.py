class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        pre, cur = None, second

        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        first, second = head, pre

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
            
            
            
        
        



        