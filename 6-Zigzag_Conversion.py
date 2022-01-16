class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        res, i, dirs, d_idx = [""] * numRows, 0, (1, -1), 0
        for c in s:
            res[i], i = res[i]+c, i+dirs[d_idx]
            if i == 0: d_idx = 0
            elif i == numRows-1: d_idx = 1
        return "".join(res)