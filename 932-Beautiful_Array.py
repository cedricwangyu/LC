class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        if n <= 2: return [i for i in range(1, n+1)]
        per = self.beautifulArray(n // 2)
        res = [i * 2 for i in per]
        if n % 2 == 0: res += [i * 2 - 1 for i in per]
        else: 
            per = self.beautifulArray(n // 2 + 1)
            res += [i*2-1 for i in per]
        return res
