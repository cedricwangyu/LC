class Solution:
    def concatenatedBinary(self, n: int) -> int:
        s = ""
        for i in range(1, n + 1): s += "{0:b}".format(i)
        return int("".join(s), 2) % (10**9 + 7)