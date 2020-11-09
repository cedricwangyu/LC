# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def helper(root):
            if root.left is None and root.right is None:
                return root.val, 0
            
            if root.left: L = helper(root.left)
            else: L = (0, 0)
            
            if root.right: R = helper(root.right)
            else: R = (0, 0)
            
            
            return L[0] + R[0] + root.val, L[1] + R[1] + abs(L[0] - R[0])
        
        if root: res = helper(root)
        else: res = (0, 0)
        return res[1]
                