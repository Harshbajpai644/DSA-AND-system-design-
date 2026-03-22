import sys

def solve():
    line = sys.stdin.readline().split()
    if not line:
        return
    n, k = map(int, line)
    
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
                
    primes = [i for i, val in enumerate(is_prime) if val]
    
    count = 0
    for i in range(len(primes) - 1):
        noldbach_candidate = primes[i] + primes[i+1] + 1
        if noldbach_candidate <= n and is_prime[noldbach_candidate]:
            count += 1
            
    if count >= k:
        print("YES")
    else:
        print("NO")

solve()