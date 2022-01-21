class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total, m = 0, [-1, float('Inf')] 
        for i in range(len(gas)): 
            curr = gas[i] - cost[i]
            total += curr
            if total < m[1]: m[0], m[1] = i, total
        if total >= 0: return (m[0] + 1) % len(gas)
        else: return -1
