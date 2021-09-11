class Solution:
    def calculate(self, s: str) -> int:
        s = "(" + s + ")"
        self.i, self.n = 0, len(s)
        def read_digit():
            curr = ""
            while self.i < self.n and s[self.i].isdigit(): curr, self.i = curr + s[self.i], self.i + 1
            self.i -= 1
            return int(curr)
        def eva():
            plus, res = True, 0
            if s[self.i] == "(": self.i += 1
            while self.i < self.n:
                c = s[self.i]
                if c == " ": pass
                elif c == "+": plus = True
                elif c == "-": plus = False
                elif c == "(" and plus: res += eva()
                elif c == "(": res -= eva()
                elif c == ")": break
                elif plus: res += read_digit()
                else: res -= read_digit()
                self.i += 1
            
            return res
        return eva()
