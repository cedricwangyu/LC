class Solution:
    def removeDuplicates(self, s: str) -> str:
        l = 0
        while l < len(s) - 1:
            if s[l] == s[l+1]: s, l = s[:l] + s[l+2:], max(l-1, 0)
            else: l += 1
        return s
