# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0
        
    def convertBST(self, root: TreeNode) -> TreeNode:
        def helper(node):
            if node.right: helper(node.right)
            print(node.val)
            self.sum += node.val
            node.val = self.sum
            if node.left: helper(node.left)
        if root: helper(root)
        return root
            
        