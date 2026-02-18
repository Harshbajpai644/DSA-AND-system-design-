import sys

def solve():
    line1 = sys.stdin.readline()
    if not line1: 
        return
    n = int(line1.strip())
    
    line2 = sys.stdin.readline()
    if not line2: 
        return
    y, r = map(int, line2.split())
    
    by_red = min(r, n)
    remaining = n - by_red
    
    by_yellow = min(y // 2, remaining)
    
    print(by_red + by_yellow)

line = sys.stdin.readline()
if line:
    t_str = line.strip()
    if t_str:
        t = int(t_str)
        for _ in range(t):
            solve()