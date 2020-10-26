import math
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        F = [False]
        for i in range(1, n + 1):
            appended = False
            for j in range(int(math.sqrt(i)), 0, -1):
                if not F[i - j ** 2]:
                    F.append(True)
                    appended = True
                    break
            if not appended:
                F.append(False)
        print(F)
        return F[-1]
        
            
        
        