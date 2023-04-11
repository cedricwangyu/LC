class Solution:
    def removeStars(self, s: str) -> str:
        res, todo = "", 0
        for c in s[::-1]:
            if c == "*":
                todo += 1
            elif todo > 0:
                todo -= 1
            else:
                res = c + res
        return res