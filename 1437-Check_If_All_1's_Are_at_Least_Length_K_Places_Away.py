class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        res = k
        for num in nums:
            if num == 1:
                if res < k: return False
                else: res = 0
            else: res += 1
        return True
