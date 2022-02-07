class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c1, c2 = collections.Counter(s), collections.Counter(t)
        for c in c2:
            if c not in c1 or c1[c] < c2[c]: return c 