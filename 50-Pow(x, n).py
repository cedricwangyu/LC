class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        elif n == 1: return x
        elif n == -1: return 1/x
        res = self.myPow(x, n // 2)
        if abs(n) % 2 == 1:  return res * res * x
        else: return res * res
