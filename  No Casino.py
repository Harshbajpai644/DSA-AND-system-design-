import sys

def solve():
    input = sys.stdin.read().split()
    idx = 0
    t = int(input[idx])
    idx += 1
    
    results = []
    for _ in range(t):
        n = int(input[idx])
        k = int(input[idx + 1])
        a = input[idx + 2 : idx + 2 + n]
        idx += 2 + n
        
        hikes = 0
        i = 0
        
        while i <= n - k:
            possible = True
            for j in range(i, i + k):
                if a[j] == '1':
                    possible = False
                    bad_day = j
                    break
            
            if possible:
                hikes += 1
                i += k + 1
            else:
                i = bad_day + 1
                
        results.append(str(hikes))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()