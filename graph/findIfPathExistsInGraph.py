class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(graph, current, destination, visited):
            if current == destination:
                return True

            visited.add(current)
            for neighbour in graph[current]:
                if neighbour not in visited:
                    if dfs(graph, neighbour, destination, visited):
                        return True
            return False

        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        return dfs(graph, source, destination, visited)