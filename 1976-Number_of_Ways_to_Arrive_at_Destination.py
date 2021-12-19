from collections import defaultdict
from heapq import heappop, heappush
from math import inf
from typing import List

MAX_SIZE = 10 ** 9 + 7


def create_graph(edges: List[List[int]]):
    g = defaultdict(list)

    for u, v, t in edges:
        g[u].append((v, t))
        g[v].append((u, t))

    return g


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        g = create_graph(roads)

        times, cnt = [inf] * n, [0] * n
        cnt[0] = 1

        pq = [(0, 0)]  # (time, node)

        while pq:
            tu, u = heappop(pq)

            for v, t_uv in g[u]:
                if times[v] == (new_time := tu + t_uv):
                    cnt[v] = (cnt[v] + cnt[u]) % MAX_SIZE
                elif times[v] > new_time:
                    cnt[v] = cnt[u]
                    times[v] = new_time
                    heappush(pq, (new_time, v))

        return cnt[-1]
