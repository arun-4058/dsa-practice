class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(parent, node):
            if parent[node] != node:
                parent[node] = find(parent, parent[node])
            return parent[node]

        n = len(edges)
        parent = list(range(n + 1))
        redundant_edge = []

        for u, v in edges:
            root_u = find(parent, u)
            root_v = find(parent, v)
            if root_u == root_v:
                redundant_edge = [u, v]
            else:
                parent[root_u] = root_v
        return redundant_edge