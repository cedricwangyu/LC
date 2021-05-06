class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0
        q, visited = [0], [None] * len(nums)
        visited[0] = 0
        while len(q) > 0:
            curr = q.pop(0)
            for i in range(max(0, curr - nums[curr]), min(len(nums), curr + nums[curr] + 1)):
                if visited[i] is None: 
                    visited[i] = curr
                    q.append(i)
                    if i == len(nums) - 1:
                        res, curr = 0, len(nums) - 1
                        while curr != 0:
                            res += 1
                            curr = visited[curr]
                        return res