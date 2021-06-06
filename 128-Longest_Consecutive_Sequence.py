class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums, res = list(set(nums)), 0
        pr, ne = {}, {}
        for n in nums:
            if n in pr:
                if n in ne:
                    l1, l2 = pr[n], ne[n]
                    del pr[n], ne[n]
                    pr[n-l2-1] = l1 + l2 + 1
                    ne[n+l1+1] = l1 + l2 + 1
                    res = max(res, l1 + l2 + 1)
                else:
                    pr[n-1] = pr[n] + 1
                    ne[n+pr[n]+1] += 1
                    res = max(res, pr[n-1], ne[n+pr[n]+1])
                    del pr[n]
            else:
                if n in ne:
                    ne[n+1] = ne[n] + 1
                    pr[n-ne[n]-1] += 1
                    res = max(res, ne[n+1], pr[n-ne[n]-1])
                    del ne[n]
                else: 
                    pr[n-1], ne[n+1] = 1, 1
                    res = max(res, 1)
        return res
