class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        
        dp0 = [1] * m
        dp1 = [1] * m
        
        for _ in range(2, n + 1):
            next_dp0 = [0] * m
            next_dp1 = [0] * m
            
            prefix_sum1 = 0
            for y in range(m):
                next_dp0[y] = prefix_sum1
                prefix_sum1 = (prefix_sum1 + dp1[y]) % MOD
                
            suffix_sum0 = 0
            for y in range(m - 1, -1, -1):
                next_dp1[y] = suffix_sum0
                suffix_sum0 = (suffix_sum0 + dp0[y]) % MOD
                
            dp0 = next_dp0
            dp1 = next_dp1
            
        return (sum(dp0) + sum(dp1)) % MOD