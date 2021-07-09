class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        two, p, res = [2 ** i for i in range(22)], {}, 0
        for d in deliciousness:
            if d in p: res += p[d]
            for t in two:
                if t >= d:
                    if t - d in p: p[t-d] += 1
                    else: p[t-d] = 1
        return res % (10 ** 9 + 7)
