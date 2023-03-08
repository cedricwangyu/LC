class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        dic = set(c for c in source)
        i, res, n = 0, 0, len(source)
        for c in target:
            if c not in dic: return -1
            while c != source[i]:
                i, res = (i+1, res) if i < n-1 else (0, res+1)
            i, res = (i+1, res) if i < n-1 else (0, res+1)
        return res + int(i > 0)