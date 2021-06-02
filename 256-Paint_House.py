class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        res = [0, 0, 0]
        for c in costs: res[0], res[1], res[2] = min(res[1], res[2]) + c[0], min(res[0], res[2]) + c[1], min(res[0], res[1]) + c[2]
        return min(res)