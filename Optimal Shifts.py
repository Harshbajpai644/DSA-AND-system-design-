import sys

def solve():
    input = sys.stdin.read().split()
    if not input:
        return
    
    t = int(input[0])
    idx = 1
    results = []
    
    for _ in range(t):
        n = int(input[idx])
        s = input[idx + 1]
        idx += 2
        
        if '0' not in s:
            results.append(0)
            continue
            
        zeros = s.split('1')
        
        if s[0] == '0' and s[-1] == '0':
            combined_gap = len(zeros[0]) + len(zeros[-1])
            max_gap = combined_gap
            for i in range(1, len(zeros) - 1):
                max_gap = max(max_gap, len(zeros[i]))
        else:
            max_gap = 0
            for z in zeros:
                max_gap = max(max_gap, len(z))
                
        results.append(max_gap)
        
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()
