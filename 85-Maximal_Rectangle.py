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
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0: return 0
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            matrix[i][0], curr = int(matrix[i][0]), int(matrix[i][0])
            for j in range(1, n):
                if matrix[i][j] == "0": matrix[i][j], curr = 0, 0
                else: matrix[i][j], curr = curr + 1, curr + 1
        res = 0
        for j in range(n):
            res = max(res, self.largestRectangleArea([matrix[i][j] for i in range(m)]))
        return res