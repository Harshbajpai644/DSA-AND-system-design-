class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        R = len(grid)
        C = len(grid[0])
        
        diff_pref = [[0] * (C + 1) for _ in range(R + 1)]
        x_count_pref = [[0] * (C + 1) for _ in range(R + 1)]
        
        res = 0
        
        for r in range(R):
            for c in range(C):
                val = 0
                is_x = 0
                if grid[r][c] == 'X':
                    val = 1
                    is_x = 1
                elif grid[r][c] == 'Y':
                    val = -1
                
                diff_pref[r+1][c+1] = val + diff_pref[r][c+1] + diff_pref[r+1][c] - diff_pref[r][c]
                x_count_pref[r+1][c+1] = is_x + x_count_pref[r][c+1] + x_count_pref[r+1][c] - x_count_pref[r][c]
                
                if diff_pref[r+1][c+1] == 0 and x_count_pref[r+1][c+1] > 0:
                    res += 1
                    
        return res