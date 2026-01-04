import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 998244353

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        parents = list(map(int, input().split()))

       
        g = [[] for _ in range(n)]
        for i, p in enumerate(parents):
            g[p - 1].append(i + 1)

       
        depth = [0] * n
        stack = [0]
        while stack:
            u = stack.pop()
            for v in g[u]:
                depth[v] = depth[u] + 1
                stack.append(v)

        maxd = max(depth)
        cnt = [0] * (maxd + 1)
        for d in depth:
            cnt[d] += 1

        dp = [0] * (maxd + 1)
        pref = [0] * (maxd + 2)

        
        dp[0] = 1
        pref[1] = 1

        for d in range(1, maxd + 1):
            L = max(0, d - k)
            R = d - 1
            total = pref[R + 1] - pref[L]
            total %= MOD
            dp[d] = cnt[d] * total % MOD
            pref[d + 1] = (pref[d] + dp[d]) % MOD

        print(sum(dp) % MOD)


if __name__ == "__main__":
    solve()
