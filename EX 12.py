def dijkstra(graph, source, destination):
    n = len(graph)
    distance = [float('inf')] * n
    visited = [False] * n
    previous = [-1] * n
    distance[source] = 0
    for _ in range(n):
        min_distance = float('inf')
        u = -1
        for i in range(n):
            if not visited[i] and distance[i] < min_distance:
                min_distance = distance[i]
                u = i
        if u == -1:
            break
        visited[u] = True
        for v in range(n):
            if graph[u][v] != 0 and not visited[v]:
                new_distance = distance[u] + graph[u][v]

                if new_distance < distance[v]:
                    distance[v] = new_distance
                    previous[v] = u
    path = []
    current = destination
    while current != -1:
        path.append(current)
        current = previous[current]
    path.reverse()
    return distance[destination], path
n = int(input("Enter number of cities: "))
print("\nEnter city names:")
cities = input().split()
while len(cities) != n:
    print("Please enter exactly", n, "city names.")
    cities = input().split()
print("\nEnter graph:")
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    while len(row) != n:
        print("Please enter exactly", n, "values.")
        row = list(map(int, input().split()))
    graph.append(row)
print("\nAvailable cities:", ", ".join(cities))
source_city = input("Enter the source city: ").strip().upper()
destination_city = input("Enter the destination city: ").strip().upper()
if source_city in cities and destination_city in cities:
    source = cities.index(source_city)
    destination = cities.index(destination_city)
    distance, path = dijkstra(graph, source, destination)
    if distance == float('inf'):
        print("\nNo path exists between", source_city, "and", destination_city)
    else:
        print("\nShortest Path:", end=" ")
        for i in range(len(path)):
            print(cities[path[i]], end="")
            if i != len(path) - 1:
                print(" -> ", end="")
        print("\nShortest Distance:", distance)
else:
    print("\nError: Invalid city name entered.")
