class Solution:
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        dic = defaultdict(dict)
        for x, y, t in times:
            dic[x][y] = t
        heap = [(0, k)]
        seen = set()
        res = 0
        while heap:
            time, curr = heapq.heappop(heap)
            seen.add(curr)
            
            if len(seen) == n: return time
            for other in dic[curr]:
                if other not in seen:
                    heapq.heappush(heap, (dic[curr][other] + time, other))
        return -1