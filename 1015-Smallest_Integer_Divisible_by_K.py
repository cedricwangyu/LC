class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        def isallones(k):
            return str(k) == '1'*len(str(k))
        def helper(k, remain, res):
            one = int(str(k)[-1])
            for i in range(10):
                if (one * i + int(str(remain)[-1])) % 10 == 1:
                    remain = (k * i + remain) // 10
                    if isallones(remain):
                        return res + 1 + len(str(remain))
                    elif remain == 0:
                        return res + 1
                    else:
                        return helper(k, remain, res + 1)
                        
            else: return -1
        
        if int(str(K)[-1]) in [1,3,7,9]: res = helper(K, 0, 0)
        else: res = -1
        return res
                    
            