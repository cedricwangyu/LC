class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        i = 0
        while i < len(s) and i < len(t) and s[i] == t[i]: i += 1
        if i >= len(s): s, t = "", t[i:]
        elif i >= len(t): s, t = s[i:], ""
        else: s, t = s[i:], t[i:]
            
        i = -1
        while len(s) + i >= 0 and len(t) + i >= 0 and s[i] == t[i]: i -= 1
        if len(s) + i < 0: s, t = "", t[:len(t) + i + 1]
        elif len(t) + i < 0: s, t = s[:len(s) + i + 1], ""
        else: s, t= s[:len(s) + i + 1], t[:len(t) + i + 1]
            
        if len(s) == 0 and len(t) == 0: return False
        if len(s) <= 1 and len(t) <= 1: return True
        else: return False