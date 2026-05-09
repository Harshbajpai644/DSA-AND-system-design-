class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        num_layers = min(m, n) // 2
        
        for layer in range(num_layers):
            elements = []
            
            # Top row
            for j in range(layer, n - 1 - layer):
                elements.append(grid[layer][j])
            # Right column
            for i in range(layer, m - 1 - layer):
                elements.append(grid[i][n - 1 - layer])
            # Bottom row
            for j in range(n - 1 - layer, layer, -1):
                elements.append(grid[m - 1 - layer][j])
            # Left column
            for i in range(m - 1 - layer, layer, -1):
                elements.append(grid[i][layer])
            
            total_elements = len(elements)
            shift = k % total_elements
            rotated = elements[shift:] + elements[:shift]
            
            idx = 0
            for j in range(layer, n - 1 - layer):
                grid[layer][j] = rotated[idx]
                idx += 1
            for i in range(layer, m - 1 - layer):
                grid[i][n - 1 - layer] = rotated[idx]
                idx += 1
            for j in range(n - 1 - layer, layer, -1):
                grid[m - 1 - layer][j] = rotated[idx]
                idx += 1
            for i in range(m - 1 - layer, layer, -1):
                grid[i][layer] = rotated[idx]
                idx += 1
                
        return grid
