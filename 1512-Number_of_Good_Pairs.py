from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter, res = Counter(nums), 0
        for num in counter:
            res += counter[num] * (counter[num] - 1) // 2

        return res