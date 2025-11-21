class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @return ListNode类
#


class Solution:
    def ReverseList(self, head: ListNode) -> ListNode:
        # write code here
        # edge case, no optional in input and output
        # if head == None:
        #     return None

        # reverse in place
        node = head
        prev = None
        temp = None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp

        return prev