class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        p = {}
        for x, y in trees:
            if x in p: p[x][0], p[x][1] = min(p[x][0], y), max(p[x][1], y)
            else: p[x] = [y, y]
        xr, hi, lo = sorted(p.keys()), [], []
        for x in xr:
            if len(lo) < 2: lo.append([x, p[x][0]])
            else: 
                curr_t, prev_t = (p[x][0] - lo[-1][1]) / (x - lo[-1][0]), (lo[-1][1] - lo[-2][1]) / (lo[-1][0] - lo[-2][0])
                while len(lo) >= 2 and curr_t < prev_t:
                    lo.pop()
                    if len(lo) < 2: break
                    curr_t, prev_t = (p[x][0] - lo[-1][1]) / (x - lo[-1][0]), (lo[-1][1] - lo[-2][1]) / (lo[-1][0] - lo[-2][0])
                lo.append([x, p[x][0]])
            if len(hi) < 2: hi.append([x, p[x][1]])
            else:
                curr_t, prev_t = (p[x][1] - hi[-1][1]) / (x - hi[-1][0]), (hi[-1][1] - hi[-2][1]) / (hi[-1][0] - hi[-2][0])
                while len(hi) >= 2 and curr_t > prev_t:
                    hi.pop()
                    if len(hi) < 2: break
                    curr_t, prev_t = (p[x][1] - hi[-1][1]) / (x - hi[-1][0]), (hi[-1][1] - hi[-2][1]) / (hi[-1][0] - hi[-2][0])
                hi.append([x, p[x][1]])
        print(hi, lo)
        xl, xr, res, hi, lo = hi[0][0], hi[-1][0], [], hi[1:-1], lo[1:-1]
        for x, y in trees:
            if x in (xl, xr): res.append([x, y])
        while len(hi) > 0 and len(lo) > 0:
            if hi[0][0] < lo[0][0]: res.append(hi.pop(0))
            elif hi[0][0] > lo[0][0]: res.append(lo.pop(0))
            elif hi[0][1] == lo[0][1]: 
                res.append(hi.pop(0))
                lo.pop(0)
            else:
                res.append(hi.pop(0))
                res.append(lo.pop(0))
        res.extend(hi+lo)
        return res
