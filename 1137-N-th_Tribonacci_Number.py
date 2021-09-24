class Solution:
    @functools.lru_cache()
    def tribonacci(self, n: int) -> int:
        if n in (0,1,2): return min(n, 1)
        else: return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3) 
