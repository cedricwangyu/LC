class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) or j < len(t):
            if i < len(s) and s[i] == '#':
                if i == 0: s = s[1:]
                else: s, i = s[:i-1] + s[i+1:], i-1
            else: i += 1
            if j < len(t) and t[j] == '#':
                if j == 0: t = t[1:]
                else: t, j = t[:j-1] + t[j+1:], j-1
            else: j += 1
        return s == t