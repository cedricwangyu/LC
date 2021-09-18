class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        self.curr, self.i, self.res = "", 0, []
        def helper():
            self.curr += num[self.i]
            if self.i == len(num) - 1:
                if eval(self.curr) == target: self.res.append(self.curr)
            else:
                if not (num[self.i] == "0" and (self.i == 0 or self.curr[-2] in "+-*")):
                    self.i += 1
                    helper()
                    self.i -= 1
                for c in "+-*":
                    self.curr, self.i = self.curr + c, self.i + 1
                    helper()
                    self.curr, self.i = self.curr[:-1], self.i - 1
            self.curr = self.curr[:-1]
        helper()
        return self.res
