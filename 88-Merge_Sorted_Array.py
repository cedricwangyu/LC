class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        del nums1[m:]
        del nums2[n:]
        if len(nums1) == 0 or len(nums2) == 0: 
            nums1.extend(nums2)
            return nums1
        i = 0
        while (i < len(nums1) and len(nums2) > 0):
            if nums1[i] >= nums2[0]: nums1.insert(i, nums2.pop(0))
            i += 1
        nums1.extend(nums2)