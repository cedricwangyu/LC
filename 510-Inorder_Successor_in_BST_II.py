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
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        if node.right:
            res = node.right
            while res.left:
                res = res.left
            return res
        else:
            res = node
            while res.parent:
                if res.parent.left is res: 
                    return res.parent
                res = res.parent
            