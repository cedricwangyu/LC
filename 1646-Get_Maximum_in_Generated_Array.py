class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1: return n
        nums, res = [0, 1], 1
        for i in range(2, n + 1):
            if i % 2 == 0: nums.append(nums[i // 2])
            else: nums.append(nums[i // 2] + nums[i // 2 + 1])
            res = max(res, nums[-1])
        return res