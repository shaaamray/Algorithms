graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)

        adjacent_nodes = graph[node]
        for i in adjacent_nodes:
            if i not in visited:
                stack.append(i)


start_node = 'A'
dfs(graph, start_node)