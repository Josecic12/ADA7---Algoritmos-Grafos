def warshall(graph):
    n = len(graph)
    reach = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            reach[i][j] = graph[i][j] or (i == j)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])

    return reach

graph = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]

print(warshall(graph))
