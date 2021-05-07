# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None: return None
        p = []
        while head:
            p.append(head.val)
            head = head.next
        def helper(node, i, j):
            m = (i+j)//2
            node.val = p[m]
            if m > i:
                node.left = TreeNode()
                helper(node.left, i, m-1)
            if m < j:
                node.right = TreeNode()
                helper(node.right, m+1, j)
        head = TreeNode()
        helper(head, 0, len(p)-1)
        return head