from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        bar = len(nums) // 3
        res = []
        for num in c:
            if c[num] > bar:
                res.append(num)
        
        return res
        