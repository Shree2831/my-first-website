def dijkstra(graph, source, destination):
    n = len(graph)
    distance = [999] * n
    visited = [False] * n
    parent = [-1] * n

    distance[source] = 0

    for i in range(n):
        min_dist = 999
        u = -1

        for j in range(n):
            if not visited[j] and distance[j] < min_dist:
                min_dist = distance[j]
                u = j

        if u == -1:
            break

        visited[u] = True

        for v in range(n):
            if graph[u][v] != 0 and not visited[v]:
                new_dist = distance[u] + graph[u][v]

                if new_dist < distance[v]:
                    distance[v] = new_dist
                    parent[v] = u

    path = []
    current = destination

    while current != -1:
        path.append(current)
        current = parent[current]

    path.reverse()

    print("\nShortest Path:", end=" ")
    for i in path:
        print(i + 1, end=" ")

    print("\nShortest Distance:", distance[destination])



n = int(input("Enter number of cities: "))


print("Enter the adjacency matrix:")
graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)


source = int(input("Enter source city: ")) - 1
destination = int(input("Enter destination city: ")) - 1


dijkstra(graph, source, destination)
