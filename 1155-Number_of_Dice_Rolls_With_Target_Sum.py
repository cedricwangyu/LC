class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        @functools.lru_cache(maxsize=d*target)
        def helper(d, target):
            if d == 1: return 1 if 1 <= target <= f else 0
            res = 0
            for i in range(1, min(f+1, target+1)): res += helper(d-1, target - i)
            return res
        return helper(d, target) % (10**9 + 7)
