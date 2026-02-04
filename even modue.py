import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    t = int(input_data[ptr])
    ptr += 1
    
    results = []
    for _ in range(t):
        n = int(input_data[ptr])
        ptr += 1
        a = [int(x) for x in input_data[ptr : ptr + n]]
        ptr += n
        
        found = False
        
        evens = [x for x in a if x % 2 == 0]
        if len(evens) >= 2:
            results.append(f"{evens[0]} {evens[1]}")
            continue

        if a[0] == 1:
            results.append(f"{a[0]} {a[1]}")
            continue

        for i in range(min(n, 100)):
            for j in range(i + 1, min(n, 100)):
                if a[j] % a[i] % 2 == 0:
                    results.append(f"{a[i]} {a[j]}")
                    found = True
                    break
            if found: break
            
        if not found:
            results.append("-1")
            
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()