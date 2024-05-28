class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            self.count -= 1


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        uf = UnionFind(n)
        row_map = {}
        col_map = {}

        for i, (x, y) in enumerate(stones):
            if x in row_map:
                uf.union(i, row_map[x])
            if y in col_map:
                uf.union(i, col_map[y])
            row_map[x] = i
            col_map[y] = i
        return n - uf.count
        # def dfs(node):
        #     visited.add(node)
        #     for neighbor in graph[node]:
        #         if neighbor not in visited:
        #             dfs(neighbor)
        # cc = 0
        # n = len(stones)
        # visited = set()
        # graph = {}
        # for i, (x1, y1) in enumerate(stones):
        #     for j, (x2, y2) in enumerate(stones):
        #         if x1 == x2 or y1 == y2:
        #             if i not in graph:
        #                 graph[i] = set()
        #             graph[i].add(j)
        # for i in range(n):
        #     if i not in visited:
        #         dfs(i)
        #         cc += 1
        # return len(stones) - cc