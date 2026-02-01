import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t_str = input_data[0]
    t = int(t_str)
    idx = 1
    results = []
    
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        a = input_data[idx : idx + n]
        idx += n
        
        present = set()
        for x in a:
            present.add(int(x))
            
        mex = 0
        while mex in present:
            mex += 1
        
        results.append(str(mex))

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()