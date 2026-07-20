class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        visited = set()
        maxArea = 0

        def bfs(r, c):
            nonlocal count, maxArea
            q = deque()
            visited.add((r, c))
            q.append((r, c))
            count += 1

            while q:
                row, col = q.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if (r in range(len(grid)) and
                    c in range(len(grid[0])) and
                    grid[r][c] == 1 and 
                    (r, c) not in visited):
                        q.append((r, c))
                        count += 1
                        visited.add((r, c))
            
            maxArea = max(maxArea, count)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in visited:
                    count = 0
                    bfs(r, c)
        
        return maxArea