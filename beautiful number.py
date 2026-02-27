import sys

def solve():
    line = sys.stdin.readline().strip()
    if not line:
        return
    
    digits = [int(d) for d in line]
    current_sum = sum(digits)
    
    if current_sum <= 9:
        print(0)
        return
    
    potential_reductions = []
    for i in range(len(digits)):
        if i == 0:
            potential_reductions.append(digits[i] - 1)
        else:
            potential_reductions.append(digits[i] - 0)
            
    potential_reductions.sort(reverse=True)
    
    moves = 0
    for reduction in potential_reductions:
        current_sum -= reduction
        moves += 1
        if current_sum <= 9:
            print(moves)
            return

line = sys.stdin.readline().strip()
if line:
    t = int(line)
    for _ in range(t):
        solve()