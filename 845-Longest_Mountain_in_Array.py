class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        res = 0
        rec = 0
        mon = None
        
        for i in range(len(A) - 1):
            rec += 1
            if A[i] < A[i + 1]:
                if mon is True: 
                    res = max(res, rec)
                    rec = 1
                    mon = False
                elif mon is None:
                    mon = False
                    rec = 1
            elif A[i] == A[i + 1]:
                if mon is True: res = max(res, rec)
                rec = 0
                mon = None
            elif A[i] > A[i + 1]:
                if mon is False: mon = True
                elif mon is None: rec = 0
        
        
        if mon is True: res = max(res, rec + 1)
        return res
                    
                
