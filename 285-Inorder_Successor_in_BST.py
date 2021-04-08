# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        self.status, self.res = -1, None
        def helper(node):
            if self.status > 0: return
            if node.left: helper(node.left)
            if self.status == 0: self.res, self.status = node, 1
            if node.val == p.val: self.status = 0
            if node.right: helper(node.right)
        
        helper(root)
        return self.res