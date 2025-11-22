class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead1 ListNode类
# @param pHead2 ListNode类 
# @return ListNode类
#
class Solution:
    def Merge(self, pHead1: ListNode, pHead2: ListNode) -> ListNode:
        # write code here

        # O(1)space, in place modify

        # edge case
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1

        # iterate once, O(2n)
        node_1 = pHead1
        node_2 = pHead2
        dummy_head = ListNode(0)
        node = dummy_head

        while node_1 and node_2:
            if node_1.val <= node_2.val:
                node.next = node_1
                node_1 = node_1.next
                node = node.next
            else:
                node.next = node_2
                node_2 = node_2.next
                node = node.next

        if node_1:
            node.next = node_1
        else:
            node.next = node_2

        return dummy_head.next