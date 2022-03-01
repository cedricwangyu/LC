"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root is None: return
        new_root = Node()
        new_root.val = root.val
        new_root.children = [self.cloneTree(child) for child in root.children]
        return new_root
    