import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    containers = []
    idx = 2
    for _ in range(m):
        a_i = int(input_data[idx])
        b_i = int(input_data[idx+1])
        containers.append((a_i, b_i))
        idx += 2
    
    containers.sort(key=lambda x: x[1], reverse=True)
    
    total_matches = 0
    remaining_capacity = n
    
    for boxes, matches_per_box in containers:
        if remaining_capacity <= 0:
            break
        
        take = min(boxes, remaining_capacity)
        total_matches += take * matches_per_box
        remaining_capacity -= take
        
    print(total_matches)

if __name__ == "__main__":
    solve()
