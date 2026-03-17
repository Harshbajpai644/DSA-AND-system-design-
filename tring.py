import sys

def solve():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    
    if n % 2 != 0:
        print("NO")
        return

    dp = [[False] * n for _ in range(n)]

    for length in range(2, n + 1, 2):
        for i in range(n - length + 1):
            j = i + length - 1
            
            if s[i] == s[i+1] and (length == 2 or dp[i+2][j]):
                dp[i][j] = True
                continue
            
            if s[j] == s[j-1] and (length == 2 or dp[i][j-2]):
                dp[i][j] = True
                continue

            for k in range(i + 1, j + 1, 2):
                if s[i] == s[k]:
                    left_inner = (k == i + 1 or dp[i+1][k-1])
                    right_outer = (k == j or dp[k+1][j])
                    if left_inner and right_outer:
                        dp[i][j] = True
                        break
    
    if dp[0][n-1]:
        print("YES")
    else:
        print("NO")

line = sys.stdin.readline()
if line:
    t = int(line)
    for _ in range(t):
        solve()