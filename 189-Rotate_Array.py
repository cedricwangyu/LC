class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        K = k % len(nums)
        if K == 0:
            return
        else:
            nums[:] = nums[len(nums) - K:] + nums[:len(nums) - K]
        
        print(nums)
        