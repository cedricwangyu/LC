class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        if len(nums) == 2 and nums[0] == nums[1]: return 1
        elif len(nums) == 2: return 2
        i = 1
        while i < len(nums) - 1:
            if nums[i] <= nums[i-1] and nums[i+1] <= nums[i]: nums.pop(i)
            elif nums[i] >= nums[i-1] and nums[i+1] >= nums[i]: nums.pop(i)
            else: i += 1
        if len(nums) == 2 and nums[0] == nums[1]: nums.pop(-1)
        return len(nums)