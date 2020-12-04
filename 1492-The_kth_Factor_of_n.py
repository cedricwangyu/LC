class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        res = 0
        for num in range(1, n // 2 + 1):
            print(num)
            if n % num == 0:
                res += 1
            if res == k: return num
        
        if res == k - 1: return n
        else: return -1