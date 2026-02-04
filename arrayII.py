class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp0 = [-float('inf')] * n
        dp1 = [-float('inf')] * n
        dp2 = [-float('inf')] * n
        dp3 = [-float('inf')] * n
        
        dp0[0] = nums[0]
        max_sum = -float('inf')
        
        for i in range(1, n):
            dp0[i] = nums[i]
            
            if nums[i] > nums[i-1]:
                dp1[i] = max(dp0[i-1], dp1[i-1]) + nums[i]
                
                if dp2[i-1] != -float('inf') or dp3[i-1] != -float('inf'):
                    dp3[i] = max(dp2[i-1], dp3[i-1]) + nums[i]
            
            elif nums[i] < nums[i-1]:
                if dp1[i-1] != -float('inf') or dp2[i-1] != -float('inf'):
                    dp2[i] = max(dp1[i-1], dp2[i-1]) + nums[i]
            
            max_sum = max(max_sum, dp3[i])
            
        return max_sum