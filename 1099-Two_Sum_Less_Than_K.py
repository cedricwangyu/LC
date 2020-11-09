class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        res = -1
        low = 0
        high = len(A) - 1
        while(low < high):
            if A[low] + A[high] >= K:
                high -= 1
            else:
                res = max(A[low] + A[high], res)
                low += 1
        
        return res
            