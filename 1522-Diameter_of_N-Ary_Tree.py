"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.res = 0
        def largestwo(L):
            if len(L) == 1: return [L[0]]
            res = [0, 0]
            for l in L:
                if l > res[0]: res[0], res[1] = l, res[0]
                elif res[0] >= l > res[1]: res[1] = l
            return res
        def depth(node):
            if len(node.children) == 0: return 0
            d = largestwo([depth(c) for c in node.children])
            if len(d) == 1: self.res = max(self.res, d[0]+1)
            else: self.res = max(self.res, sum(d)+2)
            return d[0] + 1
        d = depth(root)
        self.res = max(self.res, d)
        return self.res
