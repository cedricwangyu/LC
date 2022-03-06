class Solution:
    def countOrders(self, n: int) -> int:
        res = 1
        for i in range(1, n):
            res *= (i*2 + 3) * i + 1
        return res % (10 ** 9 + 7)