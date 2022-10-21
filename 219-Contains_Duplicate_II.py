class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) <= k: return len(set(nums)) < len(nums)
        curr = set(nums[:k])
        if len(curr) < k: return True
        for i, num in enumerate(nums[k:]):
            curr.add(num)
            if len(curr) < k+1: return True
            curr.remove(nums[i])
            
        return False
        