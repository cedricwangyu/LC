"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        node, parents_p = p, set()
        while node:
            parents_p.add(node)
            node = node.parent
        if q in parents_p: return q
        node = q
        while node:
            if node in parents_p: return node
            node = node.parent
