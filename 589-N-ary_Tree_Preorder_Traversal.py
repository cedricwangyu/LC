"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.res = []
        def helper(root):
            if root is None: return
            self.res.append(root.val)
            for node in root.children: helper(node)
        helper(root)
        return self.res
