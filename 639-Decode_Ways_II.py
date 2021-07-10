class Solution:
    def numDecodings(self, s: str) -> int:
        @functools.lru_cache(maxsize=11)
        def one(c):
            if c == "0": return 0
            return 9 if c == "*" else 1
        
        @functools.lru_cache(maxsize=121)
        def two(s):
            if s[0] == "0": return 0
            elif s[0] == "*":
                if s[1] == "*": return 15
                elif int(s[1]) <= 6: return 2
                return 1
            else:
                if s[1] == "*":
                    if s[0] == "1": return 9
                    return 6 if s[0] == "2" else 0
                return 1 if int(s) <= 26 else 0
        
        prev, curr = 1, one(s[0])
        for i in range(1, len(s)): prev, curr = curr, one(s[i]) * curr + two(s[i-1:i+1]) * prev
        return curr % (10 ** 9 + 7)
