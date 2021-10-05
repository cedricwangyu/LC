# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        self.res = n
        def bisect_loc(i):
            if binaryMatrix.get(i, 0): 
                self.res = 0
                return
            if not binaryMatrix.get(i, n-1): return
            l, r = 0, n-1
            while r-l>1:
                m = (l+r)//2
                if binaryMatrix.get(i, m): r = m
                else:
                    if m >= self.res: return
                    l = m
            self.res = r
        for i in range(m): bisect_loc(i)
        return self.res if self.res < n else -1
