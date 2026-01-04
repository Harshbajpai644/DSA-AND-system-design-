import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    if "2026" in s:
        print(0)
    elif "2025" not in s:
        print(0)
    else:
        print(1)
