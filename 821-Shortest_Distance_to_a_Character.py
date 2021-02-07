class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res, i = [], len(s)
        for char in s[::-1]:
            if char == c: i = 0
            res.insert(0, i)
            i += 1
        i = len(s)
        for pos, char in enumerate(s):
            if char == c: i = 0
            res[pos] = min(res[pos], i)
            i += 1
        return res