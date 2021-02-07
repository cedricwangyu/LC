# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None: return []
        layer, new, res = [root], [], []
        def gonextlayer():
            res.append(layer[-1].val)
            new.clear()
            for node in layer:
                if node.left: new.append(node.left)
                if node.right: new.append(node.right)
            layer.clear()
            layer.extend(new)
        while len(layer) > 0: gonextlayer()
        return res