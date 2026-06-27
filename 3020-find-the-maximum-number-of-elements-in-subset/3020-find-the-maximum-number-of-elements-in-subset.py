from collections import Counter
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0
        
        if 1 in count:
            ans = count[1] if count[1] % 2 == 1 else count[1] - 1

        for x in list(count.keys()):
            if x == 1:
                continue
            
            current_len = 0
            curr = x
            
            while curr in count and count[curr] >= 2:
                current_len += 2
                curr = curr * curr
                
            if curr in count and count[curr] >= 1:
                current_len += 1
            else:
                current_len -= 1
                
            ans = max(ans, current_len)
            
        return ans