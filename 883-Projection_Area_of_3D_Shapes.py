class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        sum1, sum2, sum3 = 0, 0, [0] * len(grid[0])
        for i in range(len(grid)):
            curr2 = 0
            for j in range(len(grid[0])):
                sum1 += int(grid[i][j] > 0)
                curr2 = max(curr2, grid[i][j])
                sum3[j] = max(sum3[j], grid[i][j])
            sum2 += curr2
        return sum1 + sum2 + sum(sum3)
                
