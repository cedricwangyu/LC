class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -prices[0]
        for p in prices:
            cash = max(cash, hold + p - fee)
            hold = max(hold, cash - p)
        return cash