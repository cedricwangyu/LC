class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0: return False
        if nums[0] == target or nums[-1] == target: return True
        while len(nums) > 1 and nums[1] == nums[0]:
            nums.pop(1)
        while len(nums) > 1 and nums[-2] == nums[-1]:
            nums.pop()
            
        if nums[0] >= nums[-1]:
            left, right = 0, len(nums) - 1
            while right - left > 1:
                mid = (right + left) // 2
                if nums[mid] > nums[left]:
                    left = mid
                else:
                    right = mid
            
            nums = nums[right:] + nums[:left+1]
        
        if nums[0] == target or nums[-1] == target: return True
        left, right = 0, len(nums) - 1
        while right - left > 1:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
        
        return False
                    
                
        