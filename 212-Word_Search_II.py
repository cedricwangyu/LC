class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.dict, m, n, self.curr_word, self.res, self.dirs, self.seen = {}, len(board), len(board[0]), "", set(), ((-1, 0), (1, 0), (0, -1), (0, 1)), set()
        for w in words:
            curr = self.dict
            for c in w+"*":
                if c not in curr: curr[c] = {}
                curr = curr[c]
        def start_at_loc(i, j, dict_curr):
            if "*" in dict_curr: 
                self.res.add(self.curr_word)
                del dict_curr["*"]
            if i < 0 or i >= m or j < 0 or j >= n or (i, j) in self.seen: return
            if board[i][j] in dict_curr: 
                dict_next, self.curr_word = dict_curr[board[i][j]], self.curr_word + board[i][j]
                self.seen.add((i, j))
                for di, dj in self.dirs: start_at_loc(i+di, j+dj, dict_next)
                self.seen.remove((i, j))
                self.curr_word = self.curr_word[:-1]
                if len(dict_next) == 0: del dict_curr[board[i][j]]
        for i in range(m):
            for j in range(n): start_at_loc(i, j, self.dict)
        return self.res
