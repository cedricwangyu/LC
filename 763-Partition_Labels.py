class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        seen, intervals = {}, []
        for i, c in enumerate(s):
            if c in seen:
                intervals[seen[c]][1] = i
            else:
                intervals.append([i, i])
                seen[c] = len(intervals)-1
                
        i = 1
        while i < len(intervals):
            if intervals[i][0] < intervals[i-1][1]:
                intervals[i-1][1] = max(intervals[i-1][1], intervals.pop(i)[1])
            else:
                i += 1
        for i, interval in enumerate(intervals):
            intervals[i] = interval[1] - interval[0] + 1
        return intervals