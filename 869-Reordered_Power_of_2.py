import collections
class Solution:
    def __init__(self):
        self.p = {0: (0, 4), 1: (4, 7), 2: (7, 10)}
    def reorderedPowerOf2(self, N: int) -> bool:
        n = len(str(N))
        p, ip1, ip2 = Counter(str(N)), (n - 1) // 3, (n - 1) % 3
        for i in range(ip1 * 10 + self.p[ip2][0], ip1 * 10 + self.p[ip2][1]):
            pc = Counter(str(2 ** i))
            if p == pc: return True
        return False
        