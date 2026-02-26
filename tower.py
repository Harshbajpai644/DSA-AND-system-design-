import sys
import math

def solve():
    # Read n, m, d
    try:
        line = sys.stdin.readline()
        if not line: return
        n, m, d = map(int, line.split())
        
        # Calculate max boxes per tower
        k_max = (d // m) + 1
        
        # Calculate minimum towers needed (ceiling division)
        ans = (n + k_max - 1) // k_max
        print(ans)
    except ValueError:
        pass

# Read number of test cases
line = sys.stdin.readline()
if line:
    t = int(line)
    for _ in range(t):
        solve()