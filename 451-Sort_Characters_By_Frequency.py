class Solution:
    def frequencySort(self, s: str) -> str:
        p = collections.Counter(s)
        q = defaultdict(list)
        for k in p: q[p[k]].append(k)
        res = ""
        for v in sorted(q.keys(), reverse=True):
            for c in q[v]:
                res += c * v
        return res
