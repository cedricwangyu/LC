from bisect import bisect_left
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r, L, R = 0, len(nums)-1, 0, len(nums)-1
        if nums[l] < nums[r]:
            i = bisect_left(nums, target)
            return -1 if i >= len(nums) or nums[i] != target else i

        while R - L > 1:
            M = (L + R) // 2
            if nums[M] > nums[L]:
                L = M
            else:
                R = M

        if target >= nums[0]:
            r = L
        else:
            l = R
        print(l, r)
        i = bisect_left(nums, target, lo=l, hi=r+1)
        return -1 if i >= len(nums) or nums[i] != target else i