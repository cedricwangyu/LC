import functools
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @functools.lru_cache(maxsize=None)
        def helper(tar):
            if tar == 0: return 1
            return sum(helper(tar - n) for n in nums if tar - n >= 0)
        return helper(target)
