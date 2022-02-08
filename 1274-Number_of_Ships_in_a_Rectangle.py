# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        if not sea.hasShips(topRight, bottomLeft): return 0
        if topRight.x > bottomLeft.x:
            xm = (topRight.x + bottomLeft.x) // 2
            if topRight.y > bottomLeft.y:
                ym = (topRight.y + bottomLeft.y) // 2
                return self.countShips(sea, topRight, Point(xm+1, ym+1)) + self.countShips(sea, Point(xm, topRight.y), Point(bottomLeft.x, ym+1)) + self.countShips(sea, Point(topRight.x, ym), Point(xm+1, bottomLeft.y)) + self.countShips(sea, Point(xm, ym), bottomLeft)
            else:
                return self.countShips(sea, topRight, Point(xm+1, bottomLeft.y)) + self.countShips(sea, Point(xm, bottomLeft.y), bottomLeft)
        else:
            if topRight.y > bottomLeft.y:
                ym = (topRight.y + bottomLeft.y) // 2
                return self.countShips(sea, topRight, Point(topRight.x, ym+1)) + self.countShips(sea, Point(topRight.x, ym), bottomLeft)
            else: return 1
                
                
        
        