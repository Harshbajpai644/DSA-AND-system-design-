def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    idx = 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        a.sort(reverse=True)
        ans = []
        used = [False] * n
        possible_sums = [False] * 20001
        possible_sums[0] = True
        
        possible = True
        for _ in range(n):
            found = False
            for i in range(n):
                if not used[i] and not possible_sums[a[i]]:
                    # Pick this number
                    val = a[i]
                    ans.append(val)
                    used[i] = True
                    found = True
                    
                    # Update reachable sums (Subset Sum DP)
                    for s in range(20000, val - 1, -1):
                        if possible_sums[s - val]:
                            possible_sums[s] = True
                    break
            
            if not found:
                possible = False
                break
        
        if possible:
            results.append(" ".join(map(str, ans)))
        else:
            results.append("-1")
            
    print("\n".join(results))

if __name__ == "__main__":
    solve()
