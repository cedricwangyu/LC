class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        temp, p, res = 0, {}, 0
        for i in range(len(matrix)):
            temp = 0
            for j in range(len(matrix[0])):
                temp += matrix[i][j]
                matrix[i][j] = temp

        for left in range(len(matrix[0])):
            for right in range(left, len(matrix[0])):
                p.clear()
                S = 0
                for i in range(len(matrix)):
                    if left == 0: s = matrix[i][right]
                    else: s = matrix[i][right] - matrix[i][left - 1]
                    S += s
                    if S == target: res += 1
                    if S in p: res += p[S]
                    if S + target in p: p[S + target] += 1
                    else: p[S + target] = 1
        return res
