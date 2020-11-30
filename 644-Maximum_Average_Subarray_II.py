class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        def check(mid):
            right = sum([item - mid for item in nums[:k]])
            if right >= 0: return True
            left, min_left = 0, 0
            for i in range(k, len(nums)):
                right += nums[i] - mid
                left += nums[i - k] - mid
                min_left = min(left, min_left)
                if right >= min_left: return True
            return False
        
        if k >= len(nums): return sum(nums) / len(nums)
        Max, Min = max(nums), min(nums)
        while (Max - Min) > 0.00001:
            Mid = (Max + Min) / 2
            if check(Mid): Min = Mid
            else: Max = Mid
        
        return Max
    

    
   
    
    
            
        
                
            
            
        