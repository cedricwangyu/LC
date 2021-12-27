class Solution:
    def findComplement(self, num: int) -> int:
        return 2 ** len(format(num, "b")) - 1 - num
