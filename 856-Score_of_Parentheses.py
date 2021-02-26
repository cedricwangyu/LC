class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        res, left = 0, 0
        for i, s in enumerate(S):
            if s == '(': left += 1
            else:
                left -= 1
                if S[i - 1] == '(': res += 2 ** left
        return res