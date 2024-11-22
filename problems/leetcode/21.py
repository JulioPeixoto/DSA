# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list = []
        n = ListNode()
        c = n
        while list1 and list2:
            if list1.val > list2.val:
                c.next = list2
                list2 = list2.next
            
            else:
                c.next = list1
                list1 = list1.next
            c = c.next
        
        if list1: c.next = list1 
        else: c.next = list2

        return n.next