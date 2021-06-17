class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)
        total = sum(matchsticks)
        if total % 4 > 0 or any(m > total // 4 for m in matchsticks): return False
        self.curr, self.i = [total // 4] * 4, 0
        def dfs():
            if all(j == 0 for j in self.curr): return True
            todo, rep = [], set()
            for i, c in enumerate(self.curr):
                if c not in set(): 
                    todo.append(i)
                    rep.add(c)
            for i in todo:
                if self.curr[i] >= matchsticks[self.i]: 
                    self.curr[i], self.i = self.curr[i] - matchsticks[self.i], self.i + 1
                    if dfs(): return True
                    self.curr[i], self.i = self.curr[i] + matchsticks[self.i - 1], self.i - 1
            return False
        return dfs()