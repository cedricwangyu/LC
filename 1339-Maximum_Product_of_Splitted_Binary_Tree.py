# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.sums = set()
        def helper(node):
            if node is None: res = 0
            else: res = node.val + helper(node.left) + helper(node.right)
            self.sums.add(res)
            return res
        total, res = helper(root), 0
        for n in self.sums: res = max(res, n * (total - n))
        return res % (10**9+7)