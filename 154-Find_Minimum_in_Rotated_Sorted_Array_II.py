class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums = [n[0] for n in groupby(nums)]
        if len(nums) == 1: return nums[0]
        l, r = 0, len(nums)-1
        if nums[l] < nums[r]: return nums[l]
        while r - l > 1:
            m = (l+r)//2
            if nums[m] >= nums[l]: l = m
            elif nums[m] <= nums[r]: r = m
        return nums[r]
