import sys

def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    
    ops = 0
    neg_count = 0
    
    for x in a:
        if x == 0:
            
            ops += 1
        elif x == -1:
            neg_count += 1
            
    
    if neg_count % 2 != 0:
        ops += 2
        
    print(ops)

line = sys.stdin.readline()
if line:
    t = int(line)
    for _ in range(t):
        solve()