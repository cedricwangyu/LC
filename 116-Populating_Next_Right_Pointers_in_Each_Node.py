"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def helper(node, lv, levs):
            if lv < len(levs):
                levs[lv].next = node
                levs[lv] = node
            else:
                levs.append(node)
            if node.left:
                helper(node.left, lv + 1, levs)
                helper(node.right, lv + 1, levs)
        
        if root:
            helper(root, 0, [])
        return root
    