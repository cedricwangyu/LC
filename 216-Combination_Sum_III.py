class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n > 45: return
        self.curr = [0] * (k+1)
        self.curr_sum = 0
        self.res = []
        def rec(idx=1):
            if idx > k:
                if self.curr_sum == n: self.res.append(self.curr[1:])
                return
            for num in range(self.curr[idx-1]+1, 10):
                self.curr[idx] = num
                self.curr_sum += num
                if self.curr_sum > n: 
                    self.curr_sum -= num
                    return
                rec(idx+1)
                self.curr_sum -= num
        rec()
        return self.res