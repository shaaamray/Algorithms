from collections import deque

graph = {
    '2': ['5', '4'],
    '5': ['2', '3'],
    '4': ['1'],
    '3': ['6', '8'],
    '1': ['8'],
    '6': [],
    '8': ['9'],
    '9': []
}
def bfs(graph, start):
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
        neighbours = graph[node]
        for i in neighbours:
            if i not in visited:
                queue.append(i)
    print(visited)

bfs(graph, '2')