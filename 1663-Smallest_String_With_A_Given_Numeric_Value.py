import string
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        z, s = (k - n) // 25, (k - n) % 25
        res = 'a' * (n - z - 1) + string.ascii_lowercase[s] + 'z' * z
        if len(res) > n: return res[1:]
        else: return res