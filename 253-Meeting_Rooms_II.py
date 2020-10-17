class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        
        intervals.sort(key = lambda x: x)
        endingtime = [0]
        for iv in intervals:
            arranged = False
            for i,et in enumerate(endingtime):
                if et <= iv[0]:
                    endingtime[i] = iv[1]
                    arranged = True
                    break
            if not arranged:
                endingtime.append(iv[1])
                
        print(len(endingtime))
        return len(endingtime)