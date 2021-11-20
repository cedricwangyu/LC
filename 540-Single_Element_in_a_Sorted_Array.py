class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) <= 1: return nums[0]
        elif nums[0] < nums[1]: return nums[0]
        elif nums[-1] > nums[-2]: return nums[-1]
        l, r = 0, (len(nums)-1) // 2
        while r-l > 1:
            m=(l+r)//2
            if nums[2*m] == nums[2*m+1]: l=m
            elif nums[2*m] == nums[2*m-1]: r=m
            else: return nums[2*m]
