class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        min_dist = float('inf')
        
        for i in range(n):
            if words[i] == target:
                abs_dist = abs(i - startIndex)
                current_shortest = min(abs_dist, n - abs_dist)
                min_dist = min(min_dist, current_shortest)
        
        return min_dist if min_dist != float('inf') else -1
