class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        p = {c: (i+1) for i, c in enumerate(string.ascii_uppercase)}
        curr, res = 1, 0
        for c in columnTitle[::-1]:
            res, curr = res + curr * p[c], curr*26
        return res