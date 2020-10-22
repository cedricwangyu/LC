class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i = 0
        while (i < len(asteroids) - 1):
            #print(asteroids)
            if (asteroids[i] > 0 and asteroids[i + 1] < 0):
                if asteroids[i] > - asteroids[i + 1]:
                    asteroids.pop(i + 1)
                elif asteroids[i] < - asteroids[i + 1]:
                    asteroids.pop(i)
                    i = i - 1 if i > 0 else i + 1
                else:
                    del asteroids[i:i + 2]
                    i = i - 1 if i > 0 else i
            else:
                i += 1
        
        return asteroids
                
            