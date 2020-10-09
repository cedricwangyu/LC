class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == []:
            return -1
        
        low, high = 0, len(nums) - 1
        if nums[low] == target:
            return low
        elif nums[high] == target:
            return high
        
        mid = 0
        while(high - low > 1):
            # print((low, high))
            mid = int((high + low) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid
            else:
                low = mid
                
        return -1
                
        