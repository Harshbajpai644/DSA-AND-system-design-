import sys

def solve():
    try:
        line1 = sys.stdin.readline()
        if not line1:
            return
        n = int(line1.strip())
        s = sys.stdin.readline().strip()
    except ValueError:
        return

    # Find the range of the string that contains 1s
    first = s.find('1')
    last = s.rfind('1')

    # If no '1's exist, the result is 0 0
    if first == -1:
        print(0, 0)
        return

    min_ones = 0
    max_ones = 0
    
    i = first
    while i <= last:
        if s[i] == '1':
            start = i
            end = i
            
            # Identify a reachable component
            # A component continues if there's a '1' at most 2 positions away
            while True:
                found_next = False
                # Check indices i+1 and i+2
                for j in range(end + 1, min(end + 3, last + 1)):
                    if s[j] == '1':
                        end = j
                        found_next = True
                        break
                if not found_next:
                    break
            
            length = end - start + 1
            
            # Apply formulas based on component length L
            # Max: Fill everything between the first and last 1 of the component
            max_ones += length
            # Min: The boundary 1s are fixed; reduce internal bits to alternating 0s
            min_ones += (length // 2) + 1
            
            i = end + 1
        else:
            i += 1

    print(f"{min_ones} {max_ones}")

def main():
    line = sys.stdin.readline()
    if line:
        t = int(line.strip())
        for _ in range(t):
            solve()

if __name__ == "__main__":
    main()