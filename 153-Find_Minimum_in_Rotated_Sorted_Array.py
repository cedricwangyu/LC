class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]: return nums[0]
        left, right = 0, len(nums) - 1
        while right - left > 1:
            mid = (left + right) // 2
            if nums[mid] > nums[left]: left = mid
            else: right = mid
        return nums[right]
