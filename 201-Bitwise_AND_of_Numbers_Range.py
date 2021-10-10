class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res, d = left & right, right - left
        n = len("{0:b}".format(d)) if d > 0 else 0
        res = res >> n
        res = res << n
        return res
