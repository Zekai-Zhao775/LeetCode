# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # O(2n)
        # Count
        len = 0
        head_temp = head
        while head_temp:
            len += 1
            head_temp = head_temp.next
        print(len)
        # Find and delete
        head_temp = head
        dummy = ListNode(-1)
        dummy.next = head
        node_last = dummy
        i = 0

        while head_temp:
            if len - n - i == 0:
                node_last.next = head_temp.next
                break
            else:
                node_last = head_temp
                head_temp = head_temp.next
                i += 1

        return dummy.next