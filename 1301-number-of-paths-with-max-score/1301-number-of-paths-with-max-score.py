class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7
        
       
        dp_score = [[-1] * n for _ in range(n)]
        
        dp_paths = [[0] * n for _ in range(n)]
        
        dp_score[n-1][n-1] = 0
        dp_paths[n-1][n-1] = 1
        
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == n - 1 and j == n - 1:
                    continue
             
                if board[i][j] == 'X':
                    continue
                    
                max_s = -1
                path_count = 0
                
                directions = [(i + 1, j), (i, j + 1), (i + 1, j + 1)]
                
                for r, c in directions:
                    if r < n and c < n and dp_score[r][c] != -1:
                        if dp_score[r][c] > max_s:
                            max_s = dp_score[r][c]
                            path_count = dp_paths[r][c]
                        elif dp_score[r][c] == max_s:
                            path_count = (path_count + dp_paths[r][c]) % MOD
                
                if max_s != -1:
                  
                    current_val = int(board[i][j]) if board[i][j] != 'E' else 0
                    dp_score[i][j] = max_s + current_val
                    dp_paths[i][j] = path_count
        
        if dp_score[0][0] == -1:
            return [0, 0]
            
        return [dp_score[0][0], dp_paths[0][0]]