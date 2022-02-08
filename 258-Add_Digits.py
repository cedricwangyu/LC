class Solution:
    def addDigits(self, num: int) -> int:
        n = str(num)
        while len(n) > 1:
            n = str(sum(int(i) for i in n))
        return int(n)