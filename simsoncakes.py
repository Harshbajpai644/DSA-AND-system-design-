import sys

def solve():
    try:
        line = sys.stdin.readline()
        if not line:
            return
        t = int(line.strip())
    except ValueError:
        return

    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        
        k = 1
        d = 2
        temp_n = n
        
        while d * d <= temp_n:
            if temp_n % d == 0:
                k *= d
                while temp_n % d == 0:
                    temp_n //= d
            d += 1
            
        if temp_n > 1:
            k *= temp_n
            
        print(k)

if __name__ == "__main__":
    solve()