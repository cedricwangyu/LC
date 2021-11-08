class Solution:
    @functools.lru_cache(maxsize=20)
    def numTrees(self, n: int) -> int:
        if n <= 1: return 1
        return sum(self.numTrees(i)*self.numTrees(n-i-1) for i in range(n))
