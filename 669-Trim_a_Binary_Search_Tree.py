# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int, prev = None) -> TreeNode:
        head = TreeNode(-1, None, None)
        def helper(node, prev):
            if node is None: return root
            if node.val < low: 
                node = node.right
                prev.left = node
                helper(node, prev)
            elif node.val > high:
                node = node.left
                prev.right = node
                helper(node, prev)
            else:
                if prev.val < 0: 
                    if prev.left: prev.left = node
                    else: prev.right = node
                helper(node.left, node)
                helper(node.right, node)
        
        helper(root, head)
        if head.left: return head.left
        else: return head.right
                
                
                
            
            
            
        