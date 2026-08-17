class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]
        max_left = [[0] * n for _ in range(n)]
        max_right = [[0] * n for _ in range(n)]

        for i in range(n):
            max_left[i][i] = stoneValue[i]
            max_right[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                mid = i
                total_sum = prefix[j + 1] - prefix[i]
                
                # Find mid where left_sum <= total_sum / 2
                while mid < j and (prefix[mid + 1] - prefix[i]) * 2 <= total_sum:
                    mid += 1

                res = 0
                
                # Case 1: left_sum < right_sum
                if mid - 1 >= i:
                    res = max(res, max_left[i][mid - 1])
                
                # Case 2: left_sum > right_sum
                if mid < j:
                    res = max(res, max_right[mid + 1][j])
                
                # Case 3: left_sum == right_sum
                if (prefix[mid] - prefix[i]) * 2 == total_sum:
                    res = max(res, max_left[i][mid - 1], max_right[mid][j])

                dp[i][j] = res
                max_left[i][j] = max(max_left[i][j - 1], res + total_sum)
                max_right[i][j] = max(max_right[i + 1][j], res + total_sum)

        return dp[0][n - 1]