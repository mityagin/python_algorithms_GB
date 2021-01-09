# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
#
# Примечания:
#
# a. граф должен храниться в виде списка смежности;
#
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

def generate_graph(n):
    grph = {}
    d = 2
    k = 4
    for i in range(1, n):
        grph.update({i: [x for x in range(d, k) if x != i]})
        d += 2
        k += 2
    for i in range(int(n/2), n):
        grph.update({i: [i + 1]})
    for i in range(n, n + 1):
        grph.update({i: []})
    return grph


n = int(input(f"Сколько вершин?: "))
graph = generate_graph(n)


def dfs_search(g, node, path=None):
    if path is None:
        path = []
    path += [node]
    for n in g[node]:
        if n not in path:
            path = dfs_search(g, n, path)
    return path


print(dfs_search(graph, 3))