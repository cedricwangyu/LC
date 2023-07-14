class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        p, res = defaultdict(int), 0
        for n in arr:
            ni, ci = n+difference, p[n]+1
            p[n] = 0
            p[ni] = ci if ni not in p else max(ci, p[ni])
            res = max(res, p[ni])
            
        return res
                

