import sys

def solve():
    # Use fast I/O for large inputs
    input = sys.stdin.read().split()
    ptr = 0
    
    t = int(input[ptr])
    ptr += 1
    results = []
    
    for _ in range(t):
        n = int(input[ptr])
        x = int(input[ptr+1])
        y = int(input[ptr+2])
        ptr += 3
        
        a = []
        total_transfers = 0
        for i in range(n):
            val = int(input[ptr + i])
            a.append(val)
            total_transfers += val // x
        ptr += n
        
        max_money = 0
        for i in range(n):
            # If bank i is the destination:
            # It keeps its full initial amount a[i]
            # It receives (total_transfers - (a[i] // x)) packets of y
            current_total = a[i] + (total_transfers - (a[i] // x)) * y
            if current_total > max_money:
                max_money = current_total
                
        results.append(str(max_money))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
