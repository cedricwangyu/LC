# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def helper(node):
            res = (node.val, node.val, 0)
            if node.left:
                res = helper(node.left)
                res = (min(res[0], node.val, res[0]), max(res[1], node.val, res[1]), max(res[2], abs(node.val - res[0]), abs(node.val - res[1]), res[2]))
            if node.right:
                R = helper(node.right)
                res = (min(R[0], node.val, res[0]), max(R[1], node.val, res[1]), max(R[2], abs(node.val - R[0]), abs(node.val - R[1]), res[2]))
            return res
        
        return helper(root)[2]