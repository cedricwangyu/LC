class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total, n, maxi, left, current = sum(nums), len(nums), -1, 0, 0
        for right in range(n):
            current += nums[right]
            while current > total-x and left <= right:
                current -= nums[left]
                left += 1
            if current == total-x: maxi = max(maxi, right-left+1)
        return n-maxi if maxi != -1 else -1