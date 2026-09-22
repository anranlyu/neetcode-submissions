# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        point = dummy
        while l1 or l2:
            if l1:
                dummy.val += l1.val
                l1 = l1.next
            if l2:
                dummy.val += l2.val
                l2 = l2.next
            if dummy.val >= 10:
                if not dummy.next:
                    dummy.next = ListNode()
                
                dummy.next.val = dummy.val//10
                dummy.val = dummy.val%10
            if l1 or l2:
                if not dummy.next:
                    dummy.next = ListNode()
                dummy = dummy.next


        return point   
            
            
        
            
            
                