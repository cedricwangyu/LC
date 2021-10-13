# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.i = 1
        def helper(node, l, r):
            if self.i >= len(preorder): return
            if preorder[self.i] <= node.val:
                node.left, self.i = TreeNode(preorder[self.i]), self.i+1
                helper(node.left, l, node.val)
            if self.i >= len(preorder): return
            if node.val < preorder[self.i] <= r:
                node.right, self.i = TreeNode(preorder[self.i]), self.i+1
                helper(node.right, node.val, r)
            
        root = TreeNode(preorder[0])
        helper(root, float('-Inf'), float('Inf'))
        return root
