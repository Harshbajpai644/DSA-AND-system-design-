import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    has_odd = False
    has_even = False

    for x in arr:
        if x % 2 == 0:
            has_even = True
        else:
            has_odd = True

    if has_even and has_odd:
        arr.sort()

    print(*arr)