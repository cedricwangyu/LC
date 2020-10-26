class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if query_row == 0:
            return min([poured, 1])
        
        last = [poured]
        for i in range(1, query_row + 1):
            out = [0] + [max([item - 1, 0]) / 2 for item in last] + [0]
            last = [out[k] + out[k + 1] for k in range(len(out) - 1)]
        return min([last[query_glass], 1])