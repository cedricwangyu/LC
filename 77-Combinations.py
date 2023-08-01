class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.curr, self.res = [], []
        def helper(i=1, r=k):
            if r == 0:
                self.res.append(self.curr.copy())
                return
            for j in range(i, n+1):
                self.curr.append(j)
                helper(j+1, r-1)
                self.curr.pop()


        
        helper()
        return self.res