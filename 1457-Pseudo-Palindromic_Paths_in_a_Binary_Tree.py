# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        def setnot(val, odds):
            if val in odds: odds.remove(val)
            else: odds.add(val)
        def helper(node, odds):
            setnot(node.val, odds)
            if node.left is None and node.right is None and len(odds) <= 1:
                self.res += 1
            if node.left: setnot(helper(node.left, odds), odds)
            if node.right: setnot(helper(node.right, odds), odds)
            return node.val
        
        helper(root, set())
        return self.res
                
                
            
                
        
        