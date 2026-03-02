class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        trailing_zeros = []
        
        for row in grid:
            count = 0
            for i in range(n - 1, -1, -1):
                if row[i] == 0:
                    count += 1
                else:
                    break
            trailing_zeros.append(count)
        
        total_swaps = 0
        for i in range(n):
            target = n - 1 - i
            found_idx = -1
            
            for j in range(i, n):
                if trailing_zeros[j] >= target:
                    found_idx = j
                    break
            
            if found_idx == -1:
                return -1
            
            total_swaps += (found_idx - i)
            
            val = trailing_zeros.pop(found_idx)
            trailing_zeros.insert(i, val)
            
        return total_swaps