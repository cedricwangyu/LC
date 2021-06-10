class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        w, h = [nums[0]], [nums[0]]
        for n in nums[1:]:
            w.append(h[-1] + n)
            bisect.insort(h, h[-1] + n)
            if len(h) > k: h.pop(bisect.bisect_left(h, w.pop(0)))
        return w[-1]