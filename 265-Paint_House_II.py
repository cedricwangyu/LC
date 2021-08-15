class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        curr, nect, curr_m, next_m = [0] * len(costs[0]), [0] * len(costs[0]), [(0, 0), (0, 0)], [(0, float('Inf')), (0, float('Inf'))]
        for cost in costs:
            nect, next_m[0], next_m[1] = [0] * len(costs[0]), (0, float('Inf')), (0, float('Inf'))
            for j in range(len(cost)):
                if j == curr_m[0][0]: nect[j] = curr[curr_m[1][0]] + cost[j]
                else: nect[j] = curr[curr_m[0][0]] + cost[j]
                if nect[j] < next_m[0][1]: next_m[0], next_m[1] = (j, nect[j]), (next_m[0][0], next_m[0][1])
                elif nect[j] <= next_m[1][1]: next_m[1] = (j, nect[j])
            curr, nect, curr_m, next_m = nect, curr, next_m, curr_m
        return curr_m[0][1]
