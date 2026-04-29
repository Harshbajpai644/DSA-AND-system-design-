class Solution:
    def maximumScore(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        pref = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            for i in range(n):
                pref[j][i + 1] = pref[j][i] + grid[i][j]
        
        dp = [[-1] * (n + 1) for _ in range(2)]
        for h in range(n + 1):
            dp[0][h] = 0
            
        for j in range(1, n + 1):
            next_dp = [[-1] * (n + 1) for _ in range(2)]
            
            for prev_h in range(n + 1):
                for curr_h in range(n + 1):
                    # Case 1: Current height is greater than or equal to previous height
                    if curr_h >= prev_h:
                        score = pref[j - 1][curr_h] - pref[j - 1][prev_h]
                        if dp[0][prev_h] != -1:
                            next_dp[0][curr_h] = max(next_dp[0][curr_h], dp[0][prev_h] + score)
                        if dp[1][prev_h] != -1:
                            next_dp[0][curr_h] = max(next_dp[0][curr_h], dp[1][prev_h] + score)
                            
                    # Case 2: Current height is less than previous height
                    else:
                        score = pref[j][prev_h] - pref[j][curr_h]
                        if dp[1][prev_h] != -1:
                            next_dp[1][curr_h] = max(next_dp[1][curr_h], dp[1][prev_h] + score)
                        
                        # When transitioning from "increasing" to "decreasing", 
                        # we can pick the best from the previous increasing state
                        if dp[0][prev_h] != -1:
                            next_dp[1][curr_h] = max(next_dp[1][curr_h], dp[0][prev_h])
            
            # Special case: allow jumping from any height at column j-2 
            # to a 0-height at j-1 to reset the "valley"
            best_prev = max(max(dp[0]), max(dp[1]))
            next_dp[0][0] = max(next_dp[0][0], best_prev)
            
            dp = next_dp
            
        return max(max(dp[0]), max(dp[1]))
