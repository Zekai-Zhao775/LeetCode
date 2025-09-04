# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        list_node_front = []
        list_node_end = []
        node = head
        while node:
            if node.val < x:
                list_node_front.append(node)
            else:
                list_node_end.append(node)
            node = node.next

        dummy_head = ListNode(0)
        dummy_head.next = head

        node = dummy_head
        for i in range(len(list_node_front)):
            node.next = list_node_front[i]
            node = node.next
        # current node: list_node_front[-1]
        for i in range(len(list_node_end)):
            node.next = list_node_end[i]
            node = node.next
        node.next = None

        return dummy_head.next
