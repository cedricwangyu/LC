from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        p = []
        for i in range(len(nums)):
            ind = bisect_left(p, nums[i])
            if ind == len(p): p.append(nums[i])
            else: p[ind] = nums[i]
        return len(p)