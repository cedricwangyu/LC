class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N, res = len(nums), []
        for i in range(2 ** N):
            mask, curr = format(i, "b"), []
            if len(mask) < N: mask = "0" * (N-len(mask)) + mask
            for m, n in zip(mask, nums):
                if m == "1": curr.append(n)
            res.append(curr)
        return res
                