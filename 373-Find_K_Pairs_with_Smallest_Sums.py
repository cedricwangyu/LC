import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        p = [(num + nums2[0], i, 0) for (i, num) in enumerate(nums1)]
        heapq.heapify(p)
        res = []
        for _ in range(k):
            if p:
                val, i, j = heapq.heappop(p)
                res.append([nums1[i], nums2[j]])
                if j+1 < len(nums2):
                    heapq.heappush(p, (nums1[i] + nums2[j+1], i, j+1))
            else:
                break
            
        return res