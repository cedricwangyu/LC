# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def bi(left, right):
            if left > right: return
            elif left == right: return TreeNode(nums[left])
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left, node.right = bi(left, mid-1), bi(mid+1, right)
            return node
        return bi(0, len(nums)-1)
