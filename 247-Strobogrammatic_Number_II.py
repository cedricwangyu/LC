class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        res, self.curr = [], ""
        def helper(i):
            if i == 0:
                if n % 2 == 1: 
                    m = len(self.curr) // 2
                    self.curr = self.curr[:m] + "." + self.curr[m:]
                    for s in "018":
                        self.curr = self.curr[:m] + s + self.curr[m+1:]
                        if str(int(self.curr)) == self.curr:
                            res.append(self.curr)
                    self.curr = self.curr[:m] + self.curr[m+1:]
                else:
                    if str(int(self.curr)) == self.curr:
                        res.append(self.curr)
            else:
                self.curr = "." + self.curr + "."
                for s in "018":
                    self.curr = s + self.curr[1:len(self.curr)-1] + s
                    helper(i-1)
                self.curr = "6" + self.curr[1:len(self.curr)-1] + "9"
                helper(i-1)
                self.curr = "9" + self.curr[1:len(self.curr)-1] + "6"
                helper(i-1)
                self.curr = self.curr[1:len(self.curr)-1]
        helper(n//2)
        return res
                    
        
        
        
        
        