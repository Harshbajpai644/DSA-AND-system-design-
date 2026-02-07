import sys

def solve():
    try:
        line1 = sys.stdin.readline()
        if not line1:
            return
        q = int(line1.strip())
    except ValueError:
        return

    for _ in range(q):
        try:
            n = int(sys.stdin.readline().strip())
            s, t = sys.stdin.readline().split()
            
            if sorted(s) == sorted(t):
                print("YES")
            else:
                print("NO")
        except ValueError:
            break

if __name__ == "__main__":
    solve()