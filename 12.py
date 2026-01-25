import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    t = int(input_data[ptr])
    ptr += 1
    
    for _ in range(t):
        n = int(input_data[ptr])
        ptr += 1
        
        a = [0] * (n + 1)
        for i in range(1, n + 1):
            a[i] = int(input_data[ptr])
            ptr += 1
            
        adj = [set() for _ in range(n + 1)]
        neighbor_sum = [0] * (n + 1)
        
        for _ in range(n - 1):
            u = int(input_data[ptr])
            v = int(input_data[ptr + 1])
            adj[u].add(v)
            adj[v].add(u)
            neighbor_sum[u] += a[v]
            neighbor_sum[v] += a[u]
            ptr += 2
            
        removable = []
        for i in range(1, n + 1):
            if (a[i] % 2) != (neighbor_sum[i] % 2):
                removable.append(i)
        
        removed = []
        is_removed = [False] * (n + 1)
        
        while removable:
            u = removable.pop()
            if is_removed[u]:
                continue
                
            is_removed[u] = True
            removed.append(u)
            
            for v in adj[u]:
                if not is_removed[v]:
                    neighbor_sum[v] -= a[u]
                    adj[v].remove(u)
                    if (a[v] % 2) != (neighbor_sum[v] % 2):
                        removable.append(v)
        
        if len(removed) == n:
            print("YES")
            print(*(removed))
        else:
            print("NO")

if __name__ == "__main__":
    solve()