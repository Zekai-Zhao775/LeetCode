# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(n) space O(n) time
        if head == None:
            return head
        if head.next == None:
            return head
        oddNodeHead = None
        oddNodeTail = None
        evenNodeHead = None
        evenNodeTail = None
        node = head
        node_last = node
        # O(n)
        count = 1
        while node != None:
            # evenNode
            if count % 2 == 0:
                if evenNodeHead == None:
                    evenNodeHead = node
                    evenNodeTail = node
                else:
                    evenNodeTail.next = node
                    evenNodeTail = node
            else:
                if oddNodeHead == None:
                    oddNodeHead = node
                    oddNodeTail = node
                else:
                    oddNodeTail.next = node
                    oddNodeTail = node
            node = node.next
            count += 1
        oddNodeTail.next = evenNodeHead
        evenNodeTail.next = None
        return oddNodeHead
