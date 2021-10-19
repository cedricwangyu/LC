class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        p = {}
        for n in nums2:
            p[n] = -1
            for m in p:
                if n > m and p[m] < 0: p[m] = n
        return [p[n] for n in nums1]
