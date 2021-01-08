"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        whole, visited = set(), set()
        for node in tree:
            whole.add(node)
            visited.update(node.children)
        res = whole.difference(visited)
        return list(res)[0]