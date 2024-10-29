def floyd_warshall(graph):
    distance = list(map(lambda i: list(map(lambda j: j, i)), graph))

    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    return distance

graph = [
    [0, 3, float('inf'), 7],
    [8, 0, 2, float('inf')],
    [5, float('inf'), 0, 1],
    [2, float('inf'), float('inf'), 0]
]

print(floyd_warshall(graph))
