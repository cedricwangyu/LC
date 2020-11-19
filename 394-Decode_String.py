class Solution:
    def decodeString(self, s: str) -> str:
        right = []
        i = -1
        while i >= - len(s):
            if s[i] == ']':
                right.append(i)
            elif s[i] == '[':
                r = right.pop()
                if s[i-3:i].isdigit():
                    n = int(s[i-3:i])
                    if r == -1: s = s[:i-3] + n * s[i+1:r]
                    else: s = s[:i-3] + n * s[i+1:r] + s[r+1:]
                    i -= (n - 1) * (r - i - 1) - 2
                elif s[i-2:i].isdigit():
                    n = int(s[i-2:i])
                    if r == -1: s = s[:i-2] + n * s[i+1:r]
                    else: s = s[:i-2] + n * s[i+1:r] + s[r+1:]
                    i -= (n - 1) * (r - i - 1) - 2
                else:
                    n = int(s[i-1])
                    if r == -1: s = s[:i-1] + n * s[i+1:r]
                    else: s = s[:i-1] + n * s[i+1:r] + s[r+1:]
                    i -= (n - 1) * (r - i - 1) - 2
            i -= 1
        return s
        
        