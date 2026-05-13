class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        diff = [0] * (2 * limit + 2)
        n = len(nums)
        
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            
            low = min(a, b) + 1
            high = max(a, b) + limit
            
            diff[2] += 2
            diff[2 * limit + 1] -= 2
            
            diff[low] -= 1
            diff[high + 1] += 1
            
            diff[a + b] -= 1
            diff[a + b + 1] += 1
            
        ans = n
        current_moves = 0
        for i in range(2, 2 * limit + 1):
            current_moves += diff[i]
            ans = min(ans, current_moves)
            
        return ans
