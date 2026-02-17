import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    pointer = 1
    results = []
    
    for _ in range(t):
        a = int(input_data[pointer])
        b = int(input_data[pointer + 1])
        c = int(input_data[pointer + 2])
        d = int(input_data[pointer + 3])
        pointer += 4
        
        if a == b == c == d:
            results.append("YES")
        else:
            results.append("NO")
            
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()