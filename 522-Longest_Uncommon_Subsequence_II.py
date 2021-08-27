class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(key = lambda x: len(x), reverse=True)
        def is_sub(s1, s2):
            if len(s1) > len(s2): return False
            i = 0
            for c in s2:
                if c == s1[i]: i += 1
                if i == len(s1): return True
            return False
        res = -1
        for i in range(len(strs)):
            if all(is_sub(strs[i], strs[j]) is False for j in range(len(strs)) if j != i): res = max(res, len(strs[i]))
        return res
