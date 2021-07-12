class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        p = {}
        for a, b in zip(s, t):
            if a not in p:
                if b in p.values(): return False
                p[a] = b
            else:
                if p[a] != b: return False
        return True
