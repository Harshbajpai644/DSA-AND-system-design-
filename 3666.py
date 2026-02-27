from collections import deque

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        z0 = s.count('0')
        
        if z0 == 0:
            return 0
            
        next_node = [list(range(n + 3)), list(range(n + 3))]
        
        def get_next(p, i):
            if next_node[p][i] == i:
                return i
            next_node[p][i] = get_next(p, next_node[p][i])
            return next_node[p][i]

        dist = [-1] * (n + 1)
        dist[z0] = 0
        queue = deque([z0])
        
        next_node[z0 % 2][z0] = get_next(z0 % 2, z0 + 2)
        
        while queue:
            z = queue.popleft()
            
            low_i = max(0, k - (n - z))
            high_i = min(k, z)
            
            z_min = z + k - 2 * high_i
            z_max = z + k - 2 * low_i
            
            p = (z + k) % 2
            curr = get_next(p, z_min)
            
            while curr <= z_max:
                if dist[curr] == -1:
                    dist[curr] = dist[z] + 1
                    if curr == 0:
                        return dist[curr]
                    queue.append(curr)
                
                next_node[p][curr] = get_next(p, curr + 2)
                curr = next_node[p][curr]
                
        return dist[0]