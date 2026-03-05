import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    
    results = []
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        a = [int(x) for x in input_data[idx : idx + n]]
        idx += n
        
        is_sorted = True
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                is_sorted = False
                break
        
        if is_sorted:
            results.append(str(n))
        else:
            results.append("1")
            
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()