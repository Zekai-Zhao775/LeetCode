class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @param m int整型
# @param n int整型
# @return ListNode类
#

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # write code here
        a = 1


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # write code here

        # edge case
        if m == n:
            return head

        # iterate once, reverse in place
        fake_head = ListNode(0)
        fake_head.next = head

        reverse_left = None  # head first, then tail
        reverse_right = None  # tail first, then head

        left_part_tail = None
        right_part_head = None

        node = fake_head
        next = None
        before = None
        curr = 0

        while node:
            if curr < m:
                before = node
                next = node.next
                node = next
                curr += 1
            elif curr == m:
                left_part_tail = before
                reverse_left = node
                next = node.next
                # connect later
                before = node
                node = next
                curr += 1
            elif curr > m and curr < n:
                # reverse in place
                next = node.next
                node.next = before
                before = node
                node = next
                curr += 1
            elif curr == n:
                reverse_right = node
                next = node.next
                right_part_head = next
                node.next = before
                before = node
                node = next
                curr += 1
            else:
                break
            # no need to iterate the rest

        # connect it
        left_part_tail.next = reverse_right
        reverse_left.next = right_part_head

        return fake_head.next