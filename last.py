import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 998244353

t = int(input())

for _ in range(t):
    n, d = map(int, input().split())
    parent = list(map(int, input().split()))

    tree = [[] for _ in range(n)]
    for i in range(1, n):
        tree[parent[i] - 1].append(i)

    
    def dfs(u):
        dp = [0] * (d + 2)

       
        dp[0] = 1

        for v in tree[u]:
            child_dp = dfs(v)
            new_dp = [0] * (d + 2)

            for i in range(d + 1):
                if dp[i] == 0:
                    continue
                for j in range(d + 1):
                    if child_dp[j] == 0:
                        continue
                    if i + j + 1 <= d:
                        new_dp[max(i + 1, j + 1)] = (new_dp[max(i + 1, j + 1)] + dp[i] * child_dp[j]) % MOD

            dp = new_dp

        return dp

    res = dfs(0)
    print(sum(res) % MOD)
