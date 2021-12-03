class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = maxi = mini = nums[0]
        for n in nums[1:]:
            maxi, mini = max(maxi * n, n, mini * n), min(maxi * n, n, mini*n)
            res = max(maxi, res)
        return res
