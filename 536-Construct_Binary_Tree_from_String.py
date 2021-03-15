# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.i = 0
    def str2tree(self, s: str) -> TreeNode:
        def helper(node):
            if self.i >= len(s): return
            curr = ""
            while self.i < len(s) and s[self.i] not in ['(',')']:
                curr += s[self.i]
                self.i += 1
            node.val = int(curr)
            if self.i < len(s) and s[self.i] is '(':
                self.i += 1
                node.left = TreeNode()
                helper(node.left)
                self.i += 1
            if self.i < len(s) and s[self.i] is '(':
                self.i += 1
                node.right = TreeNode()
                helper(node.right)
                self.i += 1
                
        head = TreeNode()
        if len(s) > 0: helper(head)
        else: head = None
        return head