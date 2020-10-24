class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]: nums.pop(i) 
            else: i += 1
        print(nums)
        
        if len(nums) < 3:
            return False
        
        ranges = []
        curr = (nums[0],) if nums[0] < nums[1] else ()
        maxx = 0
        minn = 0
        for i in range(1, len(nums)):
            if nums[i] > minn and nums[i] < maxx: 
                for r in ranges:
                    if nums[i] < r[1] and nums[i] > r[0]: return True 
            if i == len(nums) - 1:
                return False
            if nums[i] < nums[i + 1] and nums[i] < nums[i - 1]:
                curr = (nums[i],)
            elif nums[i] > nums[i + 1] and nums[i] > nums[i - 1]:
                curr = curr + (nums[i],)
                minn = min(minn, curr[0])
                maxx = max(maxx, curr[1])
                ranges.append(curr)
                del curr
        
        
        