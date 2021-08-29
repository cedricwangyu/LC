class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        res, curr = 0, 0
        while curr < n:
            if len(nums) == 0: res, curr = res + 1, 2 * curr + 1
            elif curr + 1 < nums[0]: res, curr = res + 1, 2 * curr + 1
            else: curr += nums.pop(0)
        return res
