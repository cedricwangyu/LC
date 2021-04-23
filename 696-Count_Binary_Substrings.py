class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        l, r, curr, res = 0, 1, s[0], 0
        for c in s[1:]:
            if c == curr: r += 1
            else: res, l, r, curr = res + min(l, r), r, 1, c
        res += min(l, r)
        return res