class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        p, l, curr, res = {}, 0, 0, 0
        for r, n in enumerate(nums):
            if n not in p: curr += n
            else:
                res, R, curr = max(res, curr), p[n], curr + n
                while l <= R:
                    del p[nums[l]]
                    curr, l = curr - nums[l], l + 1
            p[n] = r
        res = max(res, curr)
        return res