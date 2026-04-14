class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        factory_slots = []
        for pos, limit in factory:
            for _ in range(limit):
                factory_slots.append(pos)
        
        n, m = len(robot), len(factory_slots)
        
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            dp[i][0] = float('inf')
            
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                use_factory = dp[i - 1][j - 1] + abs(robot[i - 1] - factory_slots[j - 1])
                skip_factory = dp[i][j - 1]
                dp[i][j] = min(use_factory, skip_factory)
        
        return dp[n][m]