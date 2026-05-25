class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        reachable = [False] * n
        reachable[0] = True
        
        prev_count = 0  # # of reachable indices in current window
        
        for j in range(1, n):
            # Expand window: add index (j - minJump) if it just entered range
            if j >= minJump and reachable[j - minJump]:
                prev_count += 1
            
            # Shrink window: remove index (j - maxJump - 1) if it left range
            if j > maxJump and reachable[j - maxJump - 1]:
                prev_count -= 1
            
            # Mark j reachable if window has any reachable index and s[j] == '0'
            if prev_count > 0 and s[j] == '0':
                reachable[j] = True
        
        return reachable[n - 1]
