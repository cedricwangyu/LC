class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        states = [-prices[0], 0, -prices[0], 0]
        for p in prices: states[0], states[1], states[2], states[3] = max(-p, states[0]), max(states[0]+p, states[1]), max(states[2], states[1]-p), max(states[3], states[2]+p)
        return max(states)