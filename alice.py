import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    t = int(input_data[idx])
    idx += 1
    
    results = []
    
    for _ in range(t):
        n = int(input_data[idx])
        a = int(input_data[idx+1])
        idx += 2
        
        v = []
        for _ in range(n):
            v.append(int(input_data[idx]))
            idx += 1
            
        left_count = 0
        right_count = 0
        
        for val in v:
            if val < a:
                left_count += 1
            elif val > a:
                right_count += 1
        
        if left_count >= right_count:
            results.append(str(a - 1))
        else:
            results.append(str(a + 1))
            
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()