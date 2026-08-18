class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        
        if k == 1:
            freq = Counter(nums)
            valid = [x for x, count in freq.items() if count == 1]
            return max(valid) if valid else -1
        
        # Case 2: k = n
        if k == n:
            return max(nums)
            
        # Case 3: 1 < k < n
        ans = -1
        if nums.count(nums[0]) == 1:
            ans = max(ans, nums[0])
        if nums.count(nums[-1]) == 1:
            ans = max(ans, nums[-1])
            
        return ans