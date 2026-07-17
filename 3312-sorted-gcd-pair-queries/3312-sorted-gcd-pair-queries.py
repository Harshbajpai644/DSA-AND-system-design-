from typing import List

import bisect

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        
        freq = [0] * (max_val + 1)
        for num in nums:
            freq[num] += 1
            
        cnt = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            for j in range(i, max_val + 1, i):
                cnt[i] += freq[j]
                
 
        exact_gcd_cnt = [0] * (max_val + 1)
        for i in range(max_val, 0, -1):
            total_pairs = cnt[i] * (cnt[i] - 1) // 2
            
            
            minus = 0
            for j in range(2 * i, max_val + 1, i):
                minus += exact_gcd_cnt[j]
                
            exact_gcd_cnt[i] = total_pairs - minus
            
       
        pref = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            pref[i] = pref[i - 1] + exact_gcd_cnt[i]
            
        ans = []
        for q in queries:
            idx = bisect.bisect_right(pref, q)
            ans.append(idx)
            
        return ans