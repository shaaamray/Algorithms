graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start)

    adjacent_nodes = graph[start]
    for i in adjacent_nodes:
        if i not in visited:
            dfs(graph, i, visited)


start = 'A'
dfs(graph, start)