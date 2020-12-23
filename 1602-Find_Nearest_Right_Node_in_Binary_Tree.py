# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.target_lev = None
        
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        def helper(node, curr_lev):
            if node:
                if curr_lev == self.target_lev: return node
                elif node.val == u.val:
                    self.target_lev = curr_lev
                    return None
                res = helper(node.left, curr_lev + 1)
                if res: return res
                res = helper(node.right, curr_lev + 1)
                if res: return res
            else:
                return None
        
        res = helper(root, 1)
        return res
                