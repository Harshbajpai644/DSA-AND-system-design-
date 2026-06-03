import bisect
import math
from typing import List

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        def get_min_time(start_A: List[int], dur_A: List[int], start_B: List[int], dur_B: List[int]) -> int:
            B = sorted(zip(start_B, dur_B), key=lambda x: x[0])
            m = len(B)
            
            B_starts = [x[0] for x in B]
            
            pref_min_dur = [0] * m
            curr_min_dur = math.inf
            for i in range(m):
                if B[i][1] < curr_min_dur:
                    curr_min_dur = B[i][1]
                pref_min_dur[i] = curr_min_dur
                
            suff_min_end = [0] * m
            curr_min_end = math.inf
            for i in range(m - 1, -1, -1):
                end_time = B[i][0] + B[i][1]
                if end_time < curr_min_end:
                    curr_min_end = end_time
                suff_min_end[i] = curr_min_end
                
            ans = math.inf
            
            for s_a, d_a in zip(start_A, dur_A):
                finish_A = s_a + d_a
                
                idx = bisect.bisect_right(B_starts, finish_A) - 1
                
                if idx >= 0:
                    ans = min(ans, finish_A + pref_min_dur[idx])
                    
                if idx + 1 < m:
                    ans = min(ans, suff_min_end[idx + 1])
                    
            return ans

        order1 = get_min_time(landStartTime, landDuration, waterStartTime, waterDuration)
        order2 = get_min_time(waterStartTime, waterDuration, landStartTime, landDuration)
        
        return min(order1, order2)
