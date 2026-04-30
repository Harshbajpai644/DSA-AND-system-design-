def solve():
    n = int(input())
    s = list(input())
    
    operations = 0
    # Work from right to left to see how many changes propagate
    # Or simply: a character i needs to change if it's not the same as i+1
    for i in range(n - 2, -1, -1):
        if s[i] != s[i+1]:
            operations += 1
            s[i] = s[i+1]
            
    print(operations)

t = int(input())
for _ in range(t):
    solve()
