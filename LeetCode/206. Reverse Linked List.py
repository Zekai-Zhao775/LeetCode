from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Memory Limit Exceeded
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         listnode_list = []
#         while head:
#             listnode_list.append(head)
#             head = head.next

#         i = len(listnode_list) - 1
#         dummy = ListNode(-1)
#         dummy.next = listnode_list[i]
#         while i > 0:
#             listnode_list[i].next = listnode_list[i - 1]
#             i -= 1

#         return dummy.next

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         node_next_temp = ListNode(-1)
#         node_before_temp = None
#         current = head
#
#         while current:
#             # store current next
#             node_next_temp = current.next
#             # change current next to before
#             current.next = node_before_temp
#             node_before_temp = current
#             # move current to current next
#             current = node_next_temp
#
#         return node_before_temp


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(n) time, O(n) space
        # if head == None:
        #     return head
        # if head.next == None:
        #     return head
        # node = head
        # nodeList = []
        # while node != None:
        #     nodeList.append(node)
        #     node = node.next
        # i = len(nodeList) - 1
        # while i > 0:
        #     nodeList[i].next = nodeList[i - 1]
        #     i -= 1
        # nodeList[0].next = None
        # return nodeList[-1]

        # O(n) time, O(1) space
        if head == None:
            return head
        if head.next == None:
            return head
        node = head.next
        node_last = head
        node_next = None
        while node != None:
            node_next = node.next
            node.next = node_last
            node_last = node
            node = node_next
        head.next = None
        return node_last