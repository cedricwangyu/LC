# class Solution:
#     def findNumberOfLIS(self, nums: List[int]) -> int:
#         N = len(nums)
#         if N <= 1: return N
#         lengths = [0] * N
#         counts = [1] * N
#         for i in range(N):
#             for j in range(i + 1, N):
#                 if nums[j] > nums[i]:
#                     if lengths[i] >= lengths[j]:
#                         lengths[j] = lengths[i] + 1
#                         counts[j] = counts[i]
#                     elif lengths[j] == lengths[i] + 1:
#                         counts[j] += counts[i]
#         longest = max(lengths)
#         return sum([counts[i] for i in range(N) if lengths[i] == longest])


class Node(object):
    def __init__(self, start, end):
        self.range_left, self.range_right = start, end
        self._left = self._right = None
        self.val = 0, 1 #length, count
    @property
    def range_mid(self):
        return (self.range_left + self.range_right) // 2
    @property
    def left(self):
        self._left = self._left or Node(self.range_left, self.range_mid)
        return self._left
    @property
    def right(self):
        self._right = self._right or Node(self.range_mid + 1, self.range_right)
        return self._right

def merge(v1, v2):
    if v1[0] == v2[0]:
        if v1[0] == 0: return (0, 1)
        return v1[0], v1[1] + v2[1]
    return max(v1, v2)

def insert(node, key, val):
    if node.range_left == node.range_right:
        node.val = merge(val, node.val)
        return
    if key <= node.range_mid:
        insert(node.left, key, val)
    else:
        insert(node.right, key, val)
    node.val = merge(node.left.val, node.right.val)

def query(node, key):
    if node.range_right <= key:
        return node.val
    elif node.range_left > key:
        return 0, 1
    else:
        return merge(query(node.left, key), query(node.right, key))

class Solution(object):
    def findNumberOfLIS(self, nums):
        if not nums: return 0
        root = Node(min(nums), max(nums))
        for num in nums:
            length, count = query(root, num-1)
            insert(root, num, (length+1, count))
        return root.val[1]
        
        