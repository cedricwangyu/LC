class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        length, res = 0, 0
        for i in range(1, len(A) - 1):
            if A[i-1] - 2*A[i] + A[i+1] == 0: length += 1
            else:
                res += (length + 1) * length // 2
                length = 0
        res += (length + 1) * length // 2
        return res