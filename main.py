# Número de nodos en el grafo
V = 4

# Valor que representa una distancia infinita
INF = float("inf")

# Función para imprimir la matriz de distancias
def imprimir_matriz(dist):
    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                print("INF", end=" ")
            else:
                print(dist[i][j], end=" ")
        print()

# Función para resolver el problema de shortest paths usando el algoritmo de Floyd-Warshall
def floyd_warshall(graph):
    dist = [[0] * V for _ in range(V)]

    # Inicializa la matriz de distancias con los valores del grafo
    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]

    # Actualiza la matriz de distancias considerando todos los vértices como intermediarios
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    imprimir_matriz(dist)

# Ejemplo de grafo de entrada
graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

# Llama a la función Floyd-Warshall con el grafo de ejemplo
floyd_warshall(graph)
