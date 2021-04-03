class Solution:
    def longestValidParentheses(self, s: str) -> int:
        i, p = 0, []
        while i < len(s):
            if s[i] == '(': p.append(i)
            elif len(p) > 0:
                prev = p.pop()
                s = s[:prev] + "*" * (i - prev + 1) + s[i+1:]
            i += 1
        res, curr = 0, 0
        for c in s:
            if c == "*": res, curr = max(res, curr + 1), curr + 1
            else: curr = 0
        return res
