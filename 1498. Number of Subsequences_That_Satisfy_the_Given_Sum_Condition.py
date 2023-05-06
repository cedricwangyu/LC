from bisect import bisect_right
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        left, right, res = 0, len(nums) - 1, 0
        while right >= left:
            if nums[right] + nums[left] <= target:
                res += 2 ** (right - left)
                left += 1
            else:
                right -= 1
        return res % (10 ** 9 + 7)
