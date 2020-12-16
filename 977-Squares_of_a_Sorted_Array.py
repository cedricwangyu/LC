class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right, mid = 0, len(nums) - 1, 0
        if nums[left] >= 0: mid = left
        elif nums[right] <= 0: mid = right
        while right - left > 1:
            mid = (left + right) // 2
            if nums[mid] >= 0: right = mid
            elif nums[mid] < 0: left = mid
        
        if abs(nums[right]) <= abs(nums[left]): mid = right
        else: mid = left
        
        res = [nums[mid] ** 2]
        left = 1
        right = 1
        while mid - left >= 0 and mid + right < len(nums):
            if abs(nums[mid - left]) <= abs(nums[mid + right]):
                res.append(nums[mid - left] ** 2)
                left += 1
            else:
                res.append(nums[mid + right] ** 2)
                right += 1
        if mid - left < 0: res = res + [item ** 2 for item in nums[mid + right:]]
        elif mid + right >= len(nums): res = res + [item ** 2 for item in nums[mid - left::-1]]
        return res