from functools import lru_cache
class Solution:
    
    def numberOfWays(self, numPeople: int) -> int:
        @lru_cache(maxsize=numPeople // 2 + 1)
        def helper(num):
            if num <= 2:
                return 1
            res = 0
            for r in range(0, num // 2, 2):
                res += 2 * (helper(r) * helper(num-2-r))
            return res if num % 4 == 0 else res - helper(num // 2 - 1) ** 2
        return helper(numPeople) % (10 ** 9 + 7)
        