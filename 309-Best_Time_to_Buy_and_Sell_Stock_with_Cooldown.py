class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        In, Sell, Cool, Out = -prices[0], 0, 0, 0
        for p in prices[1:]:
            In, Sell, Cool, Out = max(Cool-p, Out-p, In), In+p, Sell, max(Cool, Out)
        return max(In, Sell, Cool, Out)