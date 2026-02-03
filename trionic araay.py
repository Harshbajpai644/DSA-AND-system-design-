class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:
            return False
            
        def is_increasing(arr):
            if len(arr) < 2: return False
            for i in range(len(arr) - 1):
                if arr[i] >= arr[i+1]:
                    return False
            return True
            
        def is_decreasing(arr):
            if len(arr) < 2: return False
            for i in range(len(arr) - 1):
                if arr[i] <= arr[i+1]:
                    return False
            return True

        for p in range(1, n - 2):
            if not is_increasing(nums[:p+1]):
                continue
                
            for q in range(p + 1, n - 1):
                if is_decreasing(nums[p:q+1]) and is_increasing(nums[q:]):
                    return True
                    
        return False