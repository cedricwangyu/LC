class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        num = nums.pop(0)
        while len(nums) > 0 and num + k >= nums[0]:
            k -= nums[0] - num - 1
            num = nums.pop(0)
        return num + k

