import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    
    results = []
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        a = input[ptr:ptr+n]
        ptr += n
        
        count = 0
        current_max = -1
        
        for x in a:
            val = int(x)
            if val >= current_max:
                current_max = val
                count += 1
        
        results.append(str(count))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
