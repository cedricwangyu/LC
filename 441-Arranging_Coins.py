class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = int(math.sqrt(2*n))
        while k*(k+1)//2 <= n: k += 1
        return k-1
