import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    results = []
    
    for i in range(1, t + 1):
        x = int(input_data[i])
        # Since we need to maximize min(x, y), 
        # any y >= x works. Using x + 1 to match example.
        # We must ensure y stays within the range [-67, 67].
        if x < 67:
            results.append(str(x + 1))
        else:
            results.append(str(x))
            
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
