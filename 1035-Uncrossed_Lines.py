class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp1, dp2 = [0] * len(nums2), [0] * len(nums2)
        for i in range(len(nums1)-1, -1, -1):
            dp1[-1] = max(dp2[-1], int(nums1[i] == nums2[-1])) 
            for j in range(len(nums2)-2, -1, -1):
                dp1[j] = max(dp1[j+1], dp2[j], dp2[j+1] + int(nums1[i] == nums2[j]))
            dp1, dp2 = dp2, dp1

        return dp2[0]