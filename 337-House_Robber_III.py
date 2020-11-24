# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node):
            r1, r2 = 0, 0
            if node.left: r1, r2 = helper(node.left)
            if node.right:
                t = helper(node.right)
                r1 += t[0]
                r2 += t[1]
            
            return r2, max(r2, r1 + node.val)
        if root is None: return 0
        return max(helper(root))
            
        