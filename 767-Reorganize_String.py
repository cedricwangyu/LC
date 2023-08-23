import heapq as hq
import collections as co
class Solution:
    def reorganizeString(self, s: str) -> str:
        p = co.Counter(s)
        q = [(-p[k], k) for k in p]
        hq.heapify(q)
        temp = None
        res = ""
        while q:
            count, key = hq.heappop(q)
            if temp is not None:
                hq.heappush(q, temp)
            res += key
            temp = (count+1, key) if count < -1 else None
        return res if len(res) == len(s) else ""
