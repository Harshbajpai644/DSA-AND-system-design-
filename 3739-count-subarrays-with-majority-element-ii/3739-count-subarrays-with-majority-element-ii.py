class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        pref = [0] * (n + 1)
        for i in range(n):
            val = 1 if nums[i] == target else -1
            pref[i + 1] = pref[i] + val
            
        unique_vals = sorted(list(set(pref)))
        ranks = {val: i + 1 for i, val in enumerate(unique_vals)}
        
        m = len(unique_vals)
        bit = [0] * (m + 1)
        
        def update(idx, delta):
            while idx <= m:
                bit[idx] += delta
                idx += idx & (-idx)
                
        def query(idx):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s
            
        ans = 0
        for p in pref:
            r = ranks[p]
            ans += query(r - 1)
            update(r, 1)
            
        return ans  