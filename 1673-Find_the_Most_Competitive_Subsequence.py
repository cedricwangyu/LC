class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = [nums[0]]
        for i, n in enumerate(nums[1:]):
            poped = None
            while len(stack) > 0 and n < stack[-1] and len(nums) - i - 1 > k - len(stack): poped = stack.pop()
            if poped is not None or len(stack) < k: stack.append(n)
            
        return stack
            
        