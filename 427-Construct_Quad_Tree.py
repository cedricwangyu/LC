"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        for i in range(n):
            for j in range(n):
                grid[i][j] = Node(grid[i][j], True, None, None, None, None)
        while n > 1:
            prev_grid, grid = grid, []
            for i in range(0, n, 2):
                grid.append([])
                for j in range(0, n, 2):
                    if prev_grid[i][j].val >= 0 and prev_grid[i][j].val == prev_grid[i][j+1].val and prev_grid[i][j].val == prev_grid[i+1][j].val and prev_grid[i][j].val == prev_grid[i+1][j+1].val:
                        grid[-1].append(Node(prev_grid[i][j].val, True, None, None, None, None))
                    else:
                        grid[-1].append(Node(-1, False, prev_grid[i][j], prev_grid[i][j+1], prev_grid[i+1][j], prev_grid[i+1][j+1]))
            n //= 2
        return grid[0][0]