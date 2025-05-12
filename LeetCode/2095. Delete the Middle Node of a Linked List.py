# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # n = 0
        # node = head
        # while node != None:
        #     node = node.next
        #     n += 1
        # if n == 1:
        #     return None
        # # print(n)
        # # print(int(n / 2))
        # node = head
        # i = 0
        # while i < int(n / 2):
        #     if i == int(n / 2) - 1:
        #         node.next = node.next.next
        #     node = node.next
        #     i += 1
        # return head


        # fast-slow pointer
        if head.next == None:
            return None
        fast = head
        slow = head
        slow_last = None
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow_last = slow
            slow = slow.next
        slow_last.next = slow_last.next.next
        return head