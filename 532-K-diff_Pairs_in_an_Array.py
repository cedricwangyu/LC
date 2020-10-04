class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        p = {}
        res = []
        for n in nums:
            if n in p:
                res.append((p[n], n))
                
            p[n + k] = n
            #print(p)
        
        return len(set(res))
                
        