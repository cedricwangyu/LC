class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        res = []
        for j in range(len(grid[0])):
            curr = j
            for i in range(len(grid)):
                if curr > 0 and grid[i][curr] == -1 and grid[i][curr-1] == -1:
                    curr -= 1
                elif curr < len(grid[0]) - 1 and grid[i][curr] == 1 and grid[i][curr+1] == 1:
                    curr += 1
                else:
                    res.append(-1)
                    break
            if len(res) < j+1:
                res.append(curr)
        
        return res
            