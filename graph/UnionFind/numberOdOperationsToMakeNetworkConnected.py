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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        uf = UnionFind(n)
        for u, v in connections:
            uf.union(u, v)

        return uf.count - 1
        # if len(connections) < n - 1:
        #     return -1
        # graph = {i: [] for i in range(n)}

        # for a,b in connections:
        #     graph[a].append(b)
        #     graph[b].append(a)
        # visited = set()

        # def dfs(i):
        #     visited.add(i)
        #     for neighbor in graph[i]:
        #         if neighbor not in visited:
        #             dfs(neighbor)

        # cc = 0
        # for i in range(n):
        #     if i not in visited:
        #         dfs(i)
        #         cc += 1
        # print(cc)
        # return cc-1
