import sys
import math

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    streets = input_data[2:]
    
    freq = [[0] * 26 for _ in range(n)]
    total_freq = [0] * 26
    
    for i in range(n):
        s = streets[i]
        for char in s:
            idx = ord(char) - ord('A')
            freq[i][idx] += 1
            total_freq[idx] += 1
            
    results = []
    
    for l in range(n):
        max_k = m
        possible = True
        
        for c in range(26):
            needed_for_one = freq[l][c]
            if needed_for_one == 0:
                continue
            
            others_sum = total_freq[c] - needed_for_one
            
            if others_sum == 0:
                possible = False
                break
            
            diff = math.ceil(needed_for_one / others_sum)
            current_k = m - diff
            
            if current_k < 0:
                possible = False
                break
            
            if current_k < max_k:
                max_k = current_k
        
        if not possible:
            results.append("-1")
        else:
            results.append(str(max_k))
            
    sys.stdout.write(" ".join(results) + "\n")

if __name__ == "__main__":
    solve()