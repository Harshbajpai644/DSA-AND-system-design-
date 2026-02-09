import sys

def solve():
    # Read the initial number of candies n
    line = sys.stdin.readline()
    if not line:
        return
    n = int(line.strip())
    
    # Calculate how many more are needed to make n divisible by 3
    remainder = n % 3
    if remainder == 0:
        print(0)
    else:
        print(3 - remainder)

def main():
    # Read number of test cases t
    line = sys.stdin.readline()
    if not line:
        return
    t = int(line.strip())
    
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()