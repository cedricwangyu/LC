class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2): return False
        c1 = collections.Counter(s1)
        c2 = collections.Counter(s2[:n])
        if c2 == c1: return True
        for i in range(n, len(s2)):
            if s2[i] in c2: c2[s2[i]] += 1
            else: c2[s2[i]] = 1
            if s2[i-n] in c2: c2[s2[i-n]] -= 1
            if c2[s2[i-n]] == 0: del c2[s2[i-n]]
            if c2 == c1: return True
        return False