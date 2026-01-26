def solve():
    n = read_int()
    a = read_list() # 1-indexed for convenience
    adj = [[] for _ in range(n + 1)]
    s = [0] * (n + 1)
    
    total_sum = sum(a)
    if total_sum % 2 == 0:
        print("NO")
        return

    for _ in range(n - 1):
        u, v = read_edge()
        adj[u].append(v)
        adj[v].append(u)
        s[u] += a[v-1]
        s[v] += a[u-1]

    queue = deque([i for i in range(1, n+1) if (a[i-1] + s[i]) % 2 == 1])
    removed = [False] * (n + 1)
    result = []

    while queue:
        v = queue.popleft()
        if removed[v]: continue
        
        removed[v] = True
        result.append(v)
        
        for neighbor in adj[v]:
            if not removed[neighbor]:
                s[neighbor] -= a[v-1]
                if (a[neighbor-1] + s[neighbor]) % 2 == 1:
                    queue.append(neighbor)

    if len(result) == n:
        print("YES")
        print(*result)
    else:
        print("NO")