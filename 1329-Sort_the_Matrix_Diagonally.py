class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        temp = []
        def helper(I, J):
            temp.clear()
            i, j = I, J
            while i < len(mat) and j < len(mat[0]):
                temp.append(mat[i][j])
                i, j = i + 1, j + 1
            temp.sort()
            i, j = I, J
            while i < len(mat) and j < len(mat[0]): 
                mat[i][j] = temp.pop(0)
                i, j = i + 1, j + 1
        
        if len(mat) > 1:
            for i in range(1, len(mat)): helper(i, 0)
        for j in range(len(mat[0])): helper(0, j)
        return mat