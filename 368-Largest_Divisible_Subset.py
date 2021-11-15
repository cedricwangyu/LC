class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        p, res, maximum = [[n] for n in nums], [nums[0]], 1
        for i, n in enumerate(nums):
            if len(p[i]) > maximum: res, maximum = p[i], len(p[i])
            for j in range(i+1, len(nums)):
                if nums[j] % n == 0 and len(p[j]) < len(p[i])+1: p[j] = p[i].copy() + [nums[j]]
        return res
