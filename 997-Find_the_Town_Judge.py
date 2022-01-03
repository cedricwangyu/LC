class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        p = {i+1: set() for i in range(n)}
        for a, b in trust:
            if a in p: del p[a]
            if b in p: p[b].add(a)
        return list(p.keys())[0] if len(p) == 1 and len(p[list(p.keys())[0]]) == n-1 else -1
