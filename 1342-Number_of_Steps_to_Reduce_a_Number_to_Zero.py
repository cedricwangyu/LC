class Solution:
    def numberOfSteps (self, num: int) -> int:
        res = 0
        for i in "{0:b}".format(num):
            if i is '0': res += 1
            else: res += 2
        return res - 1
        