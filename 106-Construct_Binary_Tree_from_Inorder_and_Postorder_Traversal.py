# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def rc(li, lp, l):
            if l <= 0: return None
            root_val = postorder[lp+l-1]
            root_ind = inorder[li:li+l].index(root_val) + li
            return TreeNode(root_val, rc(li, lp, root_ind-li), rc(root_ind+1, lp+root_ind-li, l-root_ind+li-1))
        return rc(0, 0, len(inorder))
