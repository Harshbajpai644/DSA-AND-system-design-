import sys
 
def solve():
    try:
        line1 = sys.stdin.readline()
        if not line1: return
        n = int(line1.strip())
        
        a = list(map(int, sys.stdin.readline().split()))
        x = int(sys.stdin.readline().strip())
        
        if min(a) <= x <= max(a):
            print("YES")
        else:
            print("NO")
    except EOFError:
        pass
 
line = sys.stdin.readline()
if line:
    t = int(line.strip())
    for _ in range(t):
        solve()