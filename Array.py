import sys

def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    
    results = []
    
    for i in range(n):
        if i == n - 1:
            results.append(0)
            continue
            
        suffix = a[i+1:]
        suffix.sort()
        
        m = len(suffix)
        max_j = 0
        
        # Pointer for suffix elements
        # For a fixed k, we want to count j such that |ai - k| > |aj - k|
        # This is equivalent to k being in the Voronoi region of aj vs ai.
        
        # Testing k = a[j] for each j > i is a good heuristic, 
        # but we need to be more precise.
        # The transition points for k are midpoints (ai + aj) / 2.
        
        midpoints = []
        for val in suffix:
            midpoints.append((a[i] + val) / 2)
        midpoints.sort()
        
        # The number of valid j's only changes when k passes a midpoint.
        # We test a value of k between every two consecutive midpoints.
        
        # Check very small k
        count = 0
        for val in suffix:
            if val < a[i]: count += 1
        max_j = max(max_j, count)
        
        # Check very large k
        count = 0
        for val in suffix:
            if val > a[i]: count += 1
        max_j = max(max_j, count)
        
        # Check k near each suffix value
        # Actually, for a fixed k, the number of valid j is:
        # (count of aj > ai where (ai+aj)/2 < k) + (count of aj < ai where (ai+aj)/2 > k)
        
        low_mids = sorted([(a[i] + x) / 2 for x in suffix if x < a[i]])
        high_mids = sorted([(a[i] + x) / 2 for x in suffix if x > a[i]])
        
        # Use two pointers or binary search to find best k
        # We want to find k that maximizes:
        # (number of high_mids < k) + (number of low_mids > k)
        
        # This is a classic problem: max(prefix_sum_A + suffix_sum_B)
        # Combine all midpoints, sort them, and sweep.
        
        current_val = len(low_mids) # Start with k = -infinity
        max_j = max(max_j, current_val)
        
        all_mids = []
        for m in low_mids: all_mids.append((m, -1)) # -1 means we lose a 'low' match
        for m in high_mids: all_mids.append((m, 1))  # +1 means we gain a 'high' match
        
        all_mids.sort()
        
        for _, change in all_mids:
            current_val += change
            max_j = max(max_j, current_val)
            
        results.append(max_j)
        
    print(*(results))

line = sys.stdin.readline()
if line:
    t = int(line)
    for _ in range(t):
        solve()
