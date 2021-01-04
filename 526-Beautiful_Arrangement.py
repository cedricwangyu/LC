class Solution:
    def __init__(self):
        self.count = 0
    def countArrangement(self, n: int) -> int:
        def helper(state):
            if all(state): self.count += 1
            for i in range(n):
                if not state[i]:
                    if (i + 1) % (sum(state) + 1) == 0 or (sum(state) + 1) % (i + 1) == 0:
                        state[i] = True
                        helper(state)
                        state[i] = False
        helper([False] * n)
        return self.count
                        
                
            
                
            