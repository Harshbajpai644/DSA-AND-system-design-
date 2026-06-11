from collections import defaultdict

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        max_depth = 0
        stack = [(1, 0, 0)]
        
        while stack:
            node, parent, depth = stack.pop()
            if depth > max_depth:
                max_depth = depth
                
            for neighbor in adj[node]:
                if neighbor != parent:
                    stack.append((neighbor, node, depth + 1))
                    
        MOD = 10**9 + 7
        return pow(2, max_depth - 1, MOD)
