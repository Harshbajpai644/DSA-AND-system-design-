class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0 and i > 0:
                    matrix[i][j] += matrix[i-1][j]
            
            row = sorted(matrix[i], reverse=True)
            
            for j in range(n):
                ans = max(ans, row[j] * (j + 1))
                
        return ans