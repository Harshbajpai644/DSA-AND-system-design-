import sys

def solve():
    line1 = sys.stdin.readline().split()
    if not line1: return
    n = int(line1[0])
    p = list(map(int, sys.stdin.readline().split()))
    a = list(map(int, sys.stdin.readline().split()))
    
    unique_in_a = []
    if n > 0:
        unique_in_a.append(a[0])
        for i in range(1, n):
            if a[i] != a[i-1]:
                unique_in_a.append(a[i])
    
    seen_in_a = set()
    for x in unique_in_a:
        if x in seen_in_a:
            print("NO")
            return
        seen_in_a.add(x)
        
    p_idx = 0
    for x in unique_in_a:
        while p_idx < n and p[p_idx] != x:
            p_idx += 1
        
        if p_idx == n:
            print("NO")
            return
        p_idx += 1
            
    print("YES")

line = sys.stdin.readline().strip()
if line:
    t = int(line)
    for _ in range(t):
        solve()