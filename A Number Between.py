import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    pointer = 1
    results = []
    
    for _ in range(t):
        x = int(input_data[pointer])
        y = int(input_data[pointer + 1])
        pointer += 2
        
        if y == 2 * x:
            results.append("NO")
        else:
            results.append("YES")
            
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
