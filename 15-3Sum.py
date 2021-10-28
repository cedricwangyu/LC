class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        p, res = defaultdict(set), set()
        for i, a in enumerate(nums[1:]):
            if a in p:
                for aa, bb in p[a]: 
                    if a < aa: res.add((a, aa, bb))
                    elif a > bb: res.add((aa, bb, a))
                    else: res.add((aa, a, bb))
            for b in nums[:i+1]: 
                if a > b: p[-a-b].add((b, a))
                else: p[-a-b].add((a, b))
        return res
        