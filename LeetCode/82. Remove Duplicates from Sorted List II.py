# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list_node = []
        node = head
        last_num = None
        last_num_index = 0
        remove_index = set()
        while node:
            if last_num == None:
                last_num = node.val
                last_num_index = len(list_node)
                list_node.append(node)
                node = node.next
            else:
                if node.val == last_num:
                    list_node.append(node)
                    node = node.next
                else:
                    curr_index = len(list_node)
                    if curr_index - last_num_index > 1:
                        for i in range(last_num_index, curr_index):
                            remove_index.add(i)
                    last_num = node.val
                    last_num_index = len(list_node)
                    list_node.append(node)
                    node = node.next
        if last_num_index != len(list_node) - 1:
            for i in range(last_num_index, len(list_node)):
                remove_index.add(i)

        # instead remove we build
        build_index = []
        for i in range(len(list_node)):
            if i not in remove_index:
                build_index.append(i)

        head_additional = ListNode(0)
        head_additional.next = head
        node = head_additional
        for i in build_index:
            node.next = list_node[i]
            node = node.next
        node.next = None

        return head_additional.next