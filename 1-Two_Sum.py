
class Solution:
    def twoSum(self, nums, target):
        p = {}
        for i, n in enumerate(nums):
            r = target - n
            if r in p:
                return [p[r], i]
            else:
                p[n] = i
            