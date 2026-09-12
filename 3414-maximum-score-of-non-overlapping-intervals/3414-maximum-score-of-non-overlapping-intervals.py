
        
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            r, l, w, orig_idx = indexed_intervals[i - 1]
            prev_idx = bisect_left(right_endpoints, l)
            
            for k in range(5):
                dp[i][k] = dp[i - 1][k]
                
            for k in range(1, 5):
                prev_weight, prev_indices = dp[prev_idx][k - 1]
                cand_weight = prev_weight - w
                cand_indices = sorted(prev_indices + [orig_idx])
                cand = (cand_weight, cand_indices)
                
                if cand < dp[i][k]:
                    dp[i][k] = cand

        best_score = 0
        best_indices = []
        for k in range(1, 5):
            weight = -dp[n][k][0]
            indices = dp[n][k][1]
            if weight > best_score:
                best_score = weight
                best_indices = indices
            elif weight == best_score and indices < best_indices:
                best_indices = indices
                
        return best_indices
        