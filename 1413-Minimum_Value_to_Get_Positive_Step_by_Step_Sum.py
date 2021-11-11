class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        m, c = float('Inf'), 0
        for n in nums: c, m = c+n, min(m, c+n)
        return max(1-m, 1)
