class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.row = [0] * (n + 1)
        self.col = [0] * (n + 1)
        self.n = n
    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.row[col] += 2 * int(player == 1) - 1
        self.col[row] += 2 * int(player == 1) - 1
        if row == col: self.row[self.n] += 2 * int(player == 1) - 1
        if row + col == self.n - 1: self.col[self.n] += 2 * int(player == 1) - 1
        if self.row[col] == self.n or self.col[row] == self.n or self.row[self.n] == self.n or self.col[self.n] == self.n: return 1
        elif self.row[col] == -self.n or self.col[row] == -self.n or self.row[self.n] == -self.n or self.col[self.n] == -self.n: return 2
        else: return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)