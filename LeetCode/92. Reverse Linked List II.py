from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        # add aditional head
        head_addi = ListNode(0)
        head_addi.next = head

        # store node in list
        list_node = []
        node = head
        while node:
            list_node.append(node)
            node = node.next

        # edge case
        if len(list_node) == 0 or len(list_node) == 1:
            return head
        if left == right:
            return head

        # reverse
        if left == 1:
            head_reverse_list = head_addi
        else:
            head_reverse_list = list_node[left - 2]

        if right == len(list_node):
            tail_reverse_list = None
        else:
            tail_reverse_list = list_node[right]

        count_reverse = right - left + 1
        node = head_reverse_list
        i = 0
        while i < count_reverse:
            node.next = list_node[right - 1 - i]
            node = node.next
            i += 1
        node.next = tail_reverse_list

        return head_addi.next