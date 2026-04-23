import sys

def solve():
    input = sys.stdin.read().split()
    if not input:
        return
    
    t = int(input[0])
    results = []
    idx = 1
    
    for _ in range(t):
        n = int(input[idx])
        idx += 1
        
        permutation = [0] * (3 * n)
        
        small_ptr = 1
        large_ptr = 3 * n
        
        for i in range(n):
            block_idx = i * 3
            
            permutation[block_idx] = small_ptr
            small_ptr += 1
            
            permutation[block_idx + 1] = large_ptr - 1
            permutation[block_idx + 2] = large_ptr
            large_ptr -= 2
            
        results.append(" ".join(map(str, permutation)))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
