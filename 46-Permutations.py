class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        status = [True] * len(nums)
        def helper(curr, status):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for i,num in enumerate(nums):
                if status[i]:
                    curr.append(num)
                    status[i] = False
                    helper(curr, status)
                    status[i] = True
                    curr.pop()
        
        helper([], status)
        return res
            