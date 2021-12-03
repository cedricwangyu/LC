class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        curr, res = 0, 0
        for p in s:
            if p == '(': curr += 1
            elif curr > 0: curr -= 1
            else: res += 1
        return res + curr
