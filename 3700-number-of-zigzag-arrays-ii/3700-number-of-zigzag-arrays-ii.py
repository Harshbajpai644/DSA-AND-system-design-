class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        size = 2 * m
        
        def multiply(A, B):
            C = [[0] * size for _ in range(size)]
            for i in range(size):
                for k in range(size):
                    if A[i][k] == 0:
                        continue
                    for j in range(size):
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
            return C

        def power(A, p):
            res = [[0] * size for _ in range(size)]
            for i in range(size):
                res[i][i] = 1
            base = A
            while p > 0:
                if p % 2 == 1:
                    res = multiply(res, base)
                base = multiply(base, base)
                p //= 2
            return res

        T = [[0] * size for _ in range(size)]
        
        for x in range(m):
            for y in range(m):
                if y > x:
                    T[y][m + x] = 1
                if y < x:
                    T[m + y][x] = 1
                    
        T_pow = power(T, n - 1)
        
        ans = 0
        for i in range(size):
            row_sum = sum(T_pow[i]) % MOD
            ans = (ans + row_sum) % MOD
            
        return ans