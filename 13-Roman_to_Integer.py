class Solution:
    def __init__(self):
        self.p = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    def romanToInt(self, s: str) -> int:
        res, i = 0, 0
        while i < len(s) - 1:
            if s[i:i+2] in self.p: res, i = res + self.p[s[i:i+2]], i + 2
            else: res, i = res + self.p[s[i]], i + 1
        if i == len(s) - 1: res += self.p[s[i]]
        return res  