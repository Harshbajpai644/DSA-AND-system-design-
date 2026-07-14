from math import gcd
from collections import defaultdict
from typing import List

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        max_val = max(nums)
        

        dp = defaultdict(int)
        dp[(0, 0)] = 1
        
        for x in nums:
            next_dp = defaultdict(int)
            
            for (g1, g2), count in dp.items():
               
                next_dp[(g1, g2)] = (next_dp[(g1, g2)] + count) % MOD
                
               
                new_g1 = x if g1 == 0 else gcd(g1, x)
                next_dp[(new_g1, g2)] = (next_dp[(new_g1, g2)] + count) % MOD
                
                
                new_g2 = x if g2 == 0 else gcd(g2, x)
                next_dp[(g1, new_g2)] = (next_dp[(g1, new_g2)] + count) % MOD
                
            dp = next_dp
            
      
        ans = 0
        for (g1, g2), count in dp.items():
            if g1 == g2 and g1 > 0:
                ans = (ans + count) % MOD
                
        return ans