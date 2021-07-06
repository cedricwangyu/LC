class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        p = collections.Counter(arr)
        q, curr, res = sorted(p.keys(), key=lambda x: p[x], reverse=True), 0, 0
        for n in q:
            curr, res = curr + p[n], res + 1
            if curr >= len(arr) // 2: break
        return res
