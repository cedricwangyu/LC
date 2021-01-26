class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row, col = len(heights), len(heights[0])
        def canReachDestinaton(x, y, mid):
            if x == row-1 and y == col-1: return True
            visited[x][y] = True
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                adj_x, adj_y = x + dx, y + dy
                if 0 <= adj_x < row and 0 <= adj_y < col and not visited[adj_x][adj_y]:
                    current_difference = abs(heights[adj_x][adj_y] - heights[x][y])
                    if current_difference <= mid:
                        visited[adj_x][adj_y] = True
                        if canReachDestinaton(adj_x, adj_y, mid): return True
        left, right = 0, max([max(row) for row in heights])
        while left < right:
            mid = (left + right)//2
            visited = [[False]*col for _ in range(row)]
            if canReachDestinaton(0, 0, mid): right = mid
            else: left = mid + 1
        return left