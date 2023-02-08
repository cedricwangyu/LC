class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        i = 2
        while i < len(nums):
            nums[i], nums[i-1] = nums[i-1], nums[i]
            i += 2