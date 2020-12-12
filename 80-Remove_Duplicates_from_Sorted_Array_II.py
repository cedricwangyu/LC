class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2: return len(nums)
        i = 1
        dup = False
        while (i < len(nums)):
            if nums[i] == nums[i - 1]:
                if dup:
                    nums.pop(i)
                    continue
                else: dup = True
            else: dup = False
            i += 1
        return len(nums)
        