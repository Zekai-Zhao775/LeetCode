# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        list_node = []
        node = head
        head_new = Node(0)
        node_new = head_new
        list_node_new = []
        while node:
            list_node.append(node)
            node_new.val = node.val
            if node.next:
                node_next_new = Node(-1)
                node_new.next = node_next_new
                list_node_new.append(node_new)
                node_new = node_new.next
            else:
                node_new.next = None
                list_node_new.append(node_new)
                node_new = node_new.next
            node = node.next

        list_random = []
        for node in list_node:
            if node.random:
                list_random.append(list_node.index(node.random))
            else:
                list_random.append(-1)
        for i in range(len(list_random)):
            if list_random[i] == -1:
                list_node_new[i].random = None
            else:
                list_node_new[i].random = list_node_new[list_random[i]]

        return head_new