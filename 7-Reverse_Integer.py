class Solution:
    def reverse(self, x: int) -> int:
        y = int("-" * int(x < 0) + str(abs(x))[::-1])
        return y if  - 2 ** 31 <= y <= 2 ** 31 - 1 else 0