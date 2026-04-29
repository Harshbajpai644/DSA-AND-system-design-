import sys

def solve():
    # Read number of test cases
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    pointer = 1
    
    results = []
    for _ in range(t):
        n = int(input_data[pointer])
        pointer += 1
        
        # We only need the maximum value in the array
        current_max = 0
        for i in range(n):
            val = int(input_data[pointer])
            if val > current_max:
                current_max = val
            pointer += 1
            
        results.append(str(current_max))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
