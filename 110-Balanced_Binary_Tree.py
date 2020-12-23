# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(node):
            if node:
                left = helper(node.left)
                right = helper(node.right)
                print(left, right, abs(left - right) <= 1)
                if left > 0 and right > 0 and abs(left - right) <= 1: return max(left, right) + 1
                else: return False
            else: return 1
        
        res = helper(root)
        return res > 0