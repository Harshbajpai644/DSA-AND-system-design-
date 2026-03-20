class Solution:
    def minAbsDiff(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                kgrid = []
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        kgrid.append(grid[x][y])
                
                kgrid.sort()
                
                current_min = float("inf")
                has_duplicates = False
                
                for t in range(1, len(kgrid)):
                    diff = kgrid[t] - kgrid[t-1]
                    if diff == 0:
                        has_duplicates = True
                        break
                    if diff < current_min:
                        current_min = diff
                
                if has_duplicates:
                    res[i][j] = 0
                elif current_min == float("inf"):
                    res[i][j] = 0
                else:
                    res[i][j] = current_min
                    
        return res