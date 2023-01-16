class Solution:
    def insert(self, intervals, newInterval):
        # O(logN)
        position = bisect.bisect(intervals, newInterval)
        # O(N)
        intervals.insert(position, newInterval)

        answer = []
        # O(N)
        for i in range(len(intervals)):
            if not answer or intervals[i][0] > answer[-1][1]:
                answer.append(intervals[i])
            else:
                answer[-1][1] = max(answer[-1][1], intervals[i][1])

        return answer