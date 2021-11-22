# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        self.found = False
        def dfs(node):
            if self.found: return node
            if node is None: return node
            if node.val == key:
                self.found = True
                if node.left is not None and node.right is not None:
                    tempnode = node.left
                    while tempnode.right: tempnode = tempnode.right
                    tempnode.right = node.right
                    return node.left
                elif node.left: return node.left
                else: return node.right
                
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return node
        return dfs(root)
