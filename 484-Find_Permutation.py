class Solution:
    def findPermutation(self, s: str) -> List[int]:
        low, d_num, res = 1, 0, []
        for i, c in enumerate(s + 'I'):
            if c == 'D': d_num += 1
            elif c == 'I':
                if d_num == 0:
                    res.append(low)
                    low += 1
                else:
                    for j in range(low+d_num, low-1, -1): res.append(j)
                    low += d_num + 1
                    d_num = 0
                if i == len(s):
                    res.append(low)
        return res[:-1]
                
            