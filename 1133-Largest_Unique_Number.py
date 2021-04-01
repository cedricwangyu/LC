class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        p, M = collections.Counter(A), -1
        for n in p:
            if p[n] == 1: M = max(M, n)
        return M