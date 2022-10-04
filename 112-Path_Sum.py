# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.curr_val = 0
        
        def dfs(node=root):
            if node:
                self.curr_val += node.val
                if self.curr_val == targetSum and node.left is None and node.right is None:
                    return True
                if dfs(node.left): return True
                if dfs(node.right): return True
                self.curr_val -= node.val
                
            return False
        
        return dfs()