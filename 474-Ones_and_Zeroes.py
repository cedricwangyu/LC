class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        p, c = [[0] * (n + 1) for _ in range(m + 1)], {'0': 0, '1': 0}
        for s in strs:
            c.update(collections.Counter(s))
            for i in range(m, c['0'] - 1, -1):
                for j in range(n, c['1'] - 1, -1): p[i][j] = max(p[i - c['0']][j - c['1']] + 1, p[i][j])
            c['0'], c['1'] = 0, 0
        return p[-1][-1]
