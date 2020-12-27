class Solution:
    def numDecodings(self, s: str) -> int:
        one, two = int(s[-1] != '0'), 1
        for i in range(len(s) - 2, -1, -1):
            if s[i] == '0': one, two = 0, one
            elif int(s[i:i+2]) <= 26: one, two = one + two, one
            else: one, two = one, one
        return one
        