import math

def solve():
    n, m, a = map(int, input().split())
    
    stones_n = (n + a - 1) // a
    stones_m = (m + a - 1) // a
    
    print(stones_n * stones_m)

if __name__ == "__main__":
    solve()