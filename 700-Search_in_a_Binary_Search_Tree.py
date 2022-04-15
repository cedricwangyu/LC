# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        while True:
            if node.val == val: return node
            elif node.val < val and node.right:
                node = node.right
            elif node.val > val and node.left:
                node = node.left
            else:
                return None