def count_blocks(s):
    if not s:
        return 0
    blocks = 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            blocks += 1
    return blocks

def solve():
    try:
        line1 = input().split()
        if not line1: return
        n = int(line1[0])
        s = input().strip()
    except EOFError:
        return

    max_blocks = 0
    # Check all n possible rotations
    for i in range(n):
        rotated = s[i:] + s[:i]
        max_blocks = max(max_blocks, count_blocks(rotated))
    
    print(max_blocks)

t_str = input().split()
if t_str:
    t = int(t_str[0])
    for _ in range(t):
        solve()