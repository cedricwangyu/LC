# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.i = 0
        self.res = 0
        def inorder(node):
            if self.i > k: return
            if node is None: return
            inorder(node.left)
            self.i += 1
            if self.i == k: 
                self.res = node.val
                return
            inorder(node.right)
        
        inorder(root)
        return self.res