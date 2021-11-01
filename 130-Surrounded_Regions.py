class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def bfs(i, j):
            board[i][j] = 'OO'
            todo = [(i, j)]
            while len(todo) > 0:
                ii, jj = todo.pop(0)
                for ni, nj in ((ii+1, jj), (ii-1, jj), (ii, jj+1), (ii, jj-1)):
                    if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'O':
                        board[ni][nj] = 'OO'
                        todo.append((ni, nj))
                    
        for j in range(n):
            if board[0][j] == 'O': bfs(0, j)
            if board[m-1][j] == 'O': bfs(m-1, j)
        for i in range(m):
            if board[i][0] == 'O': bfs(i, 0)
            if board[i][n-1] == 'O': bfs(i, n-1)
        for i in range(m):
            for j in range(n):
                board[i][j] = 'O' if board[i][j] == 'OO' else 'X'
        return board
