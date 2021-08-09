"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        self.res, self.i = [], 0
        def dfs(node):
            if node is None: return
            if len(self.res) <= self.i: self.res.append([])
            self.res[self.i].append(node.val)
            self.i += 1
            for c in node.children: dfs(c)
            self.i -= 1
        dfs(root)
        return self.res