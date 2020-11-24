class Solution:
    def __init__(self):
        self.m = 6
        self.k = 3
    def notlarger(self, n):
        rec = [1] * min(n + 1, self.m + 1)
        rec = rec + [0] * abs(n - self.m)
        for _ in range(self.k - 1):
            for ni in range(n,-1,-1):
                rec[ni] = sum([rec[ni - i] for i in range(min(self.m, ni) + 1)])
            
        return rec
    def prob(self, n):
        return 1 - sum(self.notlarger(n - 1)) / (self.m + 1) ** self.k


if __name__ == "__main__":
    S = Solution()
    print(S.prob(10))


