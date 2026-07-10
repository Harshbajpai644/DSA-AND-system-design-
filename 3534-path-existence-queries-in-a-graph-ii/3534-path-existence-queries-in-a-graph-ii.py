from typing import List
import bisect

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
     
        unique_vals = sorted(list(set(nums)))
        m = len(unique_vals)
        
      
        val_to_idx = {val: i for i, val in enumerate(unique_vals)}
        
       
        LOG = 18
       
        succ = [[0] * LOG for _ in range(m)]
        
        
        for i in range(m):
            target = unique_vals[i] + maxDiff
            
            idx = bisect.bisect_right(unique_vals, target) - 1
            succ[i][0] = idx
            
        
        for j in range(1, LOG):
            for i in range(m):
                nxt = succ[i][j - 1]
                succ[i][j] = succ[nxt][j - 1]
                
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            val_u, val_v = nums[u], nums[v]
            if val_u == val_v:
                ans.append(1)
                continue
                
            if val_u > val_v:
                val_u, val_v = val_v, val_u
                
            curr_idx = val_to_idx[val_u]
            target_idx = val_to_idx[val_v]
            
            steps = 0
            possible = True
            
            
            for j in range(LOG - 1, -1, -1):
                if succ[curr_idx][j] < target_idx:
                    if succ[curr_idx][j] == curr_idx:
                        possible = False
                        break
                    curr_idx = succ[curr_idx][j]
                    steps += (1 << j)
                    
            if not possible:
                ans.append(-1)
                continue
                
          
            if succ[curr_idx][0] >= target_idx:
                ans.append(steps + 1)
            else:
                ans.append(-1)
                
        return ans