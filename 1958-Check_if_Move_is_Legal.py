class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        oppo = "B" if color == "W" else "W"
        for di, dj in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)):
            moved, curr = False, [rMove, cMove]
            while 0 <= curr[0] + di < len(board) and 0 <= curr[1] + dj < len(board[0]) and board[curr[0] + di] [curr[1] + dj] == oppo: curr[0], curr[1], moved = curr[0] + di, curr[1] + dj, True
            if 0 <= curr[0] + di < len(board) and 0 <= curr[1] + dj < len(board[0]) and board[curr[0] + di] [curr[1] + dj] == color and moved: return True
        return False