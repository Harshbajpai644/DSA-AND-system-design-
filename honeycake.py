import math

def solve():
    try:
        line1 = input().split()
        if not line1: return
        w, h, d = map(int, line1)
        line2 = input().split()
        if not line2: return
        n = int(line2[0])
    except EOFError:
        return

    divs = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.append(i)
            if i*i != n:
                divs.append(n // i)
    
    divs.sort()

    for x in divs:
        if w % x == 0:
            remaining_n = n // x
            for y in divs:
                if remaining_n % y == 0:
                    if h % y == 0:
                        z = remaining_n // y
                        if d % z == 0:
                            print(f"{x-1} {y-1} {z-1}")
                            return

    print("-1")

solve()