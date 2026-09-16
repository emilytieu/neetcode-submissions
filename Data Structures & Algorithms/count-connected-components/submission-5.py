class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges: 
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()
        count = 0

        def dfs(node):
            nonlocal count
            if node not in visited:
                count += 1
                visited.add(node)
            
            for neighbour in adj[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour)
            
        for node in range(n):
            dfs(node)
        return count