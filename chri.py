import sys
from collections import Counter
input = sys.stdin.readline

MOD = 998244353

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    freq = Counter(a)
    remaining = list(freq.values())

    remaining.sort()

    ans = 1
    alive = len(remaining)
    idx = 0

    for step in range(n):
        while idx < len(remaining) and remaining[idx] == step:
            alive -= 1
            idx += 1

        ans = ans * alive % MOD

    print(ans)
