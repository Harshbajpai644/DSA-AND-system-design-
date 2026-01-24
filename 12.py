import sys
 
def solve():
    line = sys.stdin.readline()
    if not line:
        return
    n, m, s = map(int, line.split())
 
    rows = (n - 1) // s + 1
    cols = (m - 1) // s + 1
 
    x_rem = n % s
    if x_rem == 0:
        x_rem = s
        
    y_rem = m % s
    if y_rem == 0:
        y_rem = s
 
    print(rows * cols * x_rem * y_rem)
 
if __name__ == "__main__":
    solve()