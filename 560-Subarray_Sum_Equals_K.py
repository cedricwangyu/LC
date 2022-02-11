class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)): nums[i] += nums[i-1]
        p, res = defaultdict(int), 0
        p[0] += 1
        for n in nums:
            if n-k in p: res += p[n-k]
            p[n] += 1
        return res
        
        
            
            