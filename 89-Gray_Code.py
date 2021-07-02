class Solution:
    def grayCode(self, n: int) -> List[int]:
        def instructions(m):
            if m == 1: return [n-1]
            else: 
                old = instructions(m-1)
                return old + [n-m] + old
        curr, res = '0' * n, [0]
        for index in instructions(n):
            if curr[index] is '0': curr = curr[:index] + '1' + curr[index+1:]
            else: curr = curr[:index] + '0' + curr[index+1:]
            res.append(int(curr, 2))
        return res
