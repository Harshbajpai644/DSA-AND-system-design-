import sys

def solve():
    line = sys.stdin.readline()
    if not line:
        return
    n = int(line)
    p = list(map(int, sys.stdin.readline().split()))
    
    if n == 0:
        return

    pos_n = -1
    for i in range(n):
        if p[i] == n:
            pos_n = i
            break
            
    p[0], p[pos_n] = p[pos_n], p[0]
    
    print(*(p))

def main():
    line = sys.stdin.readline()
    if not line:
        return
    t_str = line.strip()
    if not t_str:
        return
    t = int(t_str)
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()