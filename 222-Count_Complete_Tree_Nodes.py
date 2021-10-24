# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def is_full(node):
            l, r = 0, 0
            t = node
            while t.left: t, l = t.left, l+1
            t = node
            while t.right: t, r = t.right, r+1
            return l, r
        self.res = 0
        def count(node):
            if node is None: return
            L, R = is_full(node)
            if L == R: self.res += 2 ** (L+1)-1
            else:
                self.res += 1
                count(node.left)
                count(node.right)
        count(root)
        return self.res
