from collections import Counter
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        
        res = [i for i in range(len(A)) if A[i] != B[i]]
        
        if len(res) == 2 and A[res[0]] == B[res[1]] and A[res[1]] == B[res[0]]:
            return True
        elif len(res) == 0 and len(A) > len(set(A)):
            return True
        else:
            return False
            
        