class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights: return 0
        n = len(heights)

        # 1. Index of the first building shorter than heights[i] to the right of i
        right = [n] * n
        stack = []
        for i, h in enumerate(heights):
            while stack and h < stack[-1][1]:
                right[stack.pop()[0]] = i
            stack.append((i, h))

        # 2. Index of the first building shorter than heights[i] to the left of i
        left = [-1] * n
        stack = []
        for i in range(n - 1, -1, -1):
            h = heights[i]
            while stack and h < stack[-1][1]:
                left[stack.pop()[0]] = i
            stack.append((i, h))

        area = [heights[i] * (right[i] - left[i] - 1) for i in range(n)]
        return max(area)