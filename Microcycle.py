import sys
from collections import deque

# Python ki default recursion depth kam hoti hai, ise badhana zaroori hai
sys.setrecursionlimit(200005)

def solve():
    # Fast I/O ke liye reading optimization
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    t = int(input_data[ptr])
    ptr += 1
    
    for _ in range(t):
        n = int(input_data[ptr])
        m = int(input_data[ptr + 1])
        ptr += 2
        
        edges = []
        for i in range(m):
            u = int(input_data[ptr])
            v = int(input_data[ptr + 1])
            w = int(input_data[ptr + 2])
            edges.append({'u': u, 'v': v, 'w': w})
            ptr += 3
            
        # Edges ko weight ke hisaab se descending sort karein
        edges.sort(key=lambda x: x['w'], reverse=True)
        
        parent = list(range(n + 1))
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
            
        min_edge = {'u': 0, 'v': 0, 'w': float('inf')}
        final_adj = [[] for _ in range(n + 1)]
        
        for edge in edges:
            root_u = find(edge['u'])
            root_v = find(edge['v'])
            
            if root_u != root_v:
                parent[root_u] = root_v
                final_adj[edge['u']].append(edge['v'])
                final_adj[edge['v']].append(edge['u'])
            else:
                # Jab sorting descending ho, toh aakhri cycle-closing edge hi min hogi
                min_edge = edge
                
        # BFS to find path between min_edge['u'] and min_edge['v']
        queue = deque([min_edge['u']])
        visited = [False] * (n + 1)
        prev = [-1] * (n + 1)
        
        visited[min_edge['u']] = True
        
        while queue:
            curr = queue.popleft()
            if curr == min_edge['v']:
                break
            for neighbor in final_adj[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    prev[neighbor] = curr
                    queue.append(neighbor)
                    
        path = []
        curr = min_edge['v']
        while curr != -1:
            path.append(curr)
            curr = prev[curr]
            
        print(f"{min_edge['w']} {len(path)}")
        print(*(path))

if __name__ == "__main__":
    solve()
    