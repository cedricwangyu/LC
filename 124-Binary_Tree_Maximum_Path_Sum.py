# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float("-Inf")
        def helper(node=root):
            if node is None: return 0
            left, right = helper(node.left), helper(node.right)
            left = left if left > 0 else 0
            right = right if right > 0 else 0
            res = node.val + left + right
            self.res = self.res if res <= self.res else res
            return left + node.val if left > right else right + node.val

        helper()
        return self.res