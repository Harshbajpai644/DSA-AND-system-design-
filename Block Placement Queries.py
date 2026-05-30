from bisect import bisect_left, insort

class SegmentTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (4 * size)

    def update(self, index, value, node, start, end):
        if start == end:
            self.tree[node] = value
            return
        mid = (start + end) // 2
        if index <= mid:
            self.update(index, value, 2 * node, start, mid)
        else:
            self.update(index, value, 2 * node + 1, mid + 1, end)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, l, r, node, start, end):
        if l > end or r < start:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        return max(
            self.query(l, r, 2 * node, start, mid),
            self.query(l, r, 2 * node + 1, mid + 1, end)
        )

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        max_coord = 0
        obstacles = [0]
        
        for q in queries:
            max_coord = max(max_coord, q[1])
            if q[0] == 1:
                obstacles.append(q[1])
        
        max_coord += 1
        obstacles.sort()
        
        seg_tree = SegmentTree(max_coord)
        for i in range(1, len(obstacles)):
            seg_tree.update(obstacles[i], obstacles[i] - obstacles[i-1], 1, 0, max_coord - 1)
            
        results = []
        
        for q in reversed(queries):
            if q[0] == 1:
                x = q[1]
                idx = bisect_left(obstacles, x)
                left_obs = obstacles[idx - 1]
                
                if idx + 1 < len(obstacles):
                    right_obs = obstacles[idx + 1]
                    seg_tree.update(right_obs, right_obs - left_obs, 1, 0, max_coord - 1)
                
                seg_tree.update(x, 0, 1, 0, max_coord - 1)
                obstacles.pop(idx)
                
            else:
                x, sz = q[1], q[2]
                idx = bisect_left(obstacles, x)
                left_obs = obstacles[idx - 1]
                
                max_gap = max(seg_tree.query(0, left_obs, 1, 0, max_coord - 1), x - left_obs)
                results.append(max_gap >= sz)
                
        return results[::-1]
