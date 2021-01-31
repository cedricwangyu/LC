class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def bis(i):
            lo, hi = i + 1, len(nums) - 1
            if nums[i] < nums[hi]: return hi
            while hi - lo > 1:
                mid = (hi + lo) // 2
                if nums[mid] > nums[i]: lo = mid
                else: hi = mid
            return lo
        if len(nums) <= 1: return
        i = len(nums) - 2
        while(i >= 0 and nums[i] >= nums[i+1]): i -= 1
        if i < 0: nums.reverse()
        else: 
            j = bis(i)
            nums[i], nums[j] = nums[j], nums[i]
            nums[i+1:] = reversed(nums[i+1:])