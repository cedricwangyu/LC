import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        h, res, curr = [], 0, 0
        for a, b in sorted(zip(nums2, nums1), reverse=True):
            if len(h) < k:
                heapq.heappush(h, b)
                curr += b
                if len(h) == k:
                    res = curr * a
            elif b > h[0]:
                curr -= heapq.heappushpop(h, b)
                curr += b
                res = max(res, curr * a)

        return res