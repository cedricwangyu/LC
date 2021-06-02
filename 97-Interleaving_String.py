class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        p = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        p[0][0] = True
        for j in range(1, len(s2)+1):
            if s2[j-1] == s3[j-1] and p[0][j-1]: p[0][j] = True
        for i in range(1, len(s1)+1):
            if s1[i-1] == s3[i-1] and p[i-1][0]: p[i][0] = True
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if (s3[i+j-1] == s1[i-1] and p[i-1][j]) or (s3[i+j-1] == s2[j-1] and p[i][j-1]): p[i][j] = True
        return p[-1][-1]