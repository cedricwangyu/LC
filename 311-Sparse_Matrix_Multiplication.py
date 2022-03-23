class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        p1, p2 = defaultdict(list), defaultdict(dict)
        for i, row in enumerate(mat1):
            for j, val in enumerate(row):
                if val != 0: 
                    p1[i].append((j, val))
        for i, row in enumerate(mat2):
            for j, val in enumerate(row):
                if val != 0: 
                    p2[j][i] = val
        res = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                val = 0
                for k, a in p1[i]:
                    if k in p2[j]:
                        val += a*p2[j][k]
                res[i][j] = val
        return res