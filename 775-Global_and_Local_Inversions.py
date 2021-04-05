class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        i = 0
        while i < len(A):
            if A[i] == i: i += 1
            elif i < len(A) - 1 and A[i] == i + 1 and A[i+1] == i: i += 2
            else: return False
        return True
