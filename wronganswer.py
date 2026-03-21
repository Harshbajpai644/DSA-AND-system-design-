import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(10**6)

def solve():
    line1 = sys.stdin.readline().split()
    if not line1:
        return
    n, k = map(int, line1)
    
    a = [0] + list(map(int, sys.stdin.readline().split()))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)

    if k == 1:
        print(max(a))
        return

    f = [0] * (n + 1)
    son = [-1] * (n + 1)
    
    # Using iterative DFS to avoid recursion depth issues on some platforms
    stack = [(1, 0, False)]
    order = []
    
    while stack:
        u, p, visited = stack.pop()
        if visited:
            best_f = 0
            best_son = -1
            for v in adj[u]:
                if v == p:
                    continue
                if f[v] > best_f:
                    best_f = f[v]
                    best_son = v
            f[u] = best_f + a[u]
            son[u] = best_son
        else:
            stack.append((u, p, True))
            for v in adj[u]:
                if v != p:
                    stack.append((v, u, False))

    paths = []
    # Iterative DFS for path decomposition
    stack = [(1, 0, True)]
    while stack:
        u, p, is_top = stack.pop()
        if is_top:
            paths.append(f[u])
        
        # Process children: heavy child (son) stays in current path, others start new
        for v in adj[u]:
            if v == p:
                continue
            if v == son[u]:
                stack.append((v, u, False))
            else:
                stack.append((v, u, True))

    paths.sort(reverse=True)
    
    print(sum(paths[:min(len(paths), k)]))

def main():
    line = sys.stdin.readline()
    if line:
        t = int(line)
        for _ in range(t):
            solve()

if __name__ == "__main__":
    main()