class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        res = 0
        stack = {}
        curr = 0
        last = None
        for c in s:
            if c in stack:
                curr += 1
                if c == last: stack[c] += 1
                else: stack[c] = 1
            else:
                res = max(res, curr)
                if len(stack) == 2:
                    stack = {last: stack[last]}
                    curr = stack[last] + 1
                    stack[c] = 1
                elif len(stack) == 1:
                    stack[c] = 1
                    curr += 1
                else:
                    stack[c] = 1
                    curr = 1
            last = c
        res = max(res, curr)
        return res
        
        