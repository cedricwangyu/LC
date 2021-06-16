class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.curr, self.res = "", []
        def dfs(lr, rr):
            if lr == 0 and rr == 0: 
                self.res.append(self.curr)
                return
            if rr > 0:
                self.curr += ")"
                dfs(lr, rr - 1)
                self.curr = self.curr[:-1]
            if lr > 0:
                self.curr += "("
                dfs(lr-1, rr + 1)
                self.curr = self.curr[:-1]
        dfs(n, 0)
        return self.res
