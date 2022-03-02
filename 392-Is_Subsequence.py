class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s): return False
        if len(s) == 0: return True
        i = 0
        for c in t: 
            if c == s[i]: i += 1
            if i == len(s): return True
        return False