class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        degree = {}

        for u, v in edges:
            degree[u] = degree.get(u, 0) + 1
            degree[v] = degree.get(v, 0) + 1

        center = max(degree, key=degree.get)
        return center