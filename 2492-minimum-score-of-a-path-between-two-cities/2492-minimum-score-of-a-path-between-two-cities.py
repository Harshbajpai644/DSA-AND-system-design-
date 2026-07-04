from collections import defaultdict, deque
from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
       
        graph = defaultdict(list)
        for u, v, distance in roads:
            graph[u].append((v, distance))
            graph[v].append((u, distance))
        
       
      
                min_score = min(min_score, distance)
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score  