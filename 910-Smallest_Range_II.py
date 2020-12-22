class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        if len(A) < 2: return 0
        A.sort()
        res = A[-1] - A[0]
        for i in range(1,len(A)):
            candidates = [A[0] + K, A[i-1] + K, A[i] - K, A[-1] - K]
            res = min(res, max(candidates) - min(candidates))
        return res