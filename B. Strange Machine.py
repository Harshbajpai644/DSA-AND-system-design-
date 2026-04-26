import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    s = input().strip()
    queries = list(map(int, input().split()))
    
    res = []
    
    has_B = 'B' in s   # 🔥 important optimization
    
    for a in queries:
        if not has_B:
            res.append(str(a))
            continue
        
        pos = 0
        steps = 0
        
        while a > 0:
            if s[pos] == 'A':
                a -= 1
            else:
                a //= 2
            
            steps += 1
            pos = (pos + 1) % n
        
        res.append(str(steps))
    
    print("\n".join(res))
