class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x)
        (start, end), res = intervals.pop(0), []
        while len(intervals) > 0:
            temp_start, temp_end = intervals.pop(0)
            if temp_start > end:
                res.append([start, end])
                start, end = temp_start, temp_end
            elif end < temp_end:
                end = temp_end
        
        res.append([start, end])
        return res
