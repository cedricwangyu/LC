# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        info = []
        def helper(node, lev):
            if lev >= len(info): info.append([node.val, 1])
            else: 
                info[lev][0] += node.val
                info[lev][1] += 1
            if node.left: helper(node.left, lev + 1)
            if node.right: helper(node.right, lev + 1)
        
        helper(root, 0)
        return [item[0] / item[1] for item in info]