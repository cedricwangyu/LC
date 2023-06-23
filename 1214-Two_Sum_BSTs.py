# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        self.p = set()
        self.target = target
        def dfs(node, set_mode):
            if node:
                if set_mode:
                    self.p.add(self.target - node.val)
                    dfs(node.left, True)
                    dfs(node.right, True)
                else:
                    if node.val in self.p:
                        return True
                    else:
                        return dfs(node.left, False) or dfs(node.right, False)
            return False
                
            
        dfs(root1, True)
        return dfs(root2, False)
