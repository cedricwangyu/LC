class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        for i, c in enumerate(num):
            if c == '6':
                return int(num[:i] + '9' + num[i+1:])
        return int(num)