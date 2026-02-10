import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    results = []
    
    for i in range(1, t + 1):
        n = int(input_data[2*i - 1])
        w = int(input_data[2*i])
        
        must_keep = n // w
        results.append(str(n - must_keep))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()