class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        self.curr = ""
        self.res = []
        def helper(i=0):
            if i < n:
                if i == 0:
                    for d in range(1, 10):
                        self.curr += str(d)
                        helper(1)
                else:
                    d = int(self.curr[-1]) + k
                    if d <= 9:
                        self.curr += str(d)
                        helper(i+1)
                    if k > 0:
                        d = int(self.curr[-1]) - k
                        if d >= 0:
                            self.curr += str(d)
                            helper(i+1)
            else:
                self.res.append(self.curr)
            
            self.curr = self.curr[:-1]
        
        helper()
        return self.res
                    
                        