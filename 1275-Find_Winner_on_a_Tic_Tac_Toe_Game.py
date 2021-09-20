class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        info = [0, 0, 0, 0, 0, 0, 0, 0]
        for i, (x, y) in enumerate(moves):
            add = 2 * int(i % 2 == 0) - 1
            info[x], info[y+3] = info[x]+add, info[y+3]+add 
            if x == y: info[-2] += add
            if x + y == 2: info[-1] += add 
        for n in info:
            if n == 3: return "A"
            elif n == -3: return "B"
        return "Draw" if len(moves) == 9 else "Pending"
