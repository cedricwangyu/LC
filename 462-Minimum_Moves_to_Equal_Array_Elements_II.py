class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        i, res = 0, 0
        while(len(nums) - i - 1 > i): i, res = i + 1, res + nums[len(nums) - i - 1] - nums[i]
        return res
