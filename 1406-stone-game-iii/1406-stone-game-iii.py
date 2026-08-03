from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            max_score_diff = float('-inf')
            current_take = 0
            
            for k in range(1, 4):
                if i + k <= n:
                    current_take += stoneValue[i + k - 1]
                    max_score_diff = max(max_score_diff, current_take - dp[i + k])
            
            dp[i] = max_score_diff
            
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"