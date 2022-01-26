# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def get_list(node):
            if node is None: return []
            return get_list(node.left) + [node.val] + get_list(node.right)
        
        list1, list2, res = get_list(root1), get_list(root2), []
        while len(list1) > 0 and len(list2) > 0:
            if list1[0] < list2[0]: res.append(list1.pop(0))
            else: res.append(list2.pop(0))
        if len(list1) > 0: res += list1
        else: res += list2
        return res