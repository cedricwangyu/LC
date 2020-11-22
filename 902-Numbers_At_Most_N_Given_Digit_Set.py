class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        digits.sort()
        n = str(n)
        if len(digits) == 1: return len(n) - 1 + (digits[0] <= n[0])
        res = len(digits) * (1 - len(digits) ** (len(n) - 1)) // (1 - len(digits))
        for i, num in enumerate(n):
            for j, d in enumerate(digits):
                if d >= num: break
            else: j += 1
                
            res += j * len(digits) ** (len(n) - i - 1)
            if d != num: break
            elif d == num and i == len(n) - 1: res += 1
        return res
        