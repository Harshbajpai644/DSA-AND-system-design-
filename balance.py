import sys
input = sys.stdin.readline

MOD = 10**9 + 7
MAXN = 200000

fact = [1] * (MAXN + 1)
invfact = [1] * (MAXN + 1)
inv = [1] * (MAXN + 1)

for i in range(1, MAXN + 1):
    fact[i] = fact[i - 1] * i % MOD
    inv[i] = pow(i, MOD - 2, MOD)
    invfact[i] = invfact[i - 1] * inv[i] % MOD

def C(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * invfact[r] % MOD * invfact[n - r] % MOD

from collections import deque

def solve():
    t = int(input())
    res = []

    for _ in range(t):
        q = int(input())
        left = deque()
        right = deque()
        n = 0
        ans = 0

        def rebuild():
            nonlocal ans
            ans = 0
            arr = list(left) + list(right)
            n2 = len(arr)
            for i, v in enumerate(arr, 1):
                ans = (ans + v * C(n2, i) * inv[i]) % MOD

        for __ in range(q):
            s = input().split()
            if s[0] == '2':
                x = int(s[1])
                right.append(x)
                n += 1
                if len(right) > len(left) + 1:
                    left.append(right.popleft())
                rebuild()
            elif s[0] == '1':
                if n == 0:
                    continue
                right.popleft()
                n -= 1
                if len(left) > len(right):
                    right.appendleft(left.pop())
                rebuild()
            else:
                res.append(str(ans))

    print("\n".join(res))

if __name__ == "__main__":
    solve()
