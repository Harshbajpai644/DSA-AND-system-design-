class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        # last_seen maps a value we are LOOKING FOR to its most recent index
        # key: reverse(nums[i]), value: i
        last_seen = {}
        min_dist = float('inf')
        
        for j, val in enumerate(nums):
            # 1. If current val is in last_seen, we found a mirror pair (i, j)
            if val in last_seen:
                min_dist = min(min_dist, j - last_seen[val])
            
            # 2. Calculate the reverse of the current number to help future pairs
            # Example: val = 120, reversed_val = 21
            reversed_val = int(str(val)[::-1])
            
            # 3. Store/Update the index. We always want the largest i (closest to future j)
            last_seen[reversed_val] = j
            
        return min_dist if min_dist != float('inf') else -1
