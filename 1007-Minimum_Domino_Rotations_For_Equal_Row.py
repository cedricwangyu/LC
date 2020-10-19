class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        possible = set([A[0], B[0]])
        target =  None
        for i in range(1,len(A)):
            print(possible)
            possible = possible.intersection(set([A[i], B[i]]))
            if len(possible) == 0:
                return -1
            elif len(possible) == 1:
                target = possible.pop()
                break
        A_score = 0
        B_score = 0
        for i in range(len(A)):
            if A[i] != target and B[i] == target:
                A_score += 1
            elif A[i] == target and B[i] != target:
                B_score += 1
            elif A[i] != target and B[i] != target:
                return -1
        
        return min(A_score, B_score)
        
                
            
            