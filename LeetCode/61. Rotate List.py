# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        list_node = []
        node = head
        while node:
            list_node.append(node)
            node = node.next

        if k == 0:
            return head
        if len(list_node) == 0:
            return None
        if len(list_node) == 1:
            return head
        k = k % len(list_node)
        if k == 0:
            return head

        dummy_head = ListNode(0)
        dummy_head.next = head

        first_head = list_node[len(list_node) - k]
        first_tail = list_node[-1]
        second_head = list_node[0]
        second_tail = list_node[len(list_node) - k - 1]

        dummy_head.next = first_head
        first_tail.next = second_head
        second_tail.next = None

        return dummy_head.next