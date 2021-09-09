class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        mines, row, col, res = set((i, j) for i, j in mines), {i: [-1, n] for i in range(n)}, {i: [-1, n] for i in range(n)}, 0
        for i, j in mines:
            bisect.insort_left(row[i], j)
            bisect.insort_left(col[j], i)
        for i in range(n):
            for j in range(n):
                if (i, j) in mines: continue
                r, c = bisect.bisect_left(row[i], j), bisect.bisect_left(col[j], i)
                res = max(res, min(j-row[i][r-1], row[i][r]-j, i-col[j][c-1], col[j][c]-i))
        return res
