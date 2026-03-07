import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()

    last = -10**9
    protect = 0

    for i in range(n):
        if s[i] == '1':
            if i - last >= k:
                protect += 1
                last = i
            else:
                last = i

    print(protect)