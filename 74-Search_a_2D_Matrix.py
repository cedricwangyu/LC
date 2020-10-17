class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        else:
            n = len(matrix[0])
            if n == 0:
                return False
        
        if matrix[0][0] == target or matrix[-1][-1] == target:
            return True
        elif matrix[0][0] > target or matrix[-1][-1] < target:
            return False
        
        
        start = 0
        end = m * n - 1
        while (end - start > 1):
            mid = start + int((end - start) / 2)
            if matrix[int(mid / n)][mid % n] == target:
                return True
            elif matrix[int(mid / n)][mid % n] > target:
                end = mid
            else:
                start = mid
        
        return False
            
        
        
        
        
        