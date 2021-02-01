class Solution:
    def hammingWeight(self, n: int) -> int:
        # return sum(int(item) for item in list("{0:b}".format(n)))
        res = 0
        while n > 0:
            if n % 2 == 1: res += 1
            n //= 2
        return res