class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        else:
            d = [str(int(not bool(int(item)))) for item in bin(N).split('b')[1]]
            try:
                id = d.index('1')
            except:
                return 0
            d = ''.join(d[id:])
        
        return int(d,2)