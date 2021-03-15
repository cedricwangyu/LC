class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        for i in range(2 ** k):
            b = "{0:b}".format(i)
            b = '0' * abs(k - len(b)) + b
            if b not in s: return False
        return True