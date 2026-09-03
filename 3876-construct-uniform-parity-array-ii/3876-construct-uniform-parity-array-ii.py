class Solution:
    
        if min_val % 2 == 1:
            return True
        return all(x % 2 == 0 for x in nums1)
        