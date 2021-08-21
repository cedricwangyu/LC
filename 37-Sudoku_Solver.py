class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.p = [[set() for _ in range(9)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                self.p[0][i].add(board[i][j])
                self.p[1][j].add(board[i][j])
                self.p[2][i // 3 * 3 + j // 3].add(board[i][j])
        def fill(num):
            if num >= 81: return True
            i, j = num // 9, num % 9
            if board[i][j] != '.': return fill(num+1)
            for c in '123456789':
                if c in self.p[0][i] or c in self.p[1][j] or c in self.p[2][i // 3 * 3 + j // 3]: continue
                else:
                    board[i][j] = c
                    self.p[0][i].add(c)
                    self.p[1][j].add(c)
                    self.p[2][i // 3 * 3 + j // 3].add(c)
                    if fill(num+1): return True
                    self.p[0][i].remove(c)
                    self.p[1][j].remove(c)
                    self.p[2][i // 3 * 3 + j // 3].remove(c)
            board[i][j] = '.'
            return False
        fill(0)
