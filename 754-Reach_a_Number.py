import math
class Solution:
    def reachNumber(self, target: int) -> int:
        n = math.ceil((math.sqrt(8 * abs(target)  + 1) - 1) / 2)
        if (int(n * (n + 1) / 2) - target) % 2 == 0: return n
        else: return n + 1 + int(n % 2 != 0) 
        