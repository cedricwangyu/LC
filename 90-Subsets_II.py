class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums, self.res = tuple(item for item in collections.Counter(nums).items()), []
        def scan(curr, idx):
            if idx >= len(nums): 
                self.res.append(curr)
                return
            for i in range(nums[idx][1]+1): scan(curr + [nums[idx][0]] * i, idx + 1)
        scan([], 0)
        return self.res
