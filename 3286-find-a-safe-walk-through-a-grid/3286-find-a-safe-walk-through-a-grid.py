from collections import deque
from typing import List

)
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c = queue.popleft()
            
            if r == m - 1 and c == n - 1:
                break
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    weight = grid[nr][nc]
                    if dist[r][c] + weight < dist[nr][nc]:
                        dist[nr][nc] = dist[r][c] + weight
                        if weight == 0:
                            queue.appendleft((nr, nc))
                        else:
                            queue.append((nr, nc))
                            
        return dist[m - 1][n - 1] < health