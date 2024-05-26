
graph = [
    [0, 7, 5, 0],
    [7, 0, 9, 7],
    [5, 9, 0, 15],
    [0, 7, 15, 0],
]

def find_min_distance(distances, visited):
    min_distance = float('inf')
    min_index = -1
    for i in range(len(distances)):
        if distances[i] < min_distance and not visited[i]:
            min_distance = distances[i]
            min_index = i
    return min_index

# Функция для реализации алгоритма Дейкстры
def dijkstra(graph, start):
    distances = [float('inf')] * len(graph)
    distances[start] = 0

    # Инициализируем массив для хранения информации о посещенных вершинах
    visited = [False] * len(graph)

    for _ in range(len(graph)):
        # Находим вершину с наименьшим расстоянием
        u = find_min_distance(distances, visited)
        visited[u] = True

        # Обновляем расстояния до соседних вершин
        for v in range(len(graph)):
            if graph[u][v] > 0 and not visited[v] and distances[v] > distances[u] + graph[u][v]:
                distances[v] = distances[u] + graph[u][v]

    return distances

start_vertex = 2
shortest_distances = dijkstra(graph, start_vertex)
print(f"Кратчайшие пути от вершины {start_vertex} до всех остальных:")
for i in range(len(shortest_distances)):
    print(f"Вершина {i}: {shortest_distances[i]}")

#Кратчайшие пути от вершины 2 до всех остальных:
#Вершина 0: 5
#Вершина 1: 9
#Вершина 2: 0
#Вершина 3: 15