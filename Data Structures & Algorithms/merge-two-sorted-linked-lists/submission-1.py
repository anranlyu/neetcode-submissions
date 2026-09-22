# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = list1

        if not list1 and not list2:
            return cur
        elif not list1:
            return list2
        elif not list2:
            return list1
        else:
            if list1.val >= list2.val:
                cur = list2
                cur.next = self.mergeTwoLists(list1,list2.next)
            else:
                cur = list1
                cur.next = self.mergeTwoLists(list1.next,list2)
        return cur
                
        