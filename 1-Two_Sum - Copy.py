# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.lev, self.d_lev, self.d_val= 0, 1, 0
        def helper(node):
            if self.lev == self.d_lev: self.d_val += node.val
            elif self.lev > self.d_lev: self.d_lev, self.d_val = self.lev, node.val
            self.lev += 1
            if node.left: helper(node.left)
            if node.right: helper(node.right)
            self.lev -= 1
        helper(root)
        return self.d_val