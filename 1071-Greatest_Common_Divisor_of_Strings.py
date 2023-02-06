class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        def valid(k):
            if len1 % k or len2 % k:
                return False
            base = str1[:k]
            return str1 == base * (len1 // k) and str2 == base * (len2 // k)
        
        for i in range(min(len1, len2), 0, -1):
            if valid(i):
                return str1[:i]
            
        return ""