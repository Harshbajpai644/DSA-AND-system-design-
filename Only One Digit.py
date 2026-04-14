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
        x_str = sys.stdin.readline().strip()
        if not x_str:
            continue
        
        digits_in_x = set(x_str)
        
        y = 0
        while True:
            y_str = str(y)
            found = False
            for digit in y_str:
                if digit in digits_in_x:
                    found = True
                    break
            
            if found:
                print(y)
                break
            y += 1

if __name__ == "__main__":
    solve()