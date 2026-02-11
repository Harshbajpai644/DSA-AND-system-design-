import sys

# No comments added to code as per instructions

def solve():
    line = sys.stdin.readline()
    if not line: return
    try:
        n = int(line.strip())
    except: return

    def ask(k):
        if k > 2**30: return None
        print(f"? {k}")
        sys.stdout.flush()
        res = list(map(int, sys.stdin.readline().split()))
        if not res or res[0] == -1: exit()
        if res[0] == 0: return None
        return res[1:]

    path_counts = [0] * (n + 1)
    start_pos = [0] * (n + 2)
    
    curr = 1
    for i in range(1, n + 1):
        start_pos[i] = curr
        p = ask(curr)
        
        # We need to find the count of paths starting at i.
        # We can find where vertex i+1 starts.
        # Since we don't know the count yet, we find the start of i+1
        # by searching or walking. In this simple version, walking is okay 
        # because the query limit allows 32 * (n+m).
        
        low = curr + 1
        high = 2**30
        next_start = curr + 1
        while low <= high:
            mid = (low + high) // 2
            res = ask(mid)
            if res is None or res[0] > i:
                next_start = mid
                high = mid - 1
            else:
                low = mid + 1
        
        path_counts[i] = next_start - curr
        curr = next_start
    
    start_pos[n+1] = curr

    edges = []
    for u in range(1, n + 1):
        idx = start_pos[u] + 1
        while idx < start_pos[u+1]:
            p = ask(idx)
            if p is None or p[0] != u: break
            
            if len(p) > 1:
                v = p[1]
                edges.append((u, v))
                idx += path_counts[v]
            else:
                idx += 1

    print(f"! {len(edges)}")
    for u, v in edges:
        print(f"{u} {v}")
    sys.stdout.flush()

line = sys.stdin.readline()
if line:
    t_str = line.strip()
    if t_str:
        t = int(t_str)
        for _ in range(t):
            solve()