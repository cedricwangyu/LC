class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1: return intervals
        intervals.sort(key = lambda x: x)
        i = 0
        while(i < len(intervals) - 1):
            if intervals[i+1][0] <= intervals[i][1]:
                intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
                intervals.pop(i + 1)
            else:
                i += 1
        
        print(intervals)
        return intervals
            
        