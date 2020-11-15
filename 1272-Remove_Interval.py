class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        i = 0
        while i < len(intervals):
            if intervals[i][1] <= toBeRemoved[0]:
                i += 1
                continue
            elif intervals[i][0] >= toBeRemoved[1]:
                break
            elif intervals[i][0] < toBeRemoved[0]:
                if intervals[i][1] > toBeRemoved[1]:
                    intervals.insert(i + 1, [toBeRemoved[1], intervals[i][1]])
                    intervals[i][1] = toBeRemoved[0]
                    i += 1
                else:
                    intervals[i][1] = toBeRemoved[0]
                
            elif intervals[i][1] > toBeRemoved[1]:
                intervals[i][0] = toBeRemoved[1]
            else:
                intervals.pop(i)
                i -= 1
            
            i += 1
        
        return intervals
                