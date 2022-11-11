class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write_idx = 0
        for num in nums[1:]:
            if num > nums[write_idx]:
                write_idx += 1
                nums[write_idx] = num
        return write_idx + 1
        