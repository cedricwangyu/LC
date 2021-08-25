class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c ==  0: return True
        while c % 4 == 0: c //= 4
        if c % 4 == 3: return False
        x, y = 0, int(math.sqrt(c)) + 1
        curr = x**2 + y**2
        while x <= int(math.sqrt(c)):
            if curr == c: return True
            elif curr > c: y, curr = y-1, curr - 2 * y + 1
            else: x, curr = x+1, curr + 2*x + 1
        return False
