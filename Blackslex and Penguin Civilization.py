import sys

def solve():
    input = sys.stdin.read().split()
    t = int(input[0])
    idx = 1
    results = []
    
    for _ in range(t):
        n = int(input[idx])
        idx += 1
        
        limit = 1 << n
        p = []
        used = [False] * limit
        
        # 1. Start with the max value to maximize initial popcount
        first = limit - 1
        p.append(first)
        used[first] = True
        
        # 2. To maximize the sum, we drop bits one by one.
        # To be lexicographically minimal, we use 2^k - 1 values.
        for k in range(n - 1, 0, -1):
            val = (1 << k) - 1
            p.append(val)
            used[val] = True
            
        # 3. Add 0 to finally drop the prefix AND to 0
        p.append(0)
        used[0] = True
        
        # 4. Fill remaining unused numbers in increasing order
        for i in range(limit):
            if not used[i]:
                p.append(i)
        
        results.append(" ".join(map(str, p)))
        
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
