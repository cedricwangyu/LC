class Solution:
    def isArmstrong(self, n: int) -> bool:
        return sum(int(i)**len(str(n)) for i in str(n)) == n
