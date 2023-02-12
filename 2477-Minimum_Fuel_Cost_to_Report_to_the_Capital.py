from math import ceil
from collections import defaultdict
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        self.seats = seats
        self.p = defaultdict(set)
        for a, b in roads:
            self.p[a].add(b)
            self.p[b].add(a)
        self.seen = {0,}
        def dfs(node):
            num, fuel = 1, 0
            for sub_node in self.p[node]:
                if sub_node in self.seen:
                    continue
                self.seen.add(sub_node)
                new_num, new_fuel = dfs(sub_node)
                num += new_num
                fuel += new_fuel + ceil(new_num / self.seats)
            
            return num, fuel
        
        _, res = dfs(0)