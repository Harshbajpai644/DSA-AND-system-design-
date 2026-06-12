import sys
from collections import defaultdict

sys.setrecursionlimit(200000)

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        LOG = 18
        up = [[1] * LOG for _ in range(n + 1)]
        depth = [0] * (n + 1)
        
        def dfs(node, parent, d):
            depth[node] = d
            up[node][0] = parent
            for i in range(1, LOG):
                up[node][i] = up[up[node][i - 1]][i - 1]
            for neighbor in adj[node]:
                if neighbor != parent:
                    dfs(neighbor, node, d + 1)
                    
        dfs(1, 1, 0)
        
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            
            diff = depth[u] - depth[v]
            for i in range(LOG):
                if (diff >> i) & 1:
                    u = up[u][i]
                    
            if u == v:
                return u
                
            for i in range(LOG - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
                    
            return up[u][0]
            
        MOD = 10**9 + 7
        
        powers_of_two = [1] * (n + 1)
        for i in range(1, n + 1):
            powers_of_two[i] = (powers_of_two[i - 1] * 2) % MOD
            
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            lca = get_lca(u, v)
            L = depth[u] + depth[v] - 2 * depth[lca]
            ans.append(powers_of_two[L - 1])
            
        return ans
