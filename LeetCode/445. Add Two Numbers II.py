# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverseListNode(l1)
        l2 = self.reverseListNode(l2)

        carry = 0
        p = l1
        q = l2
        tail = None

        sum = 0
        carry = 0

        while p and q:
            sum = p.val + q.val + carry
            p.val = sum % 10
            carry = sum // 10
            tail = p
            p = p.next
            q = q.next

        if q:
            tail.next = q
            p = q

        while p:
            sum = p.val + carry
            p.val = sum % 10
            carry = sum // 10

            tail = p
            p = p.next

        if carry == 1:
            tail.next = ListNode(1)

        return self.reverseListNode(l1)

    def reverseListNode(self, l) -> Optional[ListNode]:
        tail_temp = None
        next_temp = None

        while l:
            next_temp = l.next
            l.next = tail_temp
            tail_temp = l
            l = next_temp

        return tail_temp