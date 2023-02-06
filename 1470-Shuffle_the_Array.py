class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left, right = 1, n
        while right < 2*n:
            nums.insert(left, nums.pop(right))
            left += 2
            right += 1
            
        return nums