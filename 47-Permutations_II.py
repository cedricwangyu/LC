class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[nums[0]]]
        for num in nums[1:]:
            print(res)
            new = set()
            for row in res:
                a = row.copy()
                a.insert(0, num)
                new.add(tuple(a))
                for i in range(1, len(row) + 1):
                    if row[i-1] != num:
                        a = row.copy()
                        a.insert(i, num)
                        new.add(tuple(a))
            res = [list(row) for row in new]
        return res
                    
        
        