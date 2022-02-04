class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hist, res, curr = {0: -1}, 0, 0
        for i, n in enumerate(nums):
            curr += (2 * n - 1)
            if curr in hist: res = max(res, i-hist[curr])
            else: hist[curr] = i
        return res
        
            