# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        if list1.val <= list2.val:
            node1 = list1
            node2 = list2
        else:
            node1 = list2
            node2 = list1

        result = ListNode(0)
        result_head = result

        while node1 or node2:
            if node1 == None:
                result.next = node2
                result = result.next
                node2 = node2.next
            elif node2 == None:
                result.next = node1
                result = result.next
                node1 = node1.next
            else:
                if node1.val < node2.val:
                    result.next = node1
                    result = result.next
                    node1 = node1.next
                else:
                    result.next = node2
                    result = result.next
                    node2 = node2.next
        return result_head.next

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode()
#         current = dummy

#         current_list1 = list1
#         current_list2 = list2

#         while current_list1 and current_list2:
#             if current_list1.val <= current_list2.val:
#                 current.next = current_list1
#                 current_list1 = current_list1.next
#             else:
#                 current.next = current_list2
#                 current_list2 = current_list2.next
#             current = current.next

#         while current_list1:
#             current.next = current_list1
#             current_list1 = current_list1.next
#             current = current.next

#         while current_list2:
#             current.next = current_list2
#             current_list2 = current_list2.next
#             current = current.next

#         return dummy.next