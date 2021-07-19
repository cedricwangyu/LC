# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        minval, maxval = min(p.val, q.val), max(p.val, q.val)
        def dfs(node):
            if node.val <= maxval and node.val >= minval: return node
            elif node.val < minval: return dfs(node.right)
            else: return dfs(node.left)
        return dfs(root)
