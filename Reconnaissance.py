import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    d = int(input_data[1])
    a = list(map(int, input_data[2:]))

    count = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                if abs(a[i] - a[j]) <= d:
                    count += 1
    
    print(count)

if __name__ == "__main__":
    solve()