class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r, curr0, res = 0, 0, 0, 0
        while True:
            if curr0 <= k:
                res, r = max(res, r - l), r + 1
                if r > len(nums): break
                if nums[r-1] == 0: curr0 += 1
            else:
                if nums[l] == 0: curr0 = curr0 - 1
                l += 1
        return res
