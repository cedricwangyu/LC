class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split(' ')): return False
        p, q = {}, {}
        for c, w in zip(pattern, s.split(' ')):
            if c not in p and w not in q: p[c], q[w] = w, c
            elif c in p and w in q and p[c] == w and q[w] == c: pass
            else: return False
        return True