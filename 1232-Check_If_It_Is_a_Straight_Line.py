class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1, x2, y2 = coordinates[0][0], coordinates[0][1], coordinates[1][0], coordinates[1][1]
        if x1 == x2:
            return True if all(coordinates[i][0] == x1 for i in range(2, len(coordinates))) else False
        else:
            k = (y2 - y1) / (x2 - x1) 
            b = y1 - k * x1
            return True if all(coordinates[i][1] == coordinates[i][0] * k + b for i in range(2, len(coordinates))) else False