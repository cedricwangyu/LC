# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.p = 0
        def dfs(node):
            if node is None: return (0, 0)
            l, r = dfs(node.left), dfs(node.right)
            res = (l[0] + r[0] + node.val, l[1] + r[1] + 1)
            self.p = max(self.p, res[0] / res[1])
            return res
        dfs(root)
        return self.p
