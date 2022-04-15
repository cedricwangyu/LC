# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        def flatten(node):
            if node is None: return []
            return flatten(node.left) + [node.val] + flatten(node.right)
        
        self.nums = flatten(root)
        self.idx = -1
        

    def hasNext(self) -> bool:
        if self.idx + 1 < len(self.nums): return True
        else: return False

    def next(self) -> int:
        self.idx += 1
        return self.nums[self.idx]

    def hasPrev(self) -> bool:
        if self.idx - 1 >= 0: return True
        else: return False
        

    def prev(self) -> int:
        self.idx -= 1
        return self.nums[self.idx]
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()