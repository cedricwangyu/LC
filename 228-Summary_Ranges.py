class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        
        curr = str(nums[0])
        last = nums.pop(0)
        res = []
        while nums != []:
            if nums[0] != last + 1:
                if last == int(curr):
                    res.append(curr)
                else:
                    res.append(curr + "->" + str(last))
                    
                curr = str(nums[0])
            last = nums.pop(0)
        
        if last == int(curr):
            res.append(curr)
        else:
            res.append(curr + "->" + str(last))
            
        print(res)
        return res