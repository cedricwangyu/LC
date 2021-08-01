class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        graph = defaultdict(list)
        for index, cost in enumerate(wells):
            graph[0].append((cost, index + 1))
        for house_1, house_2, cost in pipes:
            graph[house_1].append((cost, house_2))
            graph[house_2].append((cost, house_1))
        mst_set = set([0])
        heapq.heapify(graph[0])
        edges_heap = graph[0]
        total_cost = 0
        while len(mst_set) < n + 1:
            cost, next_house = heapq.heappop(edges_heap)
            if next_house not in mst_set:
                mst_set.add(next_house)
                total_cost += cost
                for new_cost, neighbor_house in graph[next_house]:
                    if neighbor_house not in mst_set:
                        heapq.heappush(edges_heap, (new_cost, neighbor_house))
        return total_cost
