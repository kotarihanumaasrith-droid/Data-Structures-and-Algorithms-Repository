from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited=None):
        if visited is None:
            visited = set()

        visited.add(v)
        print(v, end=" ")

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = [start]

        while queue:
            node = queue.pop(0)

            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                queue.extend(self.graph[node])


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)

    print("DFS:")
    g.dfs(0)

    print("\nBFS:")
    g.bfs(0)
