class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odds, evens = [], []
        for n in nums:
            if n % 2 == 0: evens.append(n)
            else: odds.append(n)
        
        odds.sort()
        evens.sort()
        res = []
        for e, o in zip(evens, odds): res.extend([e, o])
        return res
            
