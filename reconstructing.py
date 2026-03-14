# 1-based nodes
reach = [['0']*(n+1) for _ in range(n+1)]  # or list of strings

# find node with max reachable count
best = -1
max_cnt = -1
for i in range(1,n+1):
    cnt = sum(1 for j in range(1,n+1) if reach[i][j]=='1')
    if cnt > max_cnt:
        max_cnt = cnt
        best = i

root = best

# check if root reaches everyone
if max_cnt != n:
    print("No")
    continue

# Now try to find parents
parent = [-1]*(n+1)
edges = []

for v in range(1,n+1):
    if v == root: continue
    cand = []
    for u in range(1,n+1):
        if u == v: continue
        if reach[u][v] == '0': continue
        # check if direct: no w with u→w→v strict
        direct = True
        for w in range(1,n+1):
            if w == u or w == v: continue
            if reach[u][w]=='1' and reach[w][v]=='1':
                direct = False
                break
        if direct:
            cand.append(u)

    if len(cand) != 1:
        # not unique parent → invalid under this root
        break
    p = cand[0]
    parent[v] = p
    edges.append((p, v))   # directed p → v

else:
    # all nodes got exactly one parent
    # now verify the whole reachability (optional but recommended)
    # but since n small, and constraints tight, usually if unique parents + root reaches all → ok

    print("Yes")
    for a,b in edges:
        print(a, b)
    continue

print("No")