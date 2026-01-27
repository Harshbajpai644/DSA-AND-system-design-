import heapq
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        inc = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            inc[v].append((u, w))

        INF = 10**18
        dist = [[INF, INF] for _ in range(n)]
        dist[0][0] = 0
        pq = [(0, 0, 0)]  

        while pq:
            d, u, s = heapq.heappop(pq)
            if d != dist[u][s]:
                continue

            if u == n - 1:
                return d

           
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v][s]:
                    dist[v][s] = nd
                    heapq.heappush(pq, (nd, v, s))

            
            if s == 0:
                for x, w in inc[u]:
                    nd = d + 2 * w
                    if nd < dist[x][0]:
                        dist[x][0] = nd
                        heapq.heappush(pq, (nd, x, 0))

        return -1