# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if head.next.next == None:
            return head.val + head.next.val
        num = []
        node = head
        count = 0
        while node != None:
            num.append(node.val)
            count += 1
            node = node.next
        max = 0
        temp = 0
        i = 0
        while i < (count / 2):
            temp = num[i] + num[-i - 1]
            if temp > max:
                max = temp
            i += 1
        return max