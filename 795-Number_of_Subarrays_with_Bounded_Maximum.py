class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        lmax = lmin = res = 0
        for n in nums:
            if n > right:
                if lmin > 0: res -= (lmin + 1) * lmin // 2
                if lmax > 0: res += (lmax + 1) * lmax // 2
                lmax = lmin = 0
            elif n < left: lmin, lmax = lmin + 1, lmax + 1
            else:
                if lmin > 0: res -= (lmin + 1) * lmin // 2
                lmin, lmax = 0, lmax + 1
        if lmax > 0: res += (lmax + 1) * lmax // 2
        if lmin > 0: res -= (lmin + 1) * lmin // 2
        return res
