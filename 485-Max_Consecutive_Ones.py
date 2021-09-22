class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, curr = 0, 0
        for n in nums:
            if n == 1: curr += 1
            else: res, curr = max(res, curr), 0
        res = max(res, curr)
        return res
