import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    k = int(input_data[2])
    
    min_viability = [10**6 + 7] * (m + 1)
    
    idx = 3
    for _ in range(n):
        r = int(input_data[idx])
        c = int(input_data[idx + 1])
        idx += 2
        
        if c < min_viability[r]:
            min_viability[r] = c
            
    total_capacity = 0
    for i in range(1, m + 1):
        if min_viability[i] != 10**6 + 7:
            total_capacity += min_viability[i]
            
    print(min(total_capacity, k))

if __name__ == "__main__":
    solve()