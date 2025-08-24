from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



# fast slow pointers, O(n) time, O(1) space
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        fast = head
        slow = head
        while True:
            slow = slow.next
            fast = fast.next
            if fast == None:
                return False
            fast = fast.next
            if fast == None:
                return False
            if fast == slow:
                return True

# O(n) time, O(n) space
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         visited = set()
#         node = head
#         if node == None:
#             return False
#         while node.next:
#             if node in visited:
#                 return True
#             else:
#                 visited.add(node)
#                 node = node.next
#         return False