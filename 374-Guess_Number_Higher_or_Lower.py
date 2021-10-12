# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        if guess(1) == 0: return 1
        elif guess(n) == 0: return n
        while r-l > 1:
            m = (r+l)//2
            res = guess(m)
            if res == 0: return m
            elif res > 0: l = m
            else: r = m
        
