import bisect
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        nums = sorted([item * (1 + (item % 2 == 1)) for item in nums])
        res = nums[-1] - nums[0]
        while nums[-1] % 2 == 0:
            temp = nums.pop() // 2
            bisect.insort(nums, temp)
            res = min(res, nums[-1] - nums[0])
        return res