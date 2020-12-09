class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        bounds = [[lower, upper]]
        b = 0
        i = 0
        while i < len(nums):
            if nums[i] == bounds[b][0] and nums[i] == bounds[b][1]: bounds.pop(b)
            elif nums[i] == bounds[b][0]: bounds[b][0] = nums[i] + 1
            elif nums[i] == bounds[b][1]: bounds[b][1] = nums[i] - 1
            elif nums[i] < bounds[b][1] and nums[i] > bounds[b][0]:
                temp = bounds[b][1]
                bounds[b][1] = nums[i] - 1
                bounds.insert(b + 1, [nums[i] + 1, temp])
                b += 1
            else:
                b += 1
                continue
            i += 1
        res = []
        for b in bounds:
            if b[0] == b[1]: res.append(str(b[0]))
            else: res.append(str(b[0]) + "->" + str(b[1]))
        return res
            
        