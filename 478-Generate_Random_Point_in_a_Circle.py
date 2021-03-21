import random, math
class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        theta = random.uniform(0, 2 * math.pi)
        r = math.sqrt(random.uniform(0.0, 1.0))
        return [self.x + self. r * r * math.cos(theta), self.y + self.r * r * math.sin(theta)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()