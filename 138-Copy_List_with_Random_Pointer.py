"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None: return None
        node = head
        while node is not None:
            node_next = node.next
            node.next = Node(node.val, node_next, None)
            node = node.next.next
        node = head
        while node is not None:
            if node.random is not None: node.next.random = node.random.next
            node_next = node.next.next
            if node.next.next: node.next.next = node.next.next.next
            node = node_next
        return head.next