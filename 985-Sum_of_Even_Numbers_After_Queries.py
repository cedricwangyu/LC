class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = [sum(val for val in nums if val % 2 == 0)]
        for val, ind in queries:
            if nums[ind] % 2 == 0:
                if val % 2 == 0:
                    res.append(res[-1] + val)
                else:
                    res.append(res[-1] - nums[ind])
            else:
                if val % 2 == 0:
                    res.append(res[-1])
                else:
                    res.append(res[-1] + val + nums[ind])
            nums[ind] += val
        return res[1:]