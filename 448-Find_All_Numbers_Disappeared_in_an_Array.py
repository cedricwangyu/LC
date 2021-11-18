class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n, nums = len(nums), set(nums)
        return [i for i in range(1, n+1) if i not in nums]
