class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = [i for i in range(1, n//2+1)] + [-i for i in range(1, n//2+1)]
        if n % 2 == 1: res += [0]
        return res
