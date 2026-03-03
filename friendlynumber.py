import sys

def get_digit_sum(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    results = []
    
    for i in range(1, t + 1):
        x = int(input_data[i])
        count = 0
        
        
        for y in range(x, x + 100):
            if y - get_digit_sum(y) == x:
                count += 1
        results.append(str(count))
            
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()