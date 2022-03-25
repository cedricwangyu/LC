class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: -abs(x[0]-x[1]))
        counts, res, n = [0, 0], 0, len(costs) // 2
        for cost in costs:
            if (cost[0] <= cost[1] and counts[0] < n) or (counts[1] >= n):
                res, counts[0] = res+cost[0], counts[0]+1
            else:
                res, counts[1] = res+cost[1], counts[1]+1
        return res