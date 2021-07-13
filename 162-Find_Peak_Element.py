class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def direct(i):
            if i == 0: return 2 if nums[1] > nums[0] else 0
            elif i == len(nums) - 1: return 1 if nums[i-1] > nums[i] else 0
            if nums[i+1] > nums[i]: return 2
            return 1 if nums[i-1] > nums[i] else 0
        if len(nums) == 1: return 0
        l, r,  = 0, len(nums) - 1
        if direct(l) == 0: return l 
        if direct(r) == 0: return r
        while r > l:
            m, d = (r + l) // 2, direct((r + l) // 2)
            if d == 0: return m
            elif d == 1: r = m
            else: l = m
