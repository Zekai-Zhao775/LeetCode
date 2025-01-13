from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ugly
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        current_l1 = l1
        current_l2 = l2
        last_l1_temp = None
        last_l2_temp = None

        while current_l1 and current_l2:
            sum = current_l1.val + current_l2.val + carry
            if sum < 10:
                current_l1.val = sum
                carry = 0
            elif sum >= 10:
                current_l1.val = sum - 10
                carry = 1
            last_l1_temp = current_l1
            current_l1 = current_l1.next
            last_l2_temp = current_l2
            current_l2 = current_l2.next

        return_flag = 1

        if current_l2:
            last_l1_temp.next = current_l2
            return_flag = 2

        while current_l1:
            sum = current_l1.val + carry
            if sum < 10:
                current_l1.val = sum
                carry = 0
                break
            elif sum >= 10:
                current_l1.val = sum - 10
                carry = 1
            last_l1_temp = current_l1
            current_l1 = current_l1.next

        while current_l2:
            sum = current_l2.val + carry
            if sum < 10:
                current_l2.val = sum
                carry = 0
                break
            elif sum >= 10:
                current_l2.val = sum - 10
                carry = 1
            last_l2_temp = current_l2
            current_l2 = current_l2.next

        if return_flag == 1:
            if carry == 1:
                last_l1_temp.next = ListNode(1)
            return l1
        else:
            if carry == 1:
                last_l2_temp.next = ListNode(1)
            return l1

# Optimized
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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

        return l1