class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        pushes = 0
        
       
        
        pushes += min(n, 8) * 3
        n -= min(n, 8)
        
        pushes += n * 4
        
        return pushes 