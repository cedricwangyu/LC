import math
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        if q == 0: return 0
        x = int(int(p * q / math.gcd(p, q)) / q)
        y = int(int(p * q / math.gcd(p, q)) / p)
        if x % 2 == 1:
            if y % 2 == 1: return 1
            else: return 0
        else: return 2
            
        