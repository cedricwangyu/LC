from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        curr, p, res = 0, defaultdict(int), 0
        for j, num in enumerate(n % k for n in nums):
            p[curr % k] += 1
            curr = (curr + num) % k
            if curr in p:
                res += p[curr]

        return res