class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n1, n2 = 0, 0
        for c in cost: n1, n2 = n2, min(n1, n2) + c 
        return min(n1, n2)
