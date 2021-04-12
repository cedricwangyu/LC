class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        l, r, i, res = 1, k + 1, 1, []
        while True:
            if i % 2 == 1:
                res.append(l)
                l += 1
            else:
                res.append(r)
                r -= 1
            if l == r:
                res.append(l)
                break
            i += 1
        res.extend(i for i in range(k+2, n+1))
        return res
