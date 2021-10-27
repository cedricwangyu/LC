class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, t = 0, 0
        while i < len(nums)-t:
            if nums[i] == 0: 
                nums.insert(0, nums.pop(i))
                i += 1
            elif nums[i] == 2: 
                nums.append(nums.pop(i))
                t += 1
            else: i += 1
        return nums