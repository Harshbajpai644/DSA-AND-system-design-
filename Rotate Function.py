class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        
        # Calculate F(0)
        current_f = 0
        for i in range(n):
            current_f += i * nums[i]
            
        max_f = current_f
        
        # Iteratively calculate F(1) to F(n-1) using the derived formula
        # We rotate clockwise, so the element that was at the end 
        # moves to the front and loses its (n-1) multiplier.
        for k in range(1, n):
            # The element that drops from (n-1)*val to 0*val is nums[n-k]
            current_f = current_f + s - n * nums[n - k]
            if current_f > max_f:
                max_f = current_f
                
        return max_f
