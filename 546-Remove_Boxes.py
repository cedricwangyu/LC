class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @cache
        def dp(l, r, k):
            if l > r: return 0
            while l + 1 <= r and boxes[l] == boxes[l + 1]:  # Increase both `l` and `k` if they have consecutive colors with `boxes[l]`
                l += 1
                k += 1
            ans = (k+1) * (k+1) + dp(l+1, r, 0)  # Remove all boxes which has the same with `boxes[l]`
            for m in range(l + 1, r + 1):  # Try to merge non-contiguous boxes of the same color together
                if boxes[l] == boxes[m]:
                    ans = max(ans, dp(m, r, k+1) + dp(l+1, m-1, 0))
            return ans
        return dp(0, len(boxes) - 1, 0)
