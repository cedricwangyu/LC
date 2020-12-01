class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        task = [[item[0], item[2]] for item in buildings] + [[item[1], -item[2]] for item in buildings]
        task.sort(key = lambda x: [x[0], -x[1]])
        active = []
        res = []
        for b in task:
            if b[1] > 0:
                active.append(b[1])
                active.sort()
                if b[1] == active[-1]:
                    if len(active) > 1 and active[-1] == active[-2]: pass
                    else: res.append(b)
            else:
                active.remove(-b[1])
                if len(active) == 0: res.append([b[0], 0])  
                elif active[-1] < -b[1]: res.append([b[0], active[-1]])

        return res
                
                    
        
        