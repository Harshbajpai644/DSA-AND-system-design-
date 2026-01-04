import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

  
    A2 = A * 2
    B2 = B * 2
    C2 = C * 2

    ans = 0

  
    good_bc = [[0]*n for _ in range(n)]

    for j in range(n):
        for k in range(n):
            length = 0
            while length < n and B2[j+length] < C2[k+length]:
                length += 1
            good_bc[j][k] = length

    
    for i in range(n):
        for j in range(n):
           
            ok = True
            for t2 in range(n):
                if not (A2[i+t2] < B2[j+t2]):
                    ok = False
                    break
            if not ok:
                continue

           
            for k in range(n):
                if good_bc[j][k] >= n:
                    ans += 1

    print(ans)
