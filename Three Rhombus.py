class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sums = set()

        for i in range(m):
            for j in range(n):
                sums.add(grid[i][j])
                
                for s in range(1, 50):
                    top = i - s
                    bottom = i + s
                    left = j - s
                    right = j + s
                    
                    if top < 0 or bottom >= m or left < 0 or right >= n:
                        break
                    
                    current_sum = 0
                    
                    for k in range(s):
                        current_sum += grid[top + k][j + k]
                        current_sum += grid[i + k][right - k]
                        current_sum += grid[bottom - k][j - k]
                        current_sum += grid[i - k][left + k]
                    
                    sums.add(current_sum)
        
        return sorted(list(sums), reverse=True)[:3]