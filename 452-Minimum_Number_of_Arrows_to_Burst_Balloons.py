class Solution:
    
    
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x)
        ind = 0
        #print(points)
        while len(points) > 1 and ind < len(points) - 1:
            if points[ind][1] >= points[ind + 1][0]:
                points[ind] = [points[ind + 1][0], min([points[ind][1], points[ind + 1][1]])]
                points.pop(ind + 1)
            else:
                ind += 1
            #print(points)
        
        return len(points)
        
        
                