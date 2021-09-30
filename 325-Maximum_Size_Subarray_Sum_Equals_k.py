class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        cumsum, p, res = 0, {k: -1}, 0
        for i, n in enumerate(nums):
            cumsum += n
            if cumsum in p: res = max(res, i-p[cumsum])
            if cumsum + k not in p: p[cumsum+k] = i
        return res
