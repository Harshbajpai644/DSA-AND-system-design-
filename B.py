import sys

def solve():
    line1 = sys.stdin.readline()
    if not line1: return
    n = int(line1.strip())
    
    a = list(map(int, sys.stdin.readline().split()))
    
    total_dist = 0
    for i in range(n - 1):
        total_dist += abs(a[i] - a[i+1])
    
    max_savings = abs(a[0] - a[1])
    max_savings = max(max_savings, abs(a[n-2] - a[n-1]))
    
    for i in range(1, n - 1):
        current_path = abs(a[i-1] - a[i]) + abs(a[i] - a[i+1])
        skipped_path = abs(a[i-1] - a[i+1])
        savings = current_path - skipped_path
        max_savings = max(max_savings, savings)
    
    print(total_dist - max_savings)

def main():
    line = sys.stdin.readline()
    if line:
        t_str = line.strip()
        if t_str:
            t = int(t_str)
            for _ in range(t):
                solve()

if __name__ == "__main__":
    main()