class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n, res = len(nums1), len(nums2), 0
        for pos in range(-m+1,n):
            l1, r1, l2, r2, curr =  max(0, -pos), min(m, n - pos), max(0, pos), min(n, pos + m), 0
            for w1, w2 in zip(nums1[l1:r1], nums2[l2:r2]):
                if w1 == w2: curr += 1
                else: curr = 0
                res = max(res, curr)
        return res