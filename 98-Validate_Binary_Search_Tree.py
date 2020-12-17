# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode, low = None, high = None) -> bool:
        if low and root.val <= low: return False
        if high and root.val >= high: return False
        if root.left and (root.left.val >= root.val or not self.isValidBST(root.left, low, root.val)): return False
        if root.right and (root.right.val <= root.val or not self.isValidBST(root.right, root.val, high)): return False
        return True
        