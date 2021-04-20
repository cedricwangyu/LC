class Solution:
    def minSwaps(self, data: List[int]) -> int:
        t = sum(data)
        if t == 0: return 0
        r, s = t, sum(data[:t])
        res = t - s
        while r < len(data):
            s = s - data[r - t] + data[r]
            res = min(res, t - s)
            r += 1
        return res    