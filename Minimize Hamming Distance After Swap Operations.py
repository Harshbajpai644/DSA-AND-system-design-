from collections import Counter

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
        
        for u, v in allowedSwaps:
            union(u, v)
            
        components = {}
        for i in range(n):
            root = find(i)
            if root not in components:
                components[root] = []
            components[root].append(i)
            
        hamming_distance = 0
        for root in components:
            indices = components[root]
            source_counts = Counter()
            target_counts = Counter()
            
            for idx in indices:
                source_counts[source[idx]] += 1
                target_counts[target[idx]] += 1
            
            matches = 0
            for val in source_counts:
                if val in target_counts:
                    matches += min(source_counts[val], target_counts[val])
            
            hamming_distance += (len(indices) - matches)
            
        return hamming_distance
