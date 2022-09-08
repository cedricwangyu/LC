# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        def inorder(node=root):
            if node:
                inorder(node.left)
                self.res.append(node.val)
                inorder(node.right)
        
        inorder()
        return self.res