class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = list(nums)

        for length in range(2, n + 1):
            
                dp[i] = max(nums[i] - dp[i + 1], nums[j] - dp[i])

        return dp[0] >= 0