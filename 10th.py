import sys
 
def solve():
   
    try:
        line1 = sys.stdin.readline()
        if not line1: return
        n = int(line1.strip())
        a = list(map(int, sys.stdin.readline().split()))
    except ValueError:
        return
 
    
    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1
    
   
    kept = 0
    for x, count in counts.items():
        if x > 0 and count >= x:
            kept += x
            
   
    print(n - kept)
 

line = sys.stdin.readline()
if line:
    t = int(line.strip())
    for _ in range(t):
        solve()