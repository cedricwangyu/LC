class Solution:
    def countSubstrings(self, s: str) -> int:
        L, R, res = 0, 0, 0
        while (L < len(s) and R < len(s)):
            if s[L] == s[R]:
                l, r = L, R
                while l >= 0 and r < len(s):
                    if s[l] == s[r]: res += 1
                    else: break
                    l, r = l - 1, r + 1
            if L < R: L += 1
            else: R += 1
        return res