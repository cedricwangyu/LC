class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        p, q = [1] + [0] * k, [0] * (k + 1)
        for cn in range(2, n+1):
            for i, ck in enumerate(p):
                q[i] = q[i-1] + ck if i > 0 else ck
                if i >= cn: q[i] -= p[i-cn]
            p = [0] * (k + 1)
            p, q = q, p
        return p[-1] % (10 ** 9 + 7)
