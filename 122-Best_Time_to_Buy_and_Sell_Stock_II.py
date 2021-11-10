class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, pp = 0, prices[0]
        for p in prices[1:]:
            diff, pp = p - pp, p
            b = b + diff if diff > 0 else b
        return b
