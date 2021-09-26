class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        self.temp = board[0].copy()
        def valid(t):
            creterion = (t[0] == self.temp[0])
            return int(creterion) if all((i == j) == creterion for i, j in zip(self.temp, t)) else -1
        types = [valid(row) for row in board]
        if not all(t >= 0 for t in types) or 2*sum(types)-len(types) > 1 or 2*sum(board[0])-len(board[0]) > 1: return -1
        def miniswap(t):
            c = collections.Counter(t)
            if c[0] == c[1]: return min(sum(int(tt == 0) for i, tt in enumerate(t) if i % 2 == 0), sum(int(tt == 0) for i, tt in enumerate(t) if i % 2 == 1))
            else:
                first = 0 if c[0] > c[1] else 1
                return sum(int(tt != first) for i, tt in enumerate(t) if i%2 == 0)
        return miniswap(types) + miniswap(board[0])
