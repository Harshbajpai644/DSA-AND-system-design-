import sys

def solve():
    input = sys.stdin.read().split()
    if not input: return
    
    MOD = 998244353
    t = int(input[0])
    idx = 1
    
    # Precompute factorials for derangement formula
    MAX = 10**6 + 5
    fact = [1] * MAX
    inv = [1] * MAX
    for i in range(1, MAX):
        fact[i] = (fact[i-1] * i) % MOD
        
    def nCr(n, r):
        if r < 0 or r > n: return 0
        num = fact[n]
        den = (pow(fact[r], MOD-2, MOD) * pow(fact[n-r], MOD-2, MOD)) % MOD
        return (num * den) % MOD

    for _ in range(t):
        n = int(input[idx])
        X = list(map(int, input[idx+1 : idx+1+n]))
        idx += 1 + n
        
        used_val = [False] * n
        fixed_count = 0
        possible = True
        
        for i, val in enumerate(X):
            if val != -1:
                if used_val[val] or val == i:
                    possible = False
                    break
                used_val[val] = True
                fixed_count += 1
        
        if not possible:
            print(0)
            continue
            
        # m: positions we need to fill
        # k: positions i where X[i] == -1 AND the value i is still available
        m = n - fixed_count
        k = 0
        for i in range(n):
            if X[i] == -1 and not used_val[i]:
                k += 1
        
        # Inclusion-Exclusion for partial derangements
        ans = 0
        for i in range(k + 1):
            term = (nCr(k, i) * fact[m - i]) % MOD
            if i % 2 == 1:
                ans = (ans - term + MOD) % MOD
            else:
                ans = (ans + term) % MOD
        print(ans)

solve()