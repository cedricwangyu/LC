class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n = len(strs), len(strs[0])
        if m == 1: 
            return True

        res = 0
        for j in range(n):
            for i in range(1, m):
                if strs[i][j] < strs[i-1][j]:
                    res += 1
                    break
        
        return res