class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1: return
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                j = i+1
                while j < len(nums) and nums[j] > nums[i]: j += 1
                j -= 1
                nums[i], nums[j] = nums[j], nums[i]
                nums[i+1:] = reversed(nums[i+1:])
                return
        nums.reverse()