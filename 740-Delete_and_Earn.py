class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        p, max_num = collections.defaultdict(int), 0
        for n in nums:
            p[n] += n
            max_num = max(max_num, n)
        
        @functools.lru_cache(maxsize=max_num+1)
        def dp(num):
            if num <= 0: return p[num]
            return max(dp(num-1), dp(num-2) + p[num])
        
        return dp(max_num)
        
        
        
        
                