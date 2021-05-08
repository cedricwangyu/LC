import math
class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        def is_palin(x):
            if str(x) == str(x)[::-1]: return True
            return False
        small_d, big_d, res = max(1, math.floor(len(str(math.ceil(math.sqrt(int(left))))) / 2)), math.ceil(len(str(math.floor(math.sqrt(int(right))))) / 2), 0
        for i in range(10 ** (small_d - 1), 10 ** big_d+1):
            s = str(i)
            s1 = int(s + s[::-1])
            s2 = int(s + s[-2::-1])
            if int(left) <= s1 ** 2 <= int(right) and is_palin(s1 ** 2): res += 1
            if int(left) <= s2 ** 2 <= int(right) and is_palin(s2 ** 2): res += 1
        return res