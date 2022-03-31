class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def is_done(maxi):
            curr_num, curr = 0, 0
            for num in nums:
                if curr+num <= maxi: curr += num
                else: curr_num, curr = curr_num+1, num
                if curr_num >= m: return False
            return False if curr_num >= m else True
        
        l, r = 0, 0
        for num in nums: 
            l, r = max(l, num), r+num
        
        
        if is_done(l): return l
        while r-l>1:
            mid = (r+l) // 2
            if is_done(mid): r = mid
            else: l = mid
                
        return r
            
            
            