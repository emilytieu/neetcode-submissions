class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        area = 0

        def dfs(row, col):
            if (row < 0 or col < 0 or
                row == len(grid) or col == len(grid[0]) or
                grid[row][col] == 0 or
                (row, col) in visited
            ):
                return 0
            
            visited.add((row, col))
            return (1 + dfs(row + 1, col) +
                        dfs(row - 1, col) + 
                        dfs(row, col + 1) + 
                        dfs(row, col - 1))
            
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                area = max(area, dfs(r, c))
        
        return area