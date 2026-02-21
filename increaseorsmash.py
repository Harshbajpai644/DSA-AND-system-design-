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
        arr = list(map(int, input_data[idx : idx + n]))
        idx += n
        
        unique_elements = set(arr)
        k = len(unique_elements)
        
        results.append(str(2 * k - 1))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()