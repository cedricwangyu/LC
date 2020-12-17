class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        p, q = {}, {}
        n = len(A)
        for i in range(n):
            for j in range(n):
                if - A[i] - B[j] in p: p[- A[i] - B[j]] += 1
                else: p[- A[i] - B[j]] = 1
                if C[i] + D[j] in q: q[C[i] + D[j]] += 1
                else: q[C[i] + D[j]] = 1
        res = 0
        for i in q.keys():
            if i in p: res += q[i] * p[i]
                
        return res
        
        