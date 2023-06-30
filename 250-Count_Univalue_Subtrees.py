# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        self.res = 0
        def helper(node=root):
            val1, val2 = node.val, node.val
            if node.left:
                val1 = helper(node.left)
            if node.right:
                val2 = helper(node.right)
            if val1 is None or val2 is None or (val1 != node.val) or (val2 != node.val):
                return None
            else:
                self.res += 1
                return node.val
        
        helper()
        return self.res
            
            