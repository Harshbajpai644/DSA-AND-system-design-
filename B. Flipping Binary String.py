import sys

def solve():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    
    indices_1 = [i + 1 for i, char in enumerate(s) if char == '1']
    indices_0 = [i + 1 for i, char in enumerate(s) if char == '0']
    
    count_1 = len(indices_1)
    count_0 = len(indices_0)
    
    # Case 1: Number of operations is even
    # We flip all '1's. For this to work, count_1 must be even.
    if count_1 % 2 == 0:
        print(count_1)
        print(*(indices_1))
        return

    # Case 2: Number of operations is odd
    # We flip all '0's. For this to work, count_0 must be odd.
    if count_0 % 2 != 0:
        print(count_0)
        print(*(indices_0))
        return
        
    print("-1")

line = sys.stdin.readline()
if line:
    t = int(line.strip())
    for _ in range(t):
        solve()
