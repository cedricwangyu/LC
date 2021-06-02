class Solution:
    def totalNQueens(self, n: int) -> int:
        self.sol, self.con, self.res = [], [], 0
        def helper():
            if len(self.sol) == n: 
                self.res += 1
                return
            con = set(item for sublist in self.con[-1] for item in sublist) if len(self.con) > 0 else set()
            for i in range(n):
                if i not in con:
                    self.sol.append(i)
                    if len(con) > 0: 
                        self.con.append([[c[0] - 1, c[1], c[2] + 1] for c in self.con[-1]])
                        self.con[-1].append([i-1, i, i+1])
                    else: self.con.append([[i-1, i, i+1]])
                    helper()
                    del self.con[-1], self.sol[-1]
        helper()
        return self.res