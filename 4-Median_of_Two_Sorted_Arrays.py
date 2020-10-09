import math

def median(nums):
    I = int(len(nums) / 2)
    if len(nums) % 2 == 0:
        return I - 0.5, (nums[I - 1] + nums[I])/2
    else:
        return I, nums[I]
    
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        if nums2 == []:
            _, m = median(nums1)
            return m

        while len(nums2) > 2:
            print(nums1)
            print(nums2)
            i1, m1 = median(nums1)
            i2, m2 = median(nums2)
            if m1 == m2:
                return m1
            elif m1 > m2:
                nums1 = nums1[:len(nums1) - math.floor(i2)]
                nums2 = nums2[math.floor(i2):]
            else:
                nums1 = nums1[len(nums2) - math.ceil(i2) - 1:]
                nums2 = nums2[:math.ceil(i2)+1]
                
        print(nums1)
        print(nums2)
        nums = nums1 + nums2
        nums.sort()
        _, m = median(nums)
        return m
        
                
            