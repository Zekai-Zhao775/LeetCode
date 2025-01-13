# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        current_list1 = list1
        current_list2 = list2

        while current_list1 and current_list2:
            if current_list1.val <= current_list2.val:
                current.next = current_list1
                current_list1 = current_list1.next
            else:
                current.next = current_list2
                current_list2 = current_list2.next
            current = current.next

        while current_list1:
            current.next = current_list1
            current_list1 = current_list1.next
            current = current.next

        while current_list2:
            current.next = current_list2
            current_list2 = current_list2.next
            current = current.next

        return dummy.next