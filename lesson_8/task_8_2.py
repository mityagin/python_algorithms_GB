# 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
# которые необходимо обойти.

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]


def dijkstra(graph, start):
    original_start = start
    length = len(graph)
    is_visited = [False] * length
    cost = []
    for i in range(length):
        cost.append([float('inf'), []])
    parent = [-1] * length

    cost[start][0] = 0
    min_cost = 0

    while min_cost < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i][0] > vertex + cost[start][0]:
                    cost[i][0] = vertex + cost[start][0]
                    parent[i] = start
                    cost[i][1].clear()
                    cost[i][1].append(i)
                    path_parent = start
                    while path_parent != original_start:
                        cost[i][1].append(path_parent)
                        path_parent = parent[path_parent]
                    cost[i][1].append(original_start)
                    cost[i][1].reverse()

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i][0] and not is_visited[i]:
                min_cost = cost[i][0]
                start = i

    return cost


print(dijkstra(g, 2))
