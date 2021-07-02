# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        self.res = []
        def add(index, val):
            if len(self.res) == index: self.res.append([val])
            else: self.res[index].append(val)
            return index
        def dfs(node):
            if node is None: return -1
            return add(max(dfs(node.left), dfs(node.right)) + 1, node.val)
        dfs(root)
        return self.res
