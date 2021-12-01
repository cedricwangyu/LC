"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head is None: 
            head = Node(insertVal)
            head.next = head
            return head
        node = head
        while True:
            if node.val <= insertVal <= node.next.val or node.next.val < node.val <= insertVal or insertVal <= node.next.val < node.val or node.next == head:
                node.next = Node(insertVal, node.next)
                return head
            node = node.next
