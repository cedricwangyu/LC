class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1, c2 = collections.Counter(nums1), collections.Counter(nums2)
        res = []
        for c in c1:
            if c in c2: res += [c] * min(c1[c], c2[c])
        return res
