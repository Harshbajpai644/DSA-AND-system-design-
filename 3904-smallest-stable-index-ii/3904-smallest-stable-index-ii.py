
        
        suff_min = [0] * n
        suff_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suff_min[i] = min(nums[i], suff_min[i + 1])
            
        cur_max = nums[0]
        for i in range(n):
            cur_max = max(cur_max, nums[i])
            if cur_max - suff_min[i] <= k:
                return i
                
        return -1
        