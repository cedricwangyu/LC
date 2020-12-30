class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirs = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                res = 0
                for d in dirs:
                    if i + d[0] >= 0 and i + d[0] < len(board) and j + d[1] >= 0 and j + d[1] < len(board[0]): res += board[i + d[0]][j + d[1]] % 2
                
                if board[i][j] == 1: 
                    if res == 2 or res == 3: board[i][j] = 3
                else: 
                    if res == 3: board[i][j] = 2
        
        for i in range(len(board)):
            for j in range(len(board[0])): board[i][j] = board[i][j] // 2
        

                    
        