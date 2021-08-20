class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        p = [[set() for _ in range(9)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                n = int(board[i][j]) - 1
                if i in p[0][n] or j in p[1][n] or i // 3 * 3 + j // 3 in p[2][n]: return False
                p[0][n].add(i)
                p[1][n].add(j)
                p[2][n].add(i // 3 * 3 + j // 3)
        return True
