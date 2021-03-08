class Solution:
    def __init__(self):
        self.p = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    def isStrobogrammatic(self, num: str) -> bool:
        return "".join([self.p[n] for n in num[::-1] if n in self.p]) == num