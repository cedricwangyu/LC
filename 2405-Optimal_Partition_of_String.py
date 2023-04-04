class Solution:
    def partitionString(self, s: str) -> int:
        res, curr = 0, set()
        for c in s:
            if c in curr:
                res += 1
                curr.clear()
            curr.add(c)
        return res + 1