# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def helper(node):
            if node.left is None and node.right is None: return node, node
            
            L = R = node
            if node.left:
                L, r = helper(node.left)
                r.right = node
            if node.right:
                l, R = helper(node.right)
                node.right = l
            node.left = None
            return L, R
        
        res, _ = helper(root)
        return res
    
    
            
        