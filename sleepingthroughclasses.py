def solve():
    n, k = map(int, input().split())
    s = input()
    
    sleep_count = 0
    awake_until = 0
    
    # 1-based indexing ke liye enumerate(s, 1)
    for i, char in enumerate(s, 1):
        if char == '1':
            # Rule: Must stay awake for next k classes
            awake_until = max(awake_until, i + k)
        else:
            # If not important and not forced to stay awake
            if i > awake_until:
                sleep_count += 1
                
    print(sleep_count)

# Multiple test cases handle karne ke liye
t = int(input())
for _ in range(t):
    solve()